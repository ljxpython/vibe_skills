---
description: "项目首次初始化：创建新项目目录，使用 uv 初始化 Python 环境，并生成前后端架构骨架（支持模板启动）。"
agent: build
---

你正在执行“首次初始化”命令。

输入参数：
- 目标项目目录：`$1`

必须按序执行：

1) 参数检查
- `$1` 为空：直接 BLOCK，提示用法：`/keep-off <project-dir>`

2) 创建目录并进入
- 创建目录 `$1`（若已存在，BLOCK，除非用户明确同意复用）

3) 注入工作流（必须）
- 把本仓库的 `.opencode/` 复制到新项目目录：`$1/.opencode/`
- 复制前若 `$1/.opencode/` 已存在：直接 BLOCK（避免覆盖已有工作流）

4) 初始化标记（防止二次执行）
- 若 `$1/.opencode/state/initialized.json` 已存在：直接 BLOCK，提示改用 `/继续`
- 否则创建 `$1/.opencode/state/initialized.json`，至少写入：初始化时间、uv、目录骨架版本

5) 执行 env-init skill（只在 `$1` 目录内）
- 加载 skill：`env-init`
- 严格按 skill 流程完成：uv 初始化 + `frontend/` + `backend/` + `docs/architecture.md`

6) 结束提示
- 告诉用户下一步：在新项目目录中运行 `/启动规则` 以启用强制门禁协议
