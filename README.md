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
│   └── skills/                # 可复用技能
│       ├── planning-with-files/   # 基于文件的复杂任务规划
│       └── ui-ux-pro-max/      # UI/UX 设计智能技能
├── rules/                    # AI 代理规则版本
│   ├── AGENTS_v1.md
│   └── AGENTS_v2.md
├── AGENTS.md                 # 交互/风格/行为约束
└── CLAUDE.md                 # AI 助手指令说明
```

## 怎么用（最简单的方式）
1. 直接修改对应的 Markdown 文档（新增/修订你的 skill、command、prompt）
2. 修改完 **直接提交** 即可（无 CI/自动校验）

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
