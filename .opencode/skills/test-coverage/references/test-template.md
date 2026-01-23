# 测试计划模板（Python + React/Vue）

## 测试覆盖范围（必须包含）

1. 本次改动覆盖（基于 git diff 识别）
2. 端到端（E2E）关键路径
3. 核心逻辑单元测试
4. 每个接口测试（状态码 + 正反路径）

## 输出结构

- 变更范围映射（基于 git diff 的文件与模块）
- 测试范围映射表（功能/接口/页面 -> 测试类型）
- 用例列表（输入 -> 预期 -> 校验方式）
- 执行命令
- 失败记录与重试策略
- 放行结论（PASS/BLOCK）与阻断理由

## 变更范围自动识别

- 使用 `git diff --name-only` 获取本次改动文件
- 将改动文件映射到：接口 / 核心逻辑 / UI / 配置
- 映射结果必须写入测试范围表

## Python 建议工具

- 单元/接口：pytest + httpx/TestClient
- 覆盖率：pytest-cov

## 前端建议工具

- React/Vue 单元：vitest/jest
- E2E：Playwright
