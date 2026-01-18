# vibe_skills

个人常用资料库：收集与沉淀我常用的 **skills**、**commands** 和 **system prompts**，方便复用与快速查找。

## 这仓库是干嘛的
- 把零散经验（怎么做、怎么写、怎么跑）整理成可复用的文档
- 让人和 AI 助手按同一套约定协作（少扯皮，少走弯路）
- **不是**业务服务仓库：目前不承诺存在可运行代码与运行时环境

## 目录结构（现状）
```
.
├── .claude/                  # Claude AI 技能和命令
│   ├── commands/             # 自定义斜杠命令
│   └── skills/               # 可复用技能
│       ├── planning-with-files/   # 基于文件的复杂任务规划
│       ├── project-kickoff/   # 项目启动与方案讨论
│       └── ui-ux-pro-max/      # UI/UX 设计智能技能
├── knowlege/                 # 知识沉淀（skills/commands 总结）
│   └── skills-commands-best-practices.md
├── docs/                     # 项目文档与问题复盘
│   └── problem.md
├── rules/                    # AI 代理规则版本
│   ├── AGENTS_v1.md
│   └── AGENTS_v2.md
├── AGENTS.md                 # 交互/风格/行为约束
├── CLAUDE.md                 # AI 助手指令说明
└── temp.txt                  # 原始规则素材
```

## 怎么用（最简单的方式）
1. 直接修改对应的 Markdown 文档（新增/修订你的 skill、command、prompt）
2. 修改完 **直接提交** 即可（无 CI/自动校验）

## 全流程使用方式（vibe coding）

### 1. 初始化与前置对齐
- 触发 `project-kickoff`：明确目标/约束/技术栈/协作分工
- 确认所需资源与配合事项后再行动

### 2. 持久化记忆（强制）
- 使用 `planning-with-files` 创建：`task_plan.md`、`findings.md`、`progress.md`
- 新窗口恢复顺序：`task_plan.md` → `findings.md` → `progress.md`

### 3. ToDo 与进度
- 所有阶段性产出与问题都记录到 `/docs`
- 推荐文档：`project-summary.md`、`problem.md`

### 4. 代码审查（门禁）
- 使用 `/review` 或触发 `code-audit`
- 输出审查结论与 PASS/BLOCK，记录到 `/docs/review.md`

### 5. 代码测试（门禁）
- 使用 `/test-plan` 或触发 `test-coverage`
- 覆盖：本次改动 + E2E + 核心逻辑 + 每个接口
- 输出测试计划与 PASS/BLOCK，记录到 `/docs/test-plan.md`

### 6. 问题复盘与复用
- 遇到问题触发 `problem-finder`
- 解决后使用 `/problem-summary` 追加到 `/docs/problem.md`

## 约定（别搞花的）
- 面向人的文本（说明、约束、提示词内容）用中文；标识符（目录名/文件名/change-id 等）用简洁英文
- 文件/目录名优先用 kebab-case（例如 `add-x`, `prompt-guidelines`）
- 写命令示例时，路径统一用双引号包裹（避免空格/特殊字符踩坑）

## OpenSkills 集成

本仓库现已支持 **OpenSkills** 技能管理系统，技能可以被其他 AI 代理（Claude Code, Cursor, Windsurf, Aider, Codex 等）识别和加载。

### 技能列表

```xml
<available_skills>
- planning-with-files: 基于文件的复杂任务规划技能。创建 task_plan.md, findings.md, progress.md 用于多阶段、多步骤的项目管理
- problem-finder: 问题复盘与复用指引。遇到问题时优先检索 /docs/problem.md 并复用历史方案
- project-kickoff: 项目启动与方案讨论流程。适用于项目开始/初始化/立项/方案讨论/技术选型/需求澄清等场景
- code-audit: 代码审查与可审计检查清单生成。适用于代码审查/Review/质量检查/合规审计
- test-coverage: 测试计划与覆盖策略生成。适用于测试/验证/覆盖率/端到端/接口测试/核心逻辑测试
- ui-ux-pro-max: UI/UX 设计智能技能。包含可搜索的 50 种样式、21 种配色、50 种字体配对、20 种图表类型，支持 9 种技术栈
</available_skills>
```

### 技能加载方式

1. **直接引用**：在对话中手动引用技能名称
2. **命令调用**：使用 `/planning-with-files` 或 `/ui-ux-pro-max` 命令
3. **OpenSkills CLI**：`npx openskills read planning-with-files`

### 技能存储位置

- **主要位置**：`.claude/skills/<skill-name>/`
- **模板和脚本**：存放在技能目录下的 `templates/`, `scripts/`, `references/` 子目录
- **工作文件**：技能执行时创建的持久文件（如 task_plan.md）存放在用户的项目目录

### 安装技能到其他项目

其他项目可以通过以下方式安装本仓库的技能：

```bash
# 从 GitHub 安装
npx openskills install git@github.com:yourusername/vibe_skills.git

# 本地安装
npx openskills install /path/to/vibe_skills
```

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

## 核心技能说明

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
- 输出审计式结论并记录到 `/docs/review.md`

**用法**: 在“代码审查/Review/合规审计”等场景自动触发

### test-coverage
测试计划与覆盖策略技能，用于生成本次+E2E+核心逻辑+每接口的测试计划。

**特点**:
- 覆盖本次改动 + 端到端 + 核心逻辑 + 每个接口
- 输出可执行测试计划并记录到 `/docs/test-plan.md`

**用法**: 在“测试/验证/覆盖率/端到端”等场景自动触发

### project-kickoff
项目启动与方案讨论技能，用于项目开始时的前置对齐与方案评估。

**特点**:
- 前置条件对齐与用户协作分工
- 证据优先与资料先行
- 三段论开发法（正/反/合）
- 强制复用成熟依赖，禁止降级链路

**用法**: 在“项目开始/初始化/立项/方案讨论/技术选型/需求澄清”等场景自动触发

### ui-ux-pro-max
UI/UX 设计智能技能，包含可搜索的设计指南数据库。

**包含内容**:
- 50 种 UI 样式
- 21 种配色方案
- 50 种字体配对
- 20 种图表类型
- 支持 9 种技术栈：HTML/Tailwind, React, Next.js, Vue, Svelte, SwiftUI, React Native, Flutter, shadcn/ui

**用法**: 通过搜索查询快速查找设计指南

## 参鉴的仓库
- https://github.com/OthmanAdi/planning-with-files/tree/master
- https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
