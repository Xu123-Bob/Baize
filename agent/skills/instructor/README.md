# 🧑‍🏫 Instructor Skill — AI Agent 培训师

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Skill](https://img.shields.io/badge/Claude-Skill-blue)](https://claude.com)

> 一个专为 Claude Code 设计的技能（Skill），用于在 VibeCoding 过程中实时讲解 Agent 内部组件（Skills、Subagent、MCP、Hook、CI/CD 等）的运行机制，让初学者也能边用边学。

---

## 📖 简介

`instructor` 是一个 **渐进式披露** 的技能。当 Agent 执行某项任务时，它会主动在聊天界面中以 `<组件名 开始运行>` 的形式告知用户当前使用的是哪个组件、该组件的作用是什么，以及相关的技术细节。

**核心理念**：让用户在实际操作中理解 Agent 的构成，降低学习门槛。

---

## ✨ 功能特性

- ✅ **实时讲解** – 当 Agent 触发关键组件时，自动给出清晰的中文说明
- ✅ **覆盖六大核心组件** – CLAUDE.md、Skills、Subagent、Hook、MCP、CI/CD & Headless
- ✅ **类型标注** – 明确告知 Subagent 的类型（只读/执行/并行/流水线/团队）、Skill 的触发方式（自动/命令）等
- ✅ **MCP 能力解析** – 区分 Tools、Resources、Prompts，并说明传输方式（stdio/HTTP）
- ✅ **Hook 事件分类** – 识别 17 种事件类型（如 PreToolUse、SubagentStart 等）
- ✅ **CI/CD 安全准则** – 提醒最小权限、Secrets 管理、审计日志等最佳实践

---

## 🚀 快速开始

### 前置条件

- 已安装 [Claude Code](https://docs.anthropic.com/zh-CN/docs/claude-code) 或支持 Skills 的 Agent 环境

### 安装步骤

1. **下载技能文件**  
   将本仓库中的 `instructor.md` 下载到本地。

2. **放入 Skills 目录**  
   将 `instructor.md` 放到 Claude Code 的 Skills 文件夹中（通常为 `~/.claude/skills/` 或项目根目录下的 `.claude/skills/`）。

   ```bash
   cp instructor.md ~/.claude/skills/