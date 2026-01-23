# 套装模板：Ant Design Pro + FastAPI（固化手册）

本文档是对 `antpro-fastapi-starter` 项目 `docs/setup.md` 的固化镜像（复制并内置到本仓库的 skill 中），用于避免外部文档被删除或漂移后导致流程断裂。

- 同步时间：2026-01-19
- 适用目标：快速得到“可运行的真链路”前后端分离样板（前端 /api 代理后端，禁止 mock）。

---

# 前后端分离项目搭建手册（可复刻）

本文档记录本次项目从 0 到可运行的完整过程。严格按步骤执行即可复刻。

## 1. 项目简介

**项目类型**：前后端分离、最小可运行样板

**目标**：
- 前端：Ant Design Pro（Umi 4 + TS）
- 后端：FastAPI + SQLite（stdlib sqlite3）
- 真链路：前端通过 `/api` 代理后端
- 禁止 mock 数据

**运行结果**：
- 后端提供 `/api/health`、`/api/items`（GET/POST）
- 前端提供 `/items` 页面，可真实读取/新增数据库数据

## 2. 技术栈与版本

- 前端：Ant Design Pro（Umi 4）
- 后端：FastAPI + Uvicorn
- 数据库：SQLite（文件 `backend/app/data/app.db`）
- Node：>= 20（本机示例为 v25.1.0）
- 包管理：Yarn 3、uv
- Python：3.13

## 3. 目录结构

```
plant_workflow/
├── frontend/                         # 前端（Umi 4）
├── backend/                          # 后端（FastAPI + SQLite）
├── docs/
│   └── setup.md                      # 本文档
├── Makefile                          # 启动/停止/日志命令
└── CLAUDE.md                         # 架构说明
```

## 4. 环境检查

```
node -v
npm -v
yarn -v
uv --version
```

## 5. 前端搭建（Ant Design Pro）

### 5.1 安装脚手架

```
npm i @ant-design/pro-cli -g
```

### 5.2 创建前端工程（非交互）

```
pro create "frontend" --template simple
```

> 说明：脚手架默认使用 gitee 拉取模板。

### 5.3 Yarn 安装（关键修复：关闭 PnP）

Umi 在 Yarn PnP 模式下会报 `ERR_VM_MODULE_LINK_FAILURE`，必须改为 `node-modules`。

```
cd "frontend"
yarn config set nodeLinker node-modules
yarn
```

### 5.4 关闭 mock

编辑 `frontend/config/config.ts`：

```ts
// 原 mock 配置
// mock: { include: ['mock/**/*', 'src/pages/**/_mock.ts'] },
// 替换为：
mock: false,
```

并删除 mock 目录：

```
rm -rf "frontend/mock"
```

### 5.5 配置本地代理

编辑 `frontend/config/proxy.ts`：

```ts
export default {
  dev: {
    '/api/': {
      target: 'http://127.0.0.1:8001',
      changeOrigin: true,
    },
  },
};
```

### 5.6 添加真实 Items 页面

新增 `frontend/src/services/items.ts`：

```ts
import { request } from '@umijs/max';

export interface Item {
  id: number;
  name: string;
  created_at: string;
}

export interface ItemCreatePayload {
  name: string;
}

export async function fetchItems(options?: Record<string, any>) {
  return request<Item[]>('/api/items', {
    method: 'GET',
    ...(options || {}),
  });
}

export async function createItem(data: ItemCreatePayload, options?: Record<string, any>) {
  return request<Item>('/api/items', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    data,
    ...(options || {}),
  });
}
```

新增页面 `frontend/src/pages/items/index.tsx`：

```tsx
import { PageContainer } from '@ant-design/pro-components';
import { Button, Card, Input, List, Space, Typography, message } from 'antd';
import { useCallback, useEffect, useState } from 'react';

import { createItem, fetchItems } from '@/services/items';
import type { Item } from '@/services/items';

const ItemsPage = () => {
  const [items, setItems] = useState<Item[]>([]);
  const [loading, setLoading] = useState(false);
  const [submitting, setSubmitting] = useState(false);
  const [name, setName] = useState('');

  const loadItems = useCallback(async () => {
    setLoading(true);
    try {
      const data = await fetchItems();
      setItems(data || []);
    } catch (error) {
      message.error('加载失败');
    } finally {
      setLoading(false);
    }
  }, []);

  const handleCreate = async () => {
    const trimmed = name.trim();
    if (!trimmed) {
      message.warning('请输入名称');
      return;
    }
    setSubmitting(true);
    try {
      await createItem({ name: trimmed });
      setName('');
      message.success('创建成功');
      await loadItems();
    } catch (error) {
      message.error('提交失败');
    } finally {
      setSubmitting(false);
    }
  };

  useEffect(() => {
    loadItems();
  }, [loadItems]);

  return (
    <PageContainer>
      <Card style={{ marginBottom: 16 }}>
        <Space.Compact style={{ width: '100%' }}>
          <Input
            value={name}
            placeholder="请输入名称"
            maxLength={200}
            onChange={(event) => setName(event.target.value)}
          />
          <Button type="primary" loading={submitting} onClick={handleCreate}>
            添加
          </Button>
        </Space.Compact>
      </Card>
      <Card>
        <List
          loading={loading}
          dataSource={items}
          locale={{ emptyText: '暂无数据' }}
          renderItem={(item) => (
            <List.Item>
              <Space direction="vertical" size={0}>
                <Typography.Text strong>{item.name}</Typography.Text>
                <Typography.Text type="secondary">ID: {item.id}</Typography.Text>
                <Typography.Text type="secondary">{item.created_at}</Typography.Text>
              </Space>
            </List.Item>
          )}
        />
      </Card>
    </PageContainer>
  );
};

export default ItemsPage;
```

修改路由 `frontend/config/routes.ts`：

```ts
{
  path: '/items',
  name: 'items',
  icon: 'table',
  component: './items',
},
{
  path: '/',
  redirect: '/items',
},
```

### 5.7 修复空白页（必须做）

编辑 `frontend/src/app.tsx`，去掉登录态强制跳转与外部 baseURL：

- 删除 `currentUser` 登录请求与 `onPageChange` 重定向逻辑
- 删除 request 的外部 `baseURL`

最终 `request` 保持：

```ts
export const request: RequestConfig = {
  ...errorConfig,
};
```

### 5.8 关闭 mako（修复资源 404）

编辑 `frontend/config/config.ts`：

```ts
mako: false,
```

## 6. 后端搭建（FastAPI + SQLite）

### 6.1 初始化后端工程

```
mkdir -p "backend"
cd "backend"
uv init
uv python install 3.13
uv add fastapi uvicorn
```

### 6.2 创建后端代码

`backend/app/db.py`：

```py
from __future__ import annotations

from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "app.db"


def get_connection() -> sqlite3.Connection:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    conn = get_connection()
    try:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )
        conn.commit()
    finally:
        conn.close()
```

`backend/app/schemas.py`：

```py
from pydantic import BaseModel, Field


class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)


class Item(BaseModel):
    id: int
    name: str
    created_at: str
```

`backend/app/routers/items.py`：

```py
from __future__ import annotations

from datetime import datetime, timezone
from fastapi import APIRouter

from ..db import get_connection
from ..schemas import Item, ItemCreate

router = APIRouter(prefix="/api", tags=["items"])


def _row_to_item(row) -> Item:
    return Item(id=row["id"], name=row["name"], created_at=row["created_at"])


@router.get("/items", response_model=list[Item])
def list_items() -> list[Item]:
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT id, name, created_at FROM items ORDER BY id DESC"
        ).fetchall()
    return [_row_to_item(row) for row in rows]


@router.post("/items", response_model=Item, status_code=201)
def create_item(payload: ItemCreate) -> Item:
    created_at = datetime.now(timezone.utc).isoformat()
    with get_connection() as conn:
        cursor = conn.execute(
            "INSERT INTO items (name, created_at) VALUES (?, ?)",
            (payload.name, created_at),
        )
        conn.commit()
        row = conn.execute(
            "SELECT id, name, created_at FROM items WHERE id = ?",
            (cursor.lastrowid,),
        ).fetchone()
    return _row_to_item(row)
```

`backend/app/main.py`：

```py
from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse, RedirectResponse

from .db import get_connection, init_db
from .routers.items import router as items_router

app = FastAPI()


@app.on_event("startup")
def on_startup() -> None:
    init_db()


@app.get("/api/health")
def health() -> dict:
    try:
        with get_connection() as conn:
            conn.execute("SELECT 1")
        return {"status": "ok"}
    except Exception as exc:
        raise HTTPException(status_code=500, detail="db error") from exc


@app.get("/", include_in_schema=False)
def root() -> RedirectResponse:
    return RedirectResponse(url="http://localhost:8000/items")


@app.get("/favicon.ico", include_in_schema=False)
def favicon() -> PlainTextResponse:
    return PlainTextResponse("", status_code=204)


app.include_router(items_router)
```

## 7. 启动与验证

### 7.1 启动后端

```
cd "backend"
uv run uvicorn app.main:app --port 8001 --reload
```

### 7.2 启动前端

```
cd "frontend"
yarn start
```

### 7.3 访问页面

```
http://localhost:8000/items
```

### 7.4 接口验证

```
curl "http://127.0.0.1:8001/api/health"
curl "http://127.0.0.1:8001/api/items"
```

## 8. Makefile（一键启动/停止/日志）

项目根目录提供 Makefile：

- `make help`：查看帮助
- `make start` / `make stop` / `make restart`
- `make start-frontend` / `make stop-frontend`
- `make start-backend` / `make stop-backend`
- `make logs`：最近 200 行日志
- `make logs-follow`：持续跟随日志

Makefile 使用 `lsof -i` 查端口并杀进程，不使用 PID 文件。

## 9. 踩坑记录（必须避开）

1) **Yarn PnP 导致 Umi 配置解析失败**
- 现象：`ERR_VM_MODULE_LINK_FAILURE`
- 解决：`yarn config set nodeLinker node-modules`

2) **前端空白页（强制登录 + 外部 baseURL）**
- 现象：页面空白 / 一直跳转登录
- 解决：移除登录态强制跳转、移除 request 的外部 baseURL

3) **静态资源 404（mako dev server）**
- 现象：`umi.js` / `umi.css` 返回 HTML，浏览器报 `Unexpected token '<'`
- 解决：`mako: false`，使用 webpack dev server

4) **访问错误端口**
- 现象：访问 `http://127.0.0.1:8001` 导致前端资源 404
- 解决：前端必须访问 `http://localhost:8000/items`

## 10. 架构说明

- 前端（Umi 4）只负责 UI 与请求封装
- 所有 API 统一走 `/api` 代理到后端
- 后端（FastAPI）只负责 API 和 SQLite 持久化
- 数据真实写入 `backend/app/data/app.db`

---

如需全量复刻，按本文档逐条执行即可。
