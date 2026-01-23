# Commands（斜杠命令契约）

命令目录：`.opencode/commands/`

## 首次初始化

### `/keep-off <project-dir>`

用途：只在第一次执行，创建新项目目录并完成初始化。

输入：
- `project-dir`：新项目目录（必须不存在）

行为：
1) 创建 `$1/` 并进入
2) 写入初始化标记：`$1/.opencode/state/initialized.json`
3) 调用 skill：`env-init`

产物（至少）：
- `frontend/`
- `backend/`
- `docs/architecture.md`

可选路径（推荐）：模板启动（见 `env-init`）。

### `/keepoff <project-dir>`

用途：`/keep-off` 的别名。

## 启动/恢复

### `/启动规则`

用途：把治理协议落盘为权威文档，并提示强制门禁。

输出：
- `docs/workflow/40-gates.md`（或更新）

### `/继续`

用途：恢复协议（固定读取顺序），输出 Resume Snapshot。

## 检索

### `/最大化检索 <query>`

用途：默认并行（代码侦察 + 资料检索 + MCP augment）。

输出：
- Evidence（路径/URL + 摘要）
- Conclusions（可执行结论）
- Unknowns（阻塞点）

## 改动生命周期（强制门禁）

### `/改动开始 <一句话目标>`

用途：定义成功标准（Functional/Observable/PassFail），并声明门禁要求。

### `/审计`

用途：生成审计式检查清单，写入 `docs/review.md`，给 PASS/BLOCK。

### `/测试计划`

用途：生成测试计划，写入 `docs/test-plan.md`，给 PASS/BLOCK。

### `/执行测试`

用途：执行测试/构建并把证据写入 `progress.md`。

### `/问题复盘`

用途：将问题与解决方案固化到 `docs/problem.md`（写前先检索复用）。
