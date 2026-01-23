---
name: kickoff-rules
description: |
  项目启动后的工作流治理协议：强制门禁、默认并行检索、落盘规则、opencode-only 约束。
  适用：进入持续开发前；或需要重申/更新工作法时。
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
---

# 启动规则（kickoff-rules）

## 目标

把“你的工作方式”固化成可执行、可审计的协议，覆盖：

1) 强制门禁（每次改动都必须）
- `/审计` -> `docs/review.md`
- `/测试计划` -> `docs/test-plan.md`
- `/执行测试` -> 证据写入 `progress.md`

2) 默认并行（search-mode）
- 任何需要检索/调研/不确定性的任务，默认并行：代码侦察 + 资料检索 + MCP(augment)

3) 落盘规则（强制）
- 事实/证据/决定写入 `findings.md`
- 会话动作与证据写入 `progress.md`
- 门禁输出写入 `docs/`

4) opencode-only 约束（强制）
- 禁止 superpowers / oh-my-opencode / 插件注入
- 禁止使用 `CLAUDE_PLUGIN_ROOT`
- `.opencode/` 是唯一权威来源

## 参考

- `references/rules.md`
- `references/decision-model.md`
- `references/principles.md`
