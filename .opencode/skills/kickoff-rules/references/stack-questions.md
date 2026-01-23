# 启动问答清单（模板路由）

用于在项目开始阶段快速定位模板与初始化方式。

## 必问问题

1. 项目类型：纯后端 / 前后端分离 / 全栈 / 其他
2. 复杂度：简单 / 复杂（服务数>3、需要部署脚本、CI/CD 视为复杂）
3. 语言与框架：例如 Python + FastAPI
4. Python 版本：默认最新稳定版（3.13），是否有固定版本要求
5. 依赖管理：Python 使用 uv；前端使用 pnpm 或 yarn
6. 前端框架：默认 Ant Design Pro（基于 Umi）是否接受
7. 部署方式：本地 / Docker / k8s / 云
8. 目录结构：采用默认模板还是自定义
9. 初始化结果：仅结构/依赖清单，还是要生成初始化脚本

## 路由规则（简化）

- Python 后端 + 简单 → `templates/python-backend-simple.md`
- Python 后端 + 复杂 → `templates/python-backend-complex.md`
- 前后端分离 + 简单 → `templates/python-web-simple.md`
- 前后端分离 + 复杂 → `templates/python-web-complex.md`
