---
name: env-init
description: |
  项目首次初始化（仅第一次）。使用 uv 初始化 Python 环境，并生成前端/后端技术架构（目录骨架+架构文档）。
  适用：新项目第一次创建；需要快速落地“可跑的真实链路”或“骨架+文档”。
  不适用：项目已初始化（此时应使用 resume-handshake / kickoff-rules / 变更门禁命令）。
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - WebFetch
  - WebSearch
---

# 项目首次初始化（env-init）

## 目标

在“第一次初始化”场景下，完成两类产出（A+B 同时支持）：

1) A: 生成前后端技术架构
- 创建目录骨架：`frontend/` + `backend/`
- 生成 `docs/architecture.md`：模块边界、目录树、数据流、接口约定

2) B: 模板启动（可选但推荐）
- 默认推荐：`antpro-fastapi-starter`（前端 Ant Design Pro + 后端 FastAPI + SQLite，禁 mock）

## 强制前置检查

1. 如果发现项目已初始化（存在 `.opencode/state/initialized.json`），必须停止并提示改用：
   - `/继续`
   - `/启动规则`
   - `/改动开始`
2. 强制使用 uv（不提供 poetry 方案）。

## 执行流程（必须按序）

### Step 1: 创建项目目录

- 由命令 `/keep-off <project-dir>` 传入目标目录。
- 在目标目录下创建：`.opencode/state/` 与初始化标记文件。

### Step 2: uv 初始化 Python 环境（后端）

- 参考：`references/uv-setup.md`
- 目标：后端目录 `backend/` 下具备可用的 uv/venv 初始化与最小可运行 FastAPI 依赖方案（仅骨架时可只生成配置与 README）。

### Step 3: 生成前后端架构骨架

- 创建目录：`frontend/`、`backend/`、`docs/`
- 生成 `docs/architecture.md`，至少包含：
  - 目录结构树
  - 前后端边界
  - API 约定（路径前缀、错误码、鉴权占位）
  - 本地开发端口约定

### Step 4: 模板启动（可选）

- 当用户选择“模板启动”时：
  - 参考：`references/antpro-fastapi-starter.md`
  - 目标：clone -> install -> start -> verify
  - 把关键决策写入 `docs/architecture.md` 与 `progress.md`（由文档书记落盘）

## 输出要求

- 任何“安装/启动/验证”必须提供可复核证据：执行命令 + 关键输出摘要。
