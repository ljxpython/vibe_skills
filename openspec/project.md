# Project Context

## Purpose
本仓库用于收集与沉淀我常用的：
- skills（技能说明/流程）
- commands（常用命令封装与用法）
- system prompts（系统提示词/规则约定）

目标是让人和 AI 助手在同一套“可复用、可查找、可维护”的资料库里协作与复用，而不是构建一个可运行的业务服务。

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
当前不要求 CI/自动化校验；以“人工审阅 + 文档自洽”为准。

若未来引入可执行代码或需要质量门禁，再补充测试与校验策略。

### Git Workflow
推荐（简单直接）：
- 修改完成后直接提交即可（不强制 PR/分支策略）。
- 提交信息建议：`<type>(<scope>): <message>`，其中 `<scope>` 优先用 capability 或 change-id（例如 `docs(openspec): update project context`）。

## Domain Context
给 AI 助手的“上下文真相”：
- 这是一个“技能/命令/系统提示词”的资料库，核心产物是文档与模板，而不是某个可运行服务。
- 一切讨论最终要落到“可验收”的 Requirements/Scenarios 上；任务清单（tasks.md）必须能一条条做完并打勾。
- 文档里出现的受管区块（例如带 `OPENSPEC:START/END` 的片段）不要手贱乱改，保持可被工具自动更新。

## Important Constraints
- 不要编造不存在的业务与技术栈：本仓库不承诺存在业务代码与运行时环境。
- 执行命令时路径统一用双引号包裹，避免空格/特殊字符把你坑死。

## External Dependencies
无外部依赖。
