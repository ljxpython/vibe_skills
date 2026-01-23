---
description: "按 test-coverage skill 生成测试计划（本次+E2E+核心逻辑+每接口覆盖），写入 docs/test-plan.md"
---

本命令对应 skill：`test-coverage`（测试计划与覆盖策略）。

请执行以下流程：

1. 检查 `docs/` 是否存在；若不存在则创建。
2. 检查 `docs/test-plan.md` 是否存在；若不存在则新建并写入文件头。
3. 加载测试计划模板（跨宿主通用，必须执行）：
   - 优先 `Read .claude/skills/test-coverage/references/test-template.md`
   - 若该路径不存在：用 `Glob` 搜索 `**/skills/test-coverage/references/test-template.md`
4. 加载接口扫描规则（跨宿主通用，必须执行）：
   - 优先 `Read .claude/skills/test-coverage/references/api-scan.md`
   - 若该路径不存在：用 `Glob` 搜索 `**/skills/test-coverage/references/api-scan.md`
   - 优先运行 `python3 .claude/skills/test-coverage/scripts/scan_apis.py --json` 扫描接口；若该路径不存在或执行失败则按规则手工扫描
5. 运行 `python3 .claude/skills/test-coverage/scripts/diff_map.py --json` 获取变更映射并写入测试范围表；失败则退回 `git diff --name-only`。
6. 让用户提供核心逻辑模块、关键路径（接口清单可由扫描补齐）。
7. 生成测试范围映射表与用例清单，覆盖：本次改动 + E2E + 核心逻辑 + 每个接口。
8. 给出放行结论（PASS/BLOCK）与阻断理由。
9. 结果追加到 `docs/test-plan.md`，使用时间戳标题，例如：

```
## 2026-01-18 测试计划
```
