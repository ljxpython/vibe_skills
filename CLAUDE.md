<!-- 
注意：此项目已移除 OpenSpec 框架，现在使用自定义工作流。
不再包含 OpenSpec 受管指令块。
-->

# 目录结构

```
.
├── .opencode/                # OpenCode 权威工作流（agents/commands/skills/config）
│   ├── agents/               # 子代理定义（并行/隔离）
│   ├── commands/             # 斜杠命令（入口协议）
│   ├── skills/               # Skills（渐进式披露）
│   └── opencode.json         # OpenCode 项目级权威配置（不含密钥）
├── knowlege/                 # 知识沉淀（skills/commands 总结）
│   └── skills-commands-best-practices.md
├── docs/                     # 项目文档与问题复盘
│   └── problem.md
├── rules/                    # AI 代理规则版本
│   ├── AGENTS_v1.md
│   └── AGENTS_v2.md
├── AGENTS.md                 # 交互/风格/行为约束
├── README.md                 # 仓库说明与用法
└── CLAUDE.md                 # AI 助手指令说明
```

# 模块职责

- `.opencode/skills/`: Skills 主体与资源（SKILL.md、templates、scripts、references）。
- `.opencode/commands/`: 斜杠命令目录（例如 `/keep-off`、`/审计`、`/测试计划`）。
- `.opencode/agents/`: 子代理（并行检索/门禁/落盘）。
- `knowlege/`: 与 Skills/Commands 相关的知识总结与落地指南。
- `docs/`: 项目文档与问题复盘（含 `problem.md`）。
- `rules/`: AGENTS 规则版本备份。
- `AGENTS.md`: 统一交互规范与行为约束。
- `README.md`: 仓库整体用途、约定与安装方式。

## 工作流权威文档

- `docs/workflow/00-overview.md`

# 依赖与边界

- `knowlege/` 依赖 `.opencode/skills/` 的结构与规范作为参考来源。
- `AGENTS.md` 为行为约束主入口，`rules/` 仅用于版本记录。

# 变更记录

- 2026-01-18: 新增 `knowlege/` 作为 Skills/Commands 知识沉淀目录。
