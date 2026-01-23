# 工作流总览（opencode-only）

本仓库提供一套“极致 opencode-only”的个人开发工作流资产：

- 权威入口：`.opencode/`
- 组成：Agents（子代理）+ Commands（斜杠命令）+ Skills（渐进式披露）+ MCP（外部能力）

## 设计目标

1. 首次初始化可复用：`/keep-off <project-dir>` 一次性把项目跑起来（uv + 前后端骨架 + 架构文档，支持模板启动）。
2. 每次改动强制门禁：必须 `/审计` + `/测试计划` + `/执行测试`。
3. 默认并行检索：遇到不确定/跨模块，默认并行子代理 + MCP augment。
4. 证据优先：结论必须附证据（路径/输出/URL）。

## 权威目录

```
.
├── .opencode/
│   ├── opencode.json
│   ├── agents/
│   ├── commands/
│   ├── skills/
│   └── state/
└── docs/workflow/
```

继续阅读：
- `docs/workflow/10-agents.md`
- `docs/workflow/20-commands.md`
- `docs/workflow/30-skills.md`
- `docs/workflow/40-gates.md`
- `docs/workflow/50-migration.md`
