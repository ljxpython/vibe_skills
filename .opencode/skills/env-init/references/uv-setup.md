# uv 安装与 Python 版本

## 前置要求（强制）

- 必须使用 uv 进行 Python 安装、虚拟环境管理与项目初始化
- 不允许使用 venv/conda/poetry 等替代方式

## 安装 uv

- macOS/Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

## Python 版本（强制 3.13）

- 安装：`uv python install 3.13`

## 项目初始化（强制）

1. 初始化项目：`uv init`
2. 指定 Python：`uv python pin 3.13`
3. 安装依赖：`uv add <package>`
4. 运行：`uv run <command>`

## 参考来源

- https://docs.astral.sh/uv/getting-started/installation/
- https://docs.astral.sh/uv/guides/install-python/
