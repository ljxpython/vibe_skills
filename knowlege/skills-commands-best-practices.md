# Skills 与 Commands 最佳实践

本文总结 OpenCode/OpenSkills/Claude 兼容技能与命令的设计原则与落地规范，面向“可复用、可维护、可触发”的知识资产建设。

## 目标与适用边界

- 目标：把隐性经验沉淀为可复用的 Skill/Command，并保证触发准确、输出一致、维护成本低。
- 适用：跨项目复用、稳定且可迁移的知识或流程。
- 不适用：一次性任务、强项目定制且频繁变化的流程（优先放到 `CLAUDE.md` 或项目内规则）。

## Skills 设计原则

### 1. description 是路由器（最关键）

- 描述必须包含：
  - 能力（做什么）
  - 触发场景（何时用）
  - 边界（不用于什么）
- 描述太宽会误触发，太窄则无法触发。

推荐模板：

```
---
name: xxx
description: |
  [一句话核心能力]
  提供：[包含的资源]
  适用：[触发场景1]、[触发场景2]
  不适用：[边界场景1]、[边界场景2]
---
```

### 2. 渐进式披露（主文件精简）

- 第一层：`name + description`，用于匹配与加载。
- 第二层：`SKILL.md` 主流程与关键规则（建议 300~500 词）。
- 第三层：`references/` 详细文档（表结构、长列表、案例）。

原则：不要重复信息，细节放 `references/`，主流程保持精简。

### 3. 元数据与命名规范

- `name` 用小写 + `-` 连接；避免大写、下划线、连续 `--`。
- 建议 `name` 与目录名一致。
- 必须包含 `name`、`description`。

### 4. 设计一个默认路径

- 给出“默认做法”，减少决策熵。
- 对边界情况再提供分支或兜底方案。

### 5. 工作流可验证

- 用清晰流程步骤与校验点。
- 复杂流程用检查清单（Plan → Validate → Execute）。

### 6. 确定性逻辑用脚本

- 例如解析文件、批处理、转换等。
- 在 `SKILL.md` 明确“运行脚本”，而不是把大段数据塞进上下文。

### 7. 权限与安全

- Claude 兼容：使用 `allowed-tools` 约束能力。
- OpenCode：用 `permission.skill` 控制可见性。
- 在 `scripts/` 中尽量保持最小依赖。

## Commands 设计原则（斜杠命令）

### 1. 命令 = 可复用提示模板

- Markdown 文件形式优先（便于多行与格式化）。
- 文件名即命令名，支持嵌套目录。

### 2. 参数与变量

- `$ARGUMENTS`：注入全部参数。
- `$1`、`$2`：位置参数。

### 3. Shell 输出谨慎注入

- 使用 ``!`command` `` 将命令输出嵌入提示词。
- 保持输出短小、确定，避免过大输出污染上下文。

### 4. 文件引用优先于复制

- `@path/to/file` 引用文件内容。
- 减少提示词长度与手工错误。

### 5. 指定 agent / model / subtask

- `agent`：指定执行代理。
- `model`：指定模型。
- `subtask`：在子任务中运行，避免污染主上下文。

## 目录与放置规范（本仓库约定）

- Skills 目录：`.claude/skills/<skill-name>/SKILL.md`
- Commands 目录：`.claude/commands/`（当前为空，可新增）
- 参考与模板：`references/`、`templates/`、`scripts/`

## 测试与验证建议

### Skills

- 触发测试：3 个正向请求能触发。
- 负向测试：3 个无关请求不触发。
- 输出一致性：相同输入 3 次核心内容一致。
- 引用完整性：`references/` 路径存在。

### Commands

- 参数替换正确。
- `@file` 引用路径存在。
- Shell 输出不超长，且在项目根目录执行。

## 常见坑

- description 太模糊 → 不触发或乱触发。
- SKILL.md 太长 → 上下文浪费。
- references 乱引用 → 路径错误导致加载失败。
- 命令文件放错目录 → `/command` 不显示。

## 本仓库可参考的实现

- `planning-with-files`：完整模板、脚本、示例与参考。
- `ui-ux-pro-max`：大规模数据集 + 搜索脚本 + 操作手册。

## 参考资料

- OpenCode Skill 基础：https://learnopencode.com/5-advanced/03a-skills-basics.html
- OpenCode Skill 进阶：https://learnopencode.com/5-advanced/03b-skills-advanced.html
- OpenCode Commands：https://learnopencode.com/5-advanced/04-commands.html
- OpenCode 官方 Skills：https://opencode.ai/docs/skills
- OpenCode 官方 Commands：https://opencode.ai/docs/commands
- Claude Skills 文档：https://code.claude.com/docs/en/skills
- Claude Skills 最佳实践：https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- Agent Skills 规范：https://agentskills.io/specification
- OpenSkills README：https://raw.githubusercontent.com/numman-ali/openskills/main/README.md
