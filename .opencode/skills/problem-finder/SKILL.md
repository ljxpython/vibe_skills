---
name: problem-finder
description: |
  问题复盘与复用指引。适用于“遇到问题/报错/error/失败/fail/故障/卡住/排查/debug/回溯原因/root cause/类似问题/以前怎么解决”等场景。
  也适用于用户希望输出问题复盘文档或触发命令：`/problem-summary`。
  触发后必须先检索 `docs/problem.md` 是否有相似问题与解决方案，再决定下一步。
  不适用：纯功能实现、无问题排查需求的需求讨论。
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash
---

# 问题复盘与复用 Skill

## 强制流程

1. 检查 `docs/problem.md` 是否存在
2. 若存在：搜索相似问题（按关键词/模块/报错信息）
3. 若找到：优先复用既有方案，并说明差异
4. 若未找到：按常规流程排查并在完成后生成问题记录（使用 `/problem-summary` 命令）

## 搜索策略

- 以“错误码/异常类型/模块名/关键日志”做主关键词
- 至少尝试 2 组关键词组合
- 若未命中，扩大到同类模块或同类依赖

## 输出要求

- 明确说明是否找到相似问题
- 给出复用理由或差异说明
- 若复用：列出对应记录标题与路径
