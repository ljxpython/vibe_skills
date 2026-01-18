---
name: project-kickoff
description: |
  项目开始与方案讨论的启动流程。适用于“项目开始/初始化/立项/方案讨论/方案设计/技术选型/需求澄清”等场景。
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

## 强制规则

- 行动前必须与用户确认配合事项、必要信息与资源
- 需要技术架构图/时序图时使用 Mermaid
- 阶段性产出与错误修复记录必须写入 `/docs`

## 强制联动：planning-with-files

- 必须在项目根目录创建：`task_plan.md`、`findings.md`、`progress.md`
- 新窗口恢复时必须先读取三文件（顺序固定）：`task_plan.md` → `findings.md` → `progress.md`
- 不允许跳过此步骤

## 项目启动问答（模板路由）

详见：`references/stack-questions.md`

## 模板与初始化

- `templates/python-backend-simple.md`
- `templates/python-backend-complex.md`
- `templates/python-web-simple.md`
- `templates/python-web-complex.md`

## 环境与工具

- `references/uv-setup.md`
- `references/ant-design-pro.md`

## 关键原则与约束（强制遵守）

详见：
- `references/principles.md`
- `references/dependency-reuse.md`

## 方案决策模型（强制遵守）

详见：`references/decision-model.md`
