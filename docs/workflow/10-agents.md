# Agents（子代理）

本仓库约定 2 个 primary + 6 个 subagent。

## Primary

1) 主执行（build）
- 职责：实现改动、协调并行子代理、落地与收尾。

2) 主规划（plan）
- 职责：只读分析、方案设计、风险/验收标准。
- 默认禁止写文件/跑 bash。

## Subagents

1) 代码侦察（@code-scout）
- 只读扫描：入口/模式/引用点 -> 输出“证据 + 结论 + Unknown”。

2) 资料检索（@librarian）
- 外部资料：官方��档/GitHub 示例/文章 -> 必须附 URL。

3) 工作流设计（@workflow-designer）
- 只读推导：把你的习惯固化成 commands+skills+agents 的契约。

4) 审计门禁（@gate-audit）
- 只读审计：Yes/No/Unknown 检查点 + PASS/BLOCK。

5) 测试门禁（@gate-test）
- 生成测试计划；必要时执行测试命令并给证据（不写文件）。

6) 文档书记（@scribe）
- 专职落盘：`docs/**` + 记忆文件（不联网、不跑 bash）。
