# Python 后端（简单）模板

## 目录结构

```
project/
├── README.md
├── .gitignore
├── .env
├── .env.example
├── pyproject.toml
├── src/
│   ├── main.py
│   ├── app.py
│   └── config.py
└── tests/
    └── test_smoke.py
```

## 依赖管理（uv）

- 安装 uv（如未安装）：
  - macOS/Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
  - Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
- 初始化项目：`uv init`
- 安装依赖：`uv add fastapi uvicorn`
- 运行：`uv run src/main.py`

## Python 版本

- 默认使用最新稳定版（3.13）
- 安装：`uv python install 3.13`
- 写入默认版本：`.python-version`

## 初始化步骤

1. `mkdir project && cd project`
2. `uv init`
3. `uv python install 3.13`
4. `uv add fastapi uvicorn`
5. 创建 `src/main.py` 启动入口

## 语言规范

- 命名清晰，函数单一职责
- lint/format：ruff + black
