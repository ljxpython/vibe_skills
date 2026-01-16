# vibe_skills

个人常用资料库：收集与沉淀我常用的 **skills**、**commands** 和 **system prompts**，方便复用与快速查找。

## 这仓库是干嘛的
- 把零散经验（怎么做、怎么写、怎么跑）整理成可复用的文档
- 让人和 AI 助手按同一套约定协作（少扯皮，少走弯路）
- **不是**业务服务仓库：目前不承诺存在可运行代码与运行时环境

## 目录结构（现状）
```
.
├── openspec/                 # OpenSpec 规范与变更提案目录
│   ├── project.md             # 项目约定（AI/人都以此为准）
│   ├── AGENTS.md              # OpenSpec 工作流说明
│   ├── changes/               # 变更提案（what SHOULD change）
│   └── specs/                 # 能力规范（what IS / should exist as convention）
├── .spec-workflow/            # 需求/设计/任务等模板
├── .opencode/                 # 命令说明（如 openspec-*）
├── AGENTS.md                  # 交互/风格/行为约束
└── CLAUDE.md                  # 受管 OpenSpec 指令块
```

## 怎么用（最简单的方式）
1. 直接修改对应的 Markdown 文档（新增/修订你的 skill、command、prompt）
2. 修改完 **直接提交** 即可（当前不强制 CI/自动校验）

## 约定（别搞花的）
- 面向人的文本（说明、约束、提示词内容）用中文；标识符（目录名/文件名/change-id 等）用简洁英文
- 文件/目录名优先用 kebab-case（例如 `add-x`, `prompt-guidelines`）
- 写命令示例时，路径统一用双引号包裹（避免空格/特殊字符踩坑）

## （可选）用 OpenSpec 管理“较大变更”
如果你要做的是“新增一类内容/引入新结构/改大约定”，建议走 OpenSpec 变更提案：
- 在 `openspec/changes/<change-id>/` 写 `proposal.md` + `tasks.md`（必要时加 `design.md`）
- 关联变更的 capability spec 放到 `openspec/changes/<change-id>/specs/<capability>/spec.md`

> 不想搞这套也行：小改动就直接改文档提交，保持变更小而清晰就够了。

## 借鉴的仓库
- https://github.com/OthmanAdi/planning-with-files/tree/master
- https://github.com/Fission-AI/OpenSpec
- https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
