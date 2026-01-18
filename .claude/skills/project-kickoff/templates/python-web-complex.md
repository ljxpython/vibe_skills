# Python + Web 前后端（复杂）模板

## 目录结构

```
project/
├── README.md
├── .gitignore
├── docker-compose.yml
├── docs/
│   ├── architecture.md
│   └── deployment.md
├── frontend/
│   └── (Ant Design Pro 项目)
└── backend/
    ├── pyproject.toml
    ├── src/
    │   ├── api/
    │   ├── core/
    │   ├── data/
    │   └── external/
    ├── scripts/
    │   └── init_db.sh
    └── tests/
        ├── unit/
        └── integration/
```

## 前端初始化（Ant Design Pro）

- 使用 pro-cli（必须完成安装）：
  - `npm i @ant-design/pro-cli -g`
  - `pro create myapp`
  - 选择 `umi@4`
  - 选择 `simple`
  - `cd myapp && yarn` 或 `npm install`

## 前端包管理器

- 默认 pnpm（如未安装需先安装）
- 也可选择 yarn

## 后端依赖管理（uv）

- 安装 uv（如未安装）：
  - macOS/Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
  - Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
- `cd backend && uv init`
- `uv python install 3.13`
- `uv add fastapi uvicorn pydantic sqlalchemy alembic`

## 初始化步骤（示例）

1. `mkdir project && cd project`
2. `mkdir frontend backend docs`
3. `cd frontend && pnpm create umi`（选择 Ant Design Pro）
4. `cd ../backend && uv init`
5. `uv python install 3.13 && uv add fastapi uvicorn pydantic sqlalchemy alembic`

## 语言规范

- 前端遵循 Ant Design Pro 默认规范
- 后端 lint/format：ruff + black + mypy
