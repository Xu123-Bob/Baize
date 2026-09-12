# MCP/mcp_client.py
import os
import json
import asyncio
from pathlib import Path
from typing import Dict, List, Optional, Any
import logging

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


class MCPClientManager:
    """
    管理所有 MCP 服务器连接和工具转换。
    支持内置配置（最高优先级）和用户配置合并，内置服务器永不覆盖。
    """

    def __init__(self, builtin_config_path: Optional[Path] = None):
        """
        初始化管理器。
        :param builtin_config_path: 内置配置路径（项目根目录下的 MCP/mcp_config.json）
        """
        self.builtin_config_path = builtin_config_path
        self.user_config_path: Optional[Path] = None

        # 合并后的完整服务器配置字典: server_name -> config_dict
        self._server_configs: Dict[str, dict] = {}
        # 缓存已连接会话: server_name -> ClientSession
        self._sessions: Dict[str, ClientSession] = {}
        # 缓存的工具列表（OpenAI 格式）
        self._tools_cache: Optional[List[dict]] = None

        # 如果提供了内置配置，立即加载
        if builtin_config_path:
            self.load_builtin(builtin_config_path)

    def load_builtin(self, config_path: Path):
        """
        加载内置配置，清空所有已有配置，以内置为基准。
        """
        if not config_path.exists():
            logging.warning(f"Builtin MCP config not found: {config_path}")
            self._server_configs.clear()
            self._tools_cache = None
            return

        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)

        # 假设配置顶层有 "mcpServers" 键（与现有代码一致）
        servers = config.get("mcpServers", [])
        # 转换为字典，以 name 为键
        new_configs = {s["name"]: s for s in servers if s.get("enabled", True)}
        self._server_configs = new_configs
        self._tools_cache = None
        logging.info(f"Loaded builtin MCP servers: {len(self._server_configs)}")

    def load_user(self, config_path: Path):
        """
        加载用户配置，合并到现有配置中，内置服务器不会被覆盖。
        """
        if not config_path.exists():
            logging.debug(f"User MCP config not found: {config_path}")
            return

        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)

        user_servers = config.get("mcpServers", [])
        added = 0
        for s in user_servers:
            name = s.get("name")
            if not name:
                continue
            # 只添加尚未存在的服务器（内置优先）
            if name not in self._server_configs:
                self._server_configs[name] = s
                added += 1

        self._tools_cache = None
        logging.info(f"Added {added} new MCP servers from user config (builtin preserved)")

    def get_merged_configs(self) -> List[dict]:
        """返回合并后所有启用服务器配置列表（用于连接）"""
        return list(self._server_configs.values())

    def get_tools(self) -> List[dict]:
        """返回所有 MCP 工具的工具定义（OpenAI 函数格式），供 LLM 使用"""
        if self._tools_cache is not None:
            return self._tools_cache

        tools = []
        for server_name, cfg in self._server_configs.items():
            # 每个服务器配置可能直接包含工具定义，也可能需要连接后动态获取。
            # 为保持与现有代码一致，我们假设工具列表在连接后通过 session.list_tools() 获取。
            # 但为了在连接前就能返回工具定义（用于 LLM），我们需要在 connect_all 中填充。
            # 所以这里的逻辑改为：在 connect_all 后，从已连接的会话中提取工具。
            # 更好的做法是：在连接时填充 self._tools_cache，所以这里直接返回缓存。
            # 但 get_tools 可能在 connect_all 之前调用，因此我们在此处返回空列表或抛出异常。
            # 为了安全，我们返回当前缓存（如果为空，调用者应确保已连接）。
            pass

        # 实际工具列表在 connect_all 中填充，此处直接返回缓存
        return self._tools_cache or []

    def _convert_tool(self, server_name: str, tool) -> dict:
        """将 MCP 工具转换为 OpenAI function 格式"""
        return {
            "type": "function",
            "function": {
                "name": f"mcp_{server_name}_{tool.name}",
                "description": f"[MCP:{server_name}] {tool.description}",
                "parameters": tool.inputSchema
            }
        }

    async def connect_all(self) -> List[dict]:
        """
        连接所有已配置的服务器，返回所有转换后的工具列表。
        如果之前已有连接，将先关闭并重建（实现重载）。
        """
        # 关闭已有会话
        for session in self._sessions.values():
            try:
                await session.__aexit__(None, None, None)
            except Exception:
                pass
        self._sessions.clear()
        self._tools_cache = None

        server_configs = self.get_merged_configs()
        if not server_configs:
            logging.info("No MCP servers to connect")
            return []

        all_tools = []
        for cfg in server_configs:
            name = cfg["name"]
            try:
                logging.info(f"[MCP] Connecting to server: {name}")
                params = StdioServerParameters(
                    command=cfg["command"],
                    args=cfg.get("args", []),
                    env={**os.environ, **cfg.get("env", {})}
                )
                # 使用 async with 管理连接
                read, write = await stdio_client(params).__aenter__()
                session = await ClientSession(read, write).__aenter__()
                await session.initialize()

                # 获取工具列表
                tools_result = await session.list_tools()
                self._sessions[name] = session

                # 转换工具
                for tool in tools_result.tools:
                    all_tools.append(self._convert_tool(name, tool))

                logging.info(f"[MCP] Server {name} connected, {len(tools_result.tools)} tools loaded")
            except Exception as e:
                logging.error(f"[MCP] Failed to connect server {name}: {e}")

        self._tools_cache = all_tools
        return all_tools

    def get_session(self, server_name: str) -> Optional[ClientSession]:
        """获取指定服务器的会话对象"""
        return self._sessions.get(server_name)

    async def call_tool(self, server_name: str, tool_name: str, arguments: dict) -> str:
        """调用指定服务器上的工具，返回结果字符串"""
        session = self.get_session(server_name)
        if not session:
            return f"Error: MCP server '{server_name}' not connected"
        try:
            result = await session.call_tool(tool_name, arguments)
            if hasattr(result, 'content'):
                if isinstance(result.content, list):
                    return "\n".join(str(item) for item in result.content)
                else:
                    return str(result.content)
            return str(result)
        except Exception as e:
            return f"MCP call error: {e}"

    def shutdown(self):
        """同步关闭所有连接（用于程序退出）"""
        # 由于是异步资源，需要运行事件循环来关闭
        try:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                # 如果已有循环正在运行，则创建一个新循环关闭
                asyncio.run_coroutine_threadsafe(self._close_all_sessions(), loop)
            else:
                loop.run_until_complete(self._close_all_sessions())
        except Exception:
            pass

    async def _close_all_sessions(self):
        for session in self._sessions.values():
            try:
                await session.__aexit__(None, None, None)
            except Exception:
                pass
        self._sessions.clear()
        self._tools_cache = None


# ---------- 同步包装函数（保持原有接口） ----------
_global_mcp_manager: Optional[MCPClientManager] = None


def init_mcp_client(config_path: Path, user_config_path: Optional[Path] = None) -> Optional[MCPClientManager]:
    """
    初始化全局 MCP 客户端（同步方式）。
    先加载内置配置（config_path），再加载用户配置（user_config_path，如果提供）。
    """
    global _global_mcp_manager

    manager = MCPClientManager(builtin_config_path=config_path)
    if user_config_path and user_config_path.exists():
        manager.load_user(user_config_path)

    # 连接所有服务器（异步转同步）
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        tools = loop.run_until_complete(manager.connect_all())
        loop.close()
        _global_mcp_manager = manager
        logging.info(f"[MCP] Initialized with {len(tools)} tools")
        return manager
    except Exception as e:
        logging.error(f"[MCP] Initialization failed: {e}")
        loop.close()
        return None


def reload_mcp_user_config(user_config_path: Path):
    """
    重新加载用户配置并重连（用于切换工作区后调用）。
    注意：此函数会关闭现有连接，重新连接所有服务器。
    """
    global _global_mcp_manager
    if not _global_mcp_manager:
        logging.warning("MCP manager not initialized, call init_mcp_client first")
        return

    # 加载用户配置
    _global_mcp_manager.load_user(user_config_path)

    # 重新连接（异步转同步）
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        tools = loop.run_until_complete(_global_mcp_manager.connect_all())
        loop.close()
        logging.info(f"[MCP] Reloaded user config, now {len(tools)} tools available")
    except Exception as e:
        logging.error(f"[MCP] Reload failed: {e}")
        loop.close()


def get_mcp_tools() -> List[dict]:
    """返回所有外部工具的 OpenAI 格式列表"""
    if _global_mcp_manager:
        return _global_mcp_manager.get_tools() or []
    return []


def call_mcp_tool(server_name: str, tool_name: str, arguments: dict) -> str:
    """同步调用 MCP 工具"""
    if not _global_mcp_manager:
        return "Error: MCP client not initialized"
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        result = loop.run_until_complete(
            _global_mcp_manager.call_tool(server_name, tool_name, arguments)
        )
        loop.close()
        return result
    except Exception as e:
        loop.close()
        return f"MCP call error: {e}"