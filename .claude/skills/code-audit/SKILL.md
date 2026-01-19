---
name: code-audit
description: |
  代码审查与可审计检查清单生成。适用于“代码审查/review/CR/代码评审/质量检查/规范核查/架构评审/合规审计/门禁/gate”等场景。
  也适用于用户希望直接生成审查记录或触发命令：`/review`。
  触发后必须按审查规范生成可判定检查点与逐项验证，并产出审查记录。
  不适用：纯实现需求讨论、未提供需求规范时的随意建议。
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash
---

# 代码审查与审计 Skill

## 强制流程

1. 读取 `references/audit-prompt.md` 作为审查规范
2. 要求用户提供 Context + Requirements Set
3. 生成可判定检查清单与逐项逻辑验证
4. 给出放行结论（PASS/BLOCK）与阻断理由
5. 可选运行 `scripts/review_gate.py` 复核结论；脚本失败则以人工结论为准
6. 输出审查结论并写入 `docs/review.md`

## 输出要求

- 使用规范化结构（CP-yi-xx）
- 每个检查点必须可判定（Yes/No/Unknown）
- 若信息不足，标 Unknown 并提出补充项

## 产出

- `docs/review.md`（审查记录）
