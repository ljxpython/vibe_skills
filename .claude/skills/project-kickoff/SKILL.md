---
name: project-kickoff
description: |
  项目启动与方案讨论的启动流程 + 跨窗口恢复协议。适用于“项目开始/初始化/立项/方案讨论/方案设计/技术选型/需求澄清/项目继续/继续上次/resume/continue”等场景。
  关键能力：当用户说“项目继续/继续上次”时，必须先基于磁盘持久化文件恢复上下文（project_context.md（若存在）-> task_plan.md -> findings.md -> progress.md），再讨论下一步。
  提供：启动清单、前置条件确认、协作分工、证据要求、方案三段论流程。
  不适用：具体实现细节编码、单一函数优化、纯跑测试。
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - WebFetch
  - WebSearch
  - Bash
---

# 项目启动与方案讨论 Skill

## 目标

在项目启动阶段建立正确的上下文、约束与协作方式，避免闭门造车和无证据决策，形成可执行的方案路径。

## 触发信号

当用户提到以下意图时，必须启用本流程：

- 项目开始 / 初始化 / 立项
- 方案讨论 / 方案设计 / 技术选型
- 需求澄清 / 想法评审 / 方向对齐

## 启动流程（必须按序执行）

详见：`references/workflow.md`

## 新窗口恢复协议（Resume Handshake，强制）

> 目标：让 skill 在 Codex / OpenCode 等“无自动 SessionStart hook”的宿主里也能恢复：项目背景 + 技术栈 + 已做工作 + 下一步。
> 手段：把“恢复”变成一个幂等、可审计的固定步骤（文件），而不是依赖模型记忆。

### 0. 恢复优先级（不可跳过）

当用户表达任意“继续/恢复”意图（例如：项目继续 / 继续上次 / resume / continue），必须先执行：

1. 定位项目根目录（本仓库约定的记忆文件所在目录）。
2. 读取 `project_context.md`（若存在；这是项目背景总入口）。
3. 按固定顺序读取三文件：`task_plan.md` → `findings.md` → `progress.md`。
4. 输出“恢复锚点”（见下方模板），只针对文件中缺失的关键字段提问。

严禁：在未读取上述文件前，让用户重复描述需求、背景或进展。

### 1. 根目录定位规则（必须执行）

- 默认认为当前工作目录就是项目根目录。
- 若当前目录不存在 `task_plan.md`：
  - 使用 `Glob` 在工作区内查找 `task_plan.md`（优先最近修改的一个）。
  - 若找到多个候选：只问用户 1 个问题让其选择（列出候选路径）。
  - 若一个都找不到：按“项目开始”流程初始化规划文件（或请求用户提供项目根路径）。

### 2. 文件职责与读取顺序（必须固定）

- `project_context.md`（可选但推荐）：项目背景与技术栈的短总览（优先读取）
- `task_plan.md`：目标/阶段/下一步（必须读取）
- `findings.md`：已知事实/决定/证据（必须读取）
- `progress.md`：近期动作/当前阻塞/改了哪些文件（必须读取）

### 3. 恢复锚点输出（必须输出）

读取文件后，必须用以下结构输出一段短文本（让用户确认即可开干）：

- `Project`: 从 `project_context.md` 提取 one-liner；缺失则用 task_plan.md 的 Goal 兜底。
- `Tech Stack`: 从 `project_context.md` 提取；若缺失则标 `Unknown` 并要求补 3~5 行（不要重写全文）。
- `Current Phase`: 从 `task_plan.md` 提取；若缺失则标 `Unknown` 并要求补一行到 `task_plan.md`。
- `Next 3 Actions`: 基于 `task_plan.md` / `progress.md` 归纳最多 3 条可执行动作。
- `Open Questions / Blockers`: 只列文件里没有答案、且会阻塞下一步的点。

建议（可选但推荐）：把这段锚点以“Resume Snapshot”追加到 `progress.md` 的最新 Session 段落，方便下次恢复时更快。

### 4. 维护策略（强制）

- 当发生以下事件之一，必须更新 `project_context.md`：
  - 技术栈变化（例如换框架/数据库/部署方式）
  - 架构决策落地（新增关键模块/关键接口）
  - 目标或范围发生变化
- 其他日常进展只更新：`task_plan.md` / `progress.md`。

### 5. 最小提问原则（强制）

- 只问“文件里缺的关键信息”，一次最多问 1~2 个问题。
- 如果用户说“项目继续”，默认继续当前 phase，不要把它当成新项目。
- 如果 `project_context.md` + 规划文件都存在（project_context.md/task_plan.md/findings.md/progress.md）：禁止问“请描述需求/背景”。

### 6. 失败兜底（强制）

如果恢复时发现文件存在但信息极不完整（例如 Goal/Phase/Tech Stack 全缺）：
- 先输出你从文件中能确定的最小事实。
- 然后明确要求用户只补齐以下字段（不要让用户重写整份需求）：
  1) Goal（一句话，task_plan.md）
  2) Current Phase（单值，task_plan.md）
  3) Next 3 Actions（最多 3 条，task_plan.md 或 progress.md）
  4) Tech Stack（3~5 行，project_context.md）


## 强制规则

- 行动前必须与用户确认配合事项、必要信息与资源
- 需要技术架构图/时序图时使用 Mermaid
- 阶段性产出与错误修复记录必须写入 `docs/`
- 架构级变更的文档统一写入 `docs/`

## 强制联动：planning-with-files

- 必须在项目根目录创建：
  - `project_context.md`（项目背景/技术栈/架构总览的短入口，强烈建议）
  - `task_plan.md`
  - `findings.md`
  - `progress.md`
- 模板来源：
  - `task_plan.md` / `findings.md` / `progress.md` 来自 `planning-with-files` skill
  - `project_context.md` 来自 `project-kickoff/templates/project_context.md`
- 新窗口恢复读取顺序（固定）：`project_context.md`（若存在）→ `task_plan.md` → `findings.md` → `progress.md`
- 不允许跳过此步骤

## 项目启动问答（模板路由）

详见：`references/stack-questions.md`

## 模板与初始化

- `templates/python-backend-simple.md`
- `templates/python-backend-complex.md`
- `templates/python-web-simple.md`
- `templates/python-web-complex.md`

## 套装模板（快速路径，强制支持）

当用户明确选择“直接套用简易前后端模板/不要一步步问/快速开工”时，必须提供一个可直接落地的选项：

- 套装模板：Ant Design Pro（Umi4 + TS） + FastAPI + SQLite
- 安装/部署/启动手册：`references/antpro-fastapi-starter.md`

### 快速路径的协作规则（必须遵守）

- 只做“最小确认”，不做长问答：
  1) 项目目录名（默认使用用户当前目录名）
  2) 是否允许占用端口 `8000`（前端）/`8001`（后端）（默认允许）
- 用户确认后，直接进入“安装 -> 启动 -> 验证”的落地流程（详见 `references/antpro-fastapi-starter.md`）。
- 仍然必须创建/维护项目记忆文件（project_context.md/task_plan.md/findings.md/progress.md），并把模板选择写入其中。


## 环境与工具

- `references/uv-setup.md`
- `references/ant-design-pro.md`

## 关键原则与约束（强制遵守）

详见：
- `references/principles.md`
- `references/dependency-reuse.md`

## 方案决策模型（强制遵守）

详见：`references/decision-model.md`
