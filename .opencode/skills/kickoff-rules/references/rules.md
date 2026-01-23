# 启动规则与门禁（权威）

## 1. 强制门禁（每次改动都必须）

任何会产生代码/配置/文档变更的任务，必须在“结束前”完成：

1) `/审计`
- 输出 `docs/review.md`
- 必须给出 PASS/BLOCK

2) `/测试计划`
- 输出 `docs/test-plan.md`
- 必须覆盖：本次改动 + E2E + 核心逻辑 + 每接口

3) `/执行测试`
- 把执行证据写入 `progress.md`：命令 + 关键结果摘要

未完成任意一项：一律视为 BLOCK。

## 2. 默认并行（最大化检索）

当出现以下信号时，默认并行：
- “不确定/先看看/调研一下/找一找/搜索”
- 涉及 2+ 模块或跨层（前后端/配置/脚本/文档）

并行策略：
- 子代理：代码侦察、资料检索
- 工具：MCP augment-context-engine

## 3. 落盘与记忆

必须维护四类文件：
- `project_context.md`：项目背景总入口
- `task_plan.md`：阶段与下一步
- `findings.md`：事实/证据/决策
- `progress.md`：会话动作/证据/改动文件

## 4. opencode-only 约束

- `.opencode/` 为唯一权威（agents/commands/skills/config）
- 禁止 `.claude/`、`agent_config/` 作为主路径
- 禁止 `CLAUDE_PLUGIN_ROOT`
