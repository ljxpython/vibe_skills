# vibe_skills

这是一个“全链路开发工作流资产库”（opencode-only）：把我自己的工作法固化成可复用的 **agents / commands / skills / docs**。

目标：任何项目都能用同一套入口命令完成：初始化 -> 检索 -> 改动 -> 审计门禁 -> 测试门禁 -> 复盘落盘。

## 这仓库是干嘛的

- 作为权威工作流来源（`.opencode/`）
- **/keep-off 只在首次初始化时使用**：创建一个新项目目录并注入 `.opencode/`
- 日常开发在“被初始化的项目目录”里进行（而不是在本仓库里写业务代码）

## 目录结构
```
.
├── .opencode/                # OpenCode 权威工作流（agents/commands/skills/config）
│   ├── agents/               # 子代理定义（并行/隔离）
│   ├── commands/             # 斜杠命令（入口协议）
│   ├── skills/               # Skills（渐进式披露）
│   └── opencode.json         # OpenCode 项目级权威配置（不含密钥）
├── docs/
│   └── workflow/             # 工作流权威文档（契约/门禁/迁移）
├── knowlege/                 # 额外沉淀（非权威）
├── AGENTS.md                 # 交互/风格/行为约束
├── CLAUDE.md                 # AI 助手指令说明
└── temp.txt                  # 原始规则素材
```

## 快速开始

1) 全局只配置个人机密与模型（不要把 token 写进仓库）

- 路径：`~/.config/opencode/opencode.json`
- 内容：仅 provider/apiKey/model/个人偏好（不放 commands/skills）

2) 在本仓库目录启动 OpenCode，然后执行首次初始化

```text
/keep-off <project-dir>
```

`/keep-off` 会创建一个新项目目录，并把本仓库的 `.opencode/` 注入到新项目中。

3) 进入新项目目录，启用治理协议

```text
/启动规则
```

## ��流程使用方式（opencode-only）

### 1. 首次初始化（只做一次）

- `/keep-off <project-dir>`：uv 初始化 + 前后端骨架 + `docs/architecture.md`（可选模板启动）
- `/启动规则`：启用强制门禁与默认并行检索

提示：随时可用 `/工作流帮助` 查看“可用命令/子代理/MCP/skills”与路由范例。

### 2. 持久化记忆（强制）

- 使用 `planning-with-files` 维护：`task_plan.md`、`findings.md`、`progress.md`
- 继续任务使用：`/继续`（固定读取顺序并输出 Resume Snapshot）

### 3. 记录与落盘

- 所有阶段性结论、门禁结论、失败与修复都要落盘（`docs/` + 记忆文件）
- 记忆文件：`project_context.md` / `task_plan.md` / `findings.md` / `progress.md`

### 4. 审计门禁（每次改动必做）

- `/审计` -> `docs/review.md`（PASS/BLOCK）

### 5. 测试门禁（每次改动必做）

- `/测试计划` -> `docs/test-plan.md`（PASS/BLOCK）
- `/执行测试` -> 把执行证据写入 `progress.md`

## 权威文档

- `docs/workflow/00-overview.md`
- `docs/workflow/20-commands.md`
- `docs/workflow/40-gates.md`

### 6. 问题复盘与复用

- 先查历史：`problem-finder`
- 新问题落盘：`/问题复盘`（写入 `docs/problem.md`）

## 约定（别搞花的）
- 面向人的文本（说明、约束、提示词内容）用中文；标识符（目录名/文件名/change-id 等）用简洁英文
- 文件/目录名优先用 kebab-case（例如 `add-x`, `prompt-guidelines`）
- 写命令示例时，路径统一用双引号包裹（避免空格/特殊字符踩坑）

## Skills 兼容性

本仓库的技能结构兼容 OpenSkills/Agent Skills 规范（`SKILL.md` + `references/` + `scripts/`），但本仓库的权威使用方式是 opencode-only：`.opencode/skills/`。

### 技能列表（核心）

```xml
<available_skills>
- env-init: 项目首次初始化（uv + 前后端骨架 + docs/architecture.md + 可选模板启动）
- kickoff-rules: 启动���则（强制门禁/默认并行/落盘/opencode-only 约束）
- resume-handshake: 继续任务恢复协议（固定读取顺序 + Resume Snapshot）
- planning-with-files: 文件化记忆（task_plan/findings/progress）
- code-audit: 审计门禁（Yes/No/Unknown + PASS/BLOCK）
- test-coverage: 测试计划门禁（本次改动+E2E+核心逻辑+每接口）
- problem-finder: 先查历史再排查（docs/problem.md 复用）
- ui-ux-pro-max: UI/UX 设计智能技能（数据集 + 搜索脚本）
</available_skills>
```

### 技能加载方式

1. **命令调用（推荐）**：使用 `/keep-off`、`/审计`、`/测试计划` 等命令驱动整个流程
2. **直接引用**：在对话中手动引用 skill 名称

### 技能存储位置

- **主要位置**：`.opencode/skills/<skill-name>/`
- **模板和脚本**：存放在技能目录下的 `templates/`, `scripts/`, `references/` 子目录
- **工作文件**：技能执行时创建的持久文件（如 task_plan.md）存放在用户的项目目录

### 复用到其他项目

最稳定的方式：在目标项目根目录放入本仓库的 `.opencode/`。

### 兼容性说明

本仓库的技能完全兼容 OpenSkills 标准：
- ✅ SKILL.md 格式：YAML frontmatter + Markdown 内容
- ✅ 目录结构：符合 OpenSkills 技能规范
- ✅ 工具权限：使用 `allowed-tools` 声明
- ✅ Hooks 配置：支持 SessionStart, PreToolUse, PostToolUse, Stop 等生命周期钩子

### 参考文档

- [OpenSkills GitHub 仓库](https://github.com/numman-ali/openskills)
- [OpenSkills 文档](https://github.com/anthropics/skills)

---

## 核心技能说明（简要）

### planning-with-files
基于文件的复杂任务规划技能，用于管理多步骤、多阶段的项目。

**特点**:
- 创建持久工作文件：`task_plan.md`, `findings.md`, `progress.md`
- 2-Action 规则：每 2 次查看/搜索操作后保存发现
- 3-Strike 错误协议：诊断 → 替代方案 → 广泛重思 → 升级到用户

**用法**: 自动触发复杂任务，或手动调用

### problem-finder
问题复盘与复用技能，用于遇到问题时优先查找 `docs/problem.md` 中的历史记录。

**特点**:
- 强制检索历史问题再继续排查
- 复用已有解决方案并标注差异

**用法**: 在“报错/失败/故障/回溯原因/类似问题”等场景自动触发

### code-audit
代码审查与可审计检查清单技能，用于架构评审/质量审查/合规核查。

**特点**:
- 生成可判定检查点（Yes/No/Unknown）
- 逐项逻辑验证与证据链
- 输出审计式结论并记录到 `docs/review.md`

**用法**: 在“代码审查/Review/合规审计”等场景自动触发

### test-coverage
测试计划与覆盖策略技能，用于生成本次+E2E+核心逻辑+每接口的测试计划。

**特点**:
- 覆盖本次改动 + 端到端 + 核心逻辑 + 每个接口
- 输出可执行测试计划并记录到 `docs/test-plan.md`

**用法**: 在“测试/验证/覆盖率/端到端”等场景自动触发

### env-init / kickoff-rules / resume-handshake

原先的“项目启动与方案讨论”已拆分成三块（更符合全链路工作流）：

- `env-init`：只负责首次初始化（uv + 前后端骨架 + 架构文档 + 可选模板启动）
- `kickoff-rules`：只负责启动后的治理协议（强制门禁/默认并行/落盘）
- `resume-handshake`：只负责继续任务（恢复协议）

### ui-ux-pro-max
UI/UX 设计智能技能，包含可搜索的设计指南数据库。

**包含内容**:
- 50 种 UI 样式
- 21 种配色方案
- 50 种字体配对
- 20 种图表类型
- 支持 9 种技术栈：HTML/Tailwind, React, Next.js, Vue, Svelte, SwiftUI, React Native, Flutter, shadcn/ui

**用法**: 通过搜索查询快速查找设计指南



## opencode-only 说明

本仓库以 `.opencode/` 为唯一权威来源，不再维护 `.claude/`、`agent_config/` 等多宿主配置。



## 参鉴的仓库
- https://github.com/OthmanAdi/planning-with-files/tree/master

  

- https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

  - ```
    npm install -g uipro-cli
    
    # Go to your project
    cd /path/to/your/project
    
    # Install for your AI assistant
    uipro init --ai claude      # Claude Code
    uipro init --ai cursor      # Cursor
    uipro init --ai windsurf    # Windsurf
    uipro init --ai antigravity # Antigravity (.agent + .shared)
    uipro init --ai copilot     # GitHub Copilot
    uipro init --ai kiro        # Kiro
    uipro init --ai codex       # Codex CLI
    uipro init --ai qoder       # Qoder
    uipro init --ai roocode     # Roo Code
    uipro init --ai gemini      # Gemini CLI
    uipro init --ai trae        # Trae
    uipro init --ai all         # All assistants
    ```

    

## 说明：已移除 superpowers / 插件依赖

本仓库的目标是“极致 opencode-only”，不依赖 superpowers、oh-my-opencode 等插件。

历史材料已归档到 `deprecated/`。
