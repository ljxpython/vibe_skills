# 接口自动扫描规则

## 目标

自动补齐接口清单，覆盖所有 API 用于测试计划。

## 扫描优先级

1. OpenAPI/Swagger
2. FastAPI 路由定义
3. 文档与注释中暴露的接口
4. 代码搜索中出现的路由字符串

## 扫描策略

### 1) 前端请求（React/Vue）

- 搜索 `fetch(`、`axios.`、`request(`、`useRequest(`
- 提取 URL、方法、请求体与响应字段
- 关注 `baseURL` 与环境变量拼接

### 2) OpenAPI

- 优先读取 `/openapi.json` 或 `/openapi.yaml`
- 如果项目生成 OpenAPI：优先从生成文件读取

### 3) FastAPI 路由

- 扫描 `APIRouter` 与装饰器：`@router.get|post|put|delete|patch`
- 扫描 `app.get|post|put|delete|patch`
- 提取路径、方法、请求体、响应模型

### 4) 文档

- 读取 `docs/` 中 API 文档（如 `api.md`）
- 读取 README 的接口说明

### 5) 代码搜索

- 搜索 `"/api/"`、`"/v1/"`、`"/v2/"` 等路径常量
- 搜索 `router.` 与 `app.` 的声明

## 输出要求

- 输出接口清单（方法 + 路径 + 说明）
- 若信息缺失，标记 Unknown 并列出补充问题
