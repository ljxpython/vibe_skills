---
name: resume-handshake
description: |
  继续任务/恢复协议：固定读取 project_context.md -> task_plan.md -> findings.md -> progress.md，并输出 Resume Snapshot。
  适用：任何“继续/恢复/接着做”场景。
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
---

# 继续任务（resume-handshake）

## 恢复优先级（不可跳过）

当用户表达任意“继续/恢复”意图时，必须先执行：

1. 定位项目根目录（记忆文件所在目录）。
2. 依次读取：
   - `project_context.md`（若存在）
   - `task_plan.md`
   - `findings.md`
   - `progress.md`
3. 输出 Resume Snapshot（固定格式），只针对文件中缺失字段提问（一次最多 1~2 个）。

## Resume Snapshot（固定输出模板）

```markdown
## Resume Snapshot

- Current Phase: <从 task_plan.md 提取；缺失则 Unknown>
- Goal: <从 task_plan.md 提取；缺失则 Unknown>
- Next 3 Actions:
  1) <可执行动作 1>
  2) <可执行动作 2>
  3) <可执行动作 3>
- Open Questions / Blockers:
  - <只列真正阻塞下一步的问题>
```

## 维护建议（可选）

建议把最新 Resume Snapshot 追加写回 `progress.md`，方便下次恢复更��。
