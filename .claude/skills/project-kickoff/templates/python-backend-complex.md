# Python 后端（复杂）模板

## 目录结构

```
project/
├── README.md
├── .gitignore
├── .env
├── .env.example
├── pyproject.toml
├── docs/
│   ├── architecture.md
│   └── development.md
├── scripts/
│   ├── init_db.sh
│   └── deploy.sh
├── src/
│   ├── main.py
│   ├── app.py
│   ├── config.py
│   ├── api/
│   ├── core/
│   ├── data/
│   └── external/
└── tests/
    ├── unit/
    └── integration/
```

## 依赖管理（uv）

- 安装 uv（如未安装）：
  - macOS/Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
  - Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
- 初始化项目：`uv init`
- 常用依赖：`uv add fastapi uvicorn pydantic sqlalchemy alembic`

## Python 版本

- 默认使用最新稳定版（3.13）
- 安装：`uv python install 3.13`

## 初始化步骤

1. `mkdir project && cd project`
2. `uv init`
3. `uv python install 3.13`
4. `uv add fastapi uvicorn pydantic sqlalchemy alembic`
5. 创建 `docs/` 与 `scripts/` 骨架

## 语言规范

- 分层清晰，禁止交叉依赖
- lint/format：ruff + black + mypy
