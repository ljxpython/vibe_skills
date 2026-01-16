# Project Context

## Purpose
本仓库用于沉淀“规范驱动”的项目资料：用 OpenSpec 管理需求/设计/任务清单，并提供一套可复用的模板与约定，方便人和 AI 助手在同一套规则下协作。

当前仓库内容以文档与模板为主（`openspec/`、`.spec-workflow/`、`.opencode/`），暂无明确的业务运行代码；后续若引入代码，请先把对应 capability 规范补齐到 `openspec/specs/`。

## Tech Stack
- 文档：Markdown（规范/模板/说明）
- 规范工具：OpenSpec（目录结构与校验流程）
- 工作流模板：`.spec-workflow/`（requirements/design/tasks 等模板）
- 其他：Git（协作与审阅）

## Project Conventions

### Code Style
- 文档语言：面向人的内容（说明、约束、日志文案）使用中文；标识符（目录名、文件名、change-id、变量/函数名等）使用简洁英文。
- Markdown 规范：
  - 标题层级清晰（`# / ## / ###`），一段只讲一件事，优先列表化。
  - 需求用语要“可验收”：优先用 **SHALL**（系统必须）描述，不写空话。
- 命名：
  - `change-id`：kebab-case + 动词开头（`add-`/`update-`/`remove-`/`refactor-`），必须唯一。
  - capability：聚焦单一能力，目录名用 kebab-case（例如 `user-auth`）。

### Architecture Patterns
本仓库默认采用 **Spec-driven development**：
- `openspec/specs/`：现状真相（what IS built / should exist as convention）
- `openspec/changes/<change-id>/`：变更提案（what SHOULD change）
- 任何“新增能力 / 行为变更 / 架构变更 / 破坏性改动”，先走 proposal，再实现/落地。

目录约定（简化版）：
```
openspec/
  project.md                # 项目约定（本文件）
  specs/<capability>/spec.md
  changes/<change-id>/
    proposal.md
    tasks.md
    design.md               # 可选，确有技术决策再写
    specs/<capability>/spec.md
```

### Testing Strategy
当前以“规范校验”替代传统测试：
- 变更提交前至少跑一次：`openspec validate <change-id> --strict --no-interactive`
- 日常保证仓库健康：`openspec validate --strict --no-interactive`

若未来引入可执行代码，再补充：
- 单元测试框架（TODO：由你确定）
- CI（TODO：是否使用 GitHub Actions/其他）

### Git Workflow
推荐（没必要搞花活）：
- `main` 为主分支，功能/变更走 PR 合并。
- PR 尽量小且聚焦：一个 change-id 对应一组完整文档（proposal/tasks/必要的 spec delta）。
- 提交信息建议：`<type>(<scope>): <message>`，其中 `<scope>` 优先用 capability 或 change-id（例如 `docs(openspec): fill project context`）。

## Domain Context
给 AI 助手的“上下文真相”：
- 这是一个“规则与模板仓库”，核心产物是 `openspec/` 下的规范与变更提案，而不是某个可运行服务。
- 一切讨论最终要落到“可验收”的 Requirements/Scenarios 上；任务清单（tasks.md）必须能一条条做完并打勾。
- 文档里出现的受管区块（例如带 `OPENSPEC:START/END` 的片段）不要手贱乱改，保持可被工具自动更新。

## Important Constraints
- 不要编造不存在的业务与技术栈：仓库目前缺少代码与依赖清单，未确认的信息一律标注 TODO 并向维护者确认。
- 变更提案必须可通过 OpenSpec 严格校验（`--strict --no-interactive`）。
- 执行命令时路径统一用双引号包裹，避免空格/特殊字符把你坑死。

## External Dependencies
- OpenSpec CLI（用于 `list/show/validate/archive` 等）
- `.spec-workflow/`（本仓库存放的规范模板；若你们有对应工具/脚本消费它，后续在此补充）
