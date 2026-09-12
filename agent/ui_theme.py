from rich.console import Console
from rich.theme import Theme
from rich.panel import Panel
from rich.markdown import Markdown
from rich.text import Text
from rich.syntax import Syntax
from rich import box
import re
from rich.status import Status
import sys
from rich import box

# 定义黑金主题
BLACK_GOLD_THEME = Theme({
    "info": "bold gold1",
    "warning": "bold yellow3",
    "error": "bold red1",
    "success": "bold bright_green",
    "frame": "gold1",
    "thinking": "dim grey62",
    "code": "on grey11",
    "diff_add": "bold bright_green",
    "diff_del": "bold red1",
    "bold": "bold",
})

# 创建全局控制台对象
console = Console(theme=BLACK_GOLD_THEME)

def render_thinking(content: str, show_full: bool = False):
    """渲染思考内容：默认显示前300字符，并提示 /show thought 查看完整"""
    if not content:
        return
    console.print()  # 空行分隔（前面）
    truncated = content[:300] + ('...' if len(content) > 300 else '')
    # 统一使用“思·穷究万物”，金色边框
    title = "[info]✦ 思·穷究万物[/info]"
    if show_full:
        # 完整展示（一般用于内部调试或未来功能扩展）
        console.print(Panel(content, title=title, border_style="gold1", style="grey62")) #content, title="[info]白泽思考[/info]", border_style="gold1", style="grey62")
    else:
        console.print(Panel(f"[dim]{truncated}[/dim]", title=title, border_style="gold1", style="grey62"))
        console.print("[dim]输入 /show thought 查看完整思考[/dim]")
    console.print()  # 空行分隔（后面）

# -------------------- LLM 状态行（不覆盖输入栏） --------------------
def llm_status(round_num: int, total_tokens: int):
    """
    打印 LLM 调用状态（使用原生 ANSI 清行）。
    整行统一为金黄色，包含中断提示。
    """
    if total_tokens >= 1000:
        token_display = f"{total_tokens/1000:.1f}K"
    else:
        token_display = str(total_tokens)
    # 核心状态信息（金色为主）
    status = f"⏳ 链接神机 · 第{round_num}轮 [算力: {token_display}]" #Calling LLM (round {round_num}) [Total tokens: {token_display}]
    # 中断提示（灰色，带中括号）
    hint = " \033[90m[按 Ctrl+C 可中断]\033[0m"   # 灰色
    message = status + hint
    # \r 回到行首，\033[2K 清除整行，\033[38;5;220m 设置为金色，\033[0m 恢复默认
    sys.stdout.write(f"\r\033[2K\033[38;5;220m{message}\033[0m")
    sys.stdout.flush()

# -------------------- 格式化内容（支持代码块、加粗、diff颜色） --------------------
def render_formatted_content(content: str):
    """
    按行渲染内容，模拟原 print_formatted_content：
    - 检测代码块，使用 Syntax 高亮
    - 处理 **加粗**
    - + 行显示绿色，- 行显示红色
    """
    lines = content.splitlines()
    in_code = False
    code_buffer = []
    code_lang = "text"

    for line in lines:
        # 检测代码块边界
        stripped = line.strip()
        if stripped.startswith("```"):
            if in_code:
                # 结束代码块，渲染
                code_text = "\n".join(code_buffer)
                syntax = Syntax(code_text, code_lang, theme="monokai", line_numbers=False)
                console.print(syntax)
                code_buffer = []
                in_code = False
            else:
                # 开始代码块，提取语言
                in_code = True
                # 获取语言（例如 ```python）
                lang = stripped[3:].strip()
                code_lang = lang if lang else "text"
                code_buffer = []
            continue

        if in_code:
            code_buffer.append(line)
        else:
            # 非代码块：处理加粗和diff颜色
            # 先处理 **加粗**
            line = re.sub(r'\*\*(.*?)\*\*', r'[bold]\1[/bold]', line)
            if line.startswith('+ '):
                console.print(f"[diff_add]{line}[/diff_add]")
            elif line.startswith('- '):
                console.print(f"[diff_del]{line}[/diff_del]")
            else:
                console.print(line)

def render_answer(content: str):
    """渲染回答内容：优先使用 Markdown，若包含代码块则交给 render_formatted_content"""
    if not content:
        return
    console.print()  # 空行分隔（前面）
    title = "[bold gold1]✦ 天启 · 真言显化[/bold gold1]"
    # 简单判断是否包含代码块，如果有则使用 render_formatted_content 保持原样式
    if '```' in content:
        console.print(Panel("", title=title, border_style="gold1", padding=(1,2)))  #title="[bold gold1]白泽[/bold gold1]"，无box=box.DOUBLE_EDGE
        render_formatted_content(content)
        console.print()  # 添加底部空隙
    else:
        md = Markdown(content)
        console.print(Panel(md, title=title, border_style="gold1", padding=(1,2)))
    console.print()  # 空行分隔（后面）

def render_tool_call(name: str, arguments: str):
    """渲染工具调用摘要（压缩参数到50字符）"""
    if not name:
        return
    console.print()  # 空行分隔（前面）
    args_preview = arguments.replace('\n', ' ')[:50]
    if len(arguments) > 50:
        args_preview += '...'
    console.print(f"[gold1]施法·灵器『{name}』[/gold1] [dim]({args_preview})[/dim]") #print(f"[[gold1]工具调用[/gold1]] {name}({args_preview})", style="grey74")
    console.print()  # 空行分隔（后面）

def render_tool_result(tool: str, result: str):
    """渲染工具结果摘要（压缩结果到200字符）"""
    if not result:
        return
    console.print()  # 空行分隔（前面）
    result_preview = result.replace('\n', ' ')[:200]
    if len(result) > 200:
        result_preview += '...'
    console.print(f"[dim]灵器·回响 {result_preview}[/dim]") #f"[dim][结果] {result_preview}[/dim]"
    console.print()  # 空行分隔（后面）

def render_final(content: str):
    """渲染最终回答，使用 render_formatted_content 或 Markdown"""
    if not content:
        console.print("[dim]（无所得）[/dim]") #"[dim]（Agent 未生成回答）[/dim]"
        return
    console.print()  # 空行分隔（前面）
    console.rule("[bold gold1]✦ 天机已明[/bold gold1]", style="gold1") #"[bold gold1]最终结果[/bold gold1]", style="gold1"
    if '```' in content:
        render_formatted_content(content)
    else:
        md = Markdown(content)
        console.print(Panel(md, border_style="gold1", padding=(1,2)))
    console.print()  # 空行分隔（后面）

def render_system(message: str):
    """渲染系统消息"""
    if not message:
        return
    console.print()  # 空行分隔（前面）
    console.print(f"[bold yellow3][系统][/bold yellow3] {message}")
    console.print()  # 空行分隔（后面）