# 启动流程与检查清单

## 0. 项目记忆文件（强制）

- 在项目根目录创建：
  - `project_context.md`（项目背景/技术栈/架构总览的短文件，强烈建议）
  - `task_plan.md`（阶段/下一步）
  - `findings.md`（事实/证据/决策细节）
  - `progress.md`（做了什么/改了哪些文件/错误与修复）
- 模板：
  - `task_plan.md` / `findings.md` / `progress.md` 来自 `planning-with-files` skill
  - `project_context.md` 来自 `project-kickoff/templates/project_context.md`

### 新窗口恢复读取顺序（强制）

1) `project_context.md`（若存在，先读；用于恢复背景与技术栈）
2) `task_plan.md`
3) `findings.md`
4) `progress.md`

### 0.1 新窗口恢复产出（Resume Snapshot，强制）

恢复三文件后，必须输出并（推荐）写回 `progress.md` 的一段短锚点，格式固定如下：

```markdown
## Resume Snapshot

- Current Phase: <从 task_plan.md 提取；缺失则 Unknown>
- Goal: <从 task_plan.md 提取；缺失则 Unknown>
- Next 3 Actions:
  1) <可执行动作 1>
  2) <可执行动作 2>
  3) <可执行动作 3>
- Open Questions / Blockers:
  - <只列真正阻塞下一步的问题；文件中已有答案的禁止再问>
```

最小提问原则：只问文件里缺失的关键字段，一次最多 1~2 个问题。严禁让用户重述整个需求与进展。

## 1. 前置条件对齐

### 1.1 快速路径：套装模板（可选，优先支持）

当用户明确表达“直接套模板/快速开工/不要一步步问”，优先提供“套装模板”选项，跳过冗长的方案确认。

选项菜单（固定问法，建议默认 1）：

```
请选择启动方式：
1) 套装模板（推荐，最快跑通真链路）：antpro-fastapi-starter（Ant Design Pro + FastAPI + SQLite）
2) 自定义方案（按问答逐步收敛架构/技术栈）

回复 1 或 2。
```

- 模板仓库：`https://github.com/ljxpython/antpro-fastapi-starter.git`
- 落地手册：`references/antpro-fastapi-starter.md`
- 模板特性：前端 Ant Design Pro（Umi4 + TS） + 后端 FastAPI + SQLite，前端通过 `/api` 代理后端，禁止 mock

快速路径只允许做最小确认：
- 项目目录名（默认 `antpro-fastapi-starter` 或用户指定）
- 端口占用（默认 8000/8001）

确认后直接进入：clone -> install -> start -> verify，并把该决策写入 `project_context.md` / `task_plan.md` / `progress.md`。


## 1. 前置条件对齐

- 目标：业务/技术结果
- 约束：时间、成本、依赖、平台、合规
- 输入资料：需求文档、现有系统、日志或数据
- 成功标准：可验证的通过条件

## 2. 角色分工与协作

- 与用户确认需要配合完成的事项
- 明确用户需要提供的材料与资源
- 明确谁负责验证、谁做实现、谁做评审

## 3. 证据优先

- 先找资料再讨论方案
- 结论必须附证据与来源
- 讨论维度：是什么 / 为什么 / 怎么做 / 是否最合适

## 4. 三段论开发法

- 正：先给主路径，确保能跑通
- 反：审计失败模式、边界、性能、安全
- 合：收敛接口、依赖、测试与文档

## 5. 依赖复用与链路真实性

- 优先复用成熟库/仓库
- 禁止 mock / demo 代替真实链路
- 禁止降级链路

## 6. 用户方案辩证

- 明确风险与替代方案
- 若存在明显问题必须先提醒

## 7. 产出与记录

- 每阶段输出结论、证据、下一步，并同步更新 `task_plan.md` / `findings.md` / `progress.md`
- 文档记录默认放 `docs/`
- `docs/` 组成：
  - `project-summary.md`：小项目总结
  - `problem.md`：错误与修复记录（含避免再犯）
  - `review.md`：审查记录（来自 /review）
  - `test-plan.md`：测试计划（来自 /test-plan）
- 需要技术架构图/时序图时必须使用 Mermaid

## 输出结构模板

- 目标与范围
- 已知约束与未知点
- 方案候选（含对比）
- 推荐方案与理由（含证据）
- 资源/资料需求清单
- 下一步可执行计划
