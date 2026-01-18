---
description: "按审查规范生成检查清单与逐项验证，并写入 /docs/review.md"
---

请执行以下流程：

1. 检查 `docs/` 是否存在；若不存在则创建。
2. 检查 `/docs/review.md` 是否存在；若不存在则新建并写入文件头。
3. 读取 `@.claude/skills/code-audit/references/audit-prompt.md` 作为审查规范。
4. 让用户提供 Context + Requirements Set + 需要审查的文件路径列表。
5. 生成“可执行、可审计、可复用”的检查清单，并完成逐项逻辑验证。
6. 给出放行结论（PASS/BLOCK）与阻断理由。
7. 可选运行 `python3 .claude/skills/code-audit/scripts/review_gate.py /docs/review.md --max-unknown 3` 复核结论；失败则以人工结论为准。
8. 结果追加到 `/docs/review.md`，使用时间戳标题，例如：

```
## 2026-01-18 审查标题
```
