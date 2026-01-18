---
name: test-coverage
description: |
  测试计划与覆盖策略生成。适用于“测试/验证/覆盖率/端到端/接口测试/核心逻辑测试/回归”等场景。
  触发后必须覆盖本次改动 + E2E + 核心逻辑 + 每个接口测试，并输出可执行测试计划。
  不适用：无需测试的纯讨论。
---

# 测试计划与覆盖 Skill

## 强制流程

1. 读取 `references/test-template.md`
2. 读取 `references/api-scan.md`，优先使用脚本 `scripts/scan_apis.py` 补齐接口清单；脚本失败则回退到手工扫描规则
3. 运行 `scripts/diff_map.py --json` 获取变更映射并写入测试范围表；脚本失败则回退为 `git diff --name-only`
4. 要求用户提供核心逻辑模块、关键路径（接口清单可由扫描补齐）
5. 生成测试范围映射表与用例清单
6. 输出执行命令与验证方式
7. 给出放行结论（PASS/BLOCK）与阻断理由
8. 结果写入 `/docs/test-plan.md`

## 输出要求

- 必须覆盖：本次改动、端到端、核心逻辑、每个接口
- 每个测试项必须可执行与可验证
- 信息不足时标记 Unknown 并列出补充清单

## 产出

- `/docs/test-plan.md`（测试计划）
