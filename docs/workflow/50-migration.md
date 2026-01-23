# 迁移与约束（opencode-only）

## 目标态

- `.opencode/` 是唯一权威入口
- 不依赖任何插件（例如 superpowers / oh-my-opencode）
- 不依赖插件根变量（例如 `CLAUDE_PLUGIN_ROOT`）

## 已归档的历史内容

`deprecated/` 下包含：
- 旧多宿主配置（agent_config）
- 旧 Claude 目录结构与历史规则

## 迁移检查清单

1) 目录
- [ ] 根目录不存在 `.claude/`
- [ ] 根目录不存在 `agent_config/`

2) 配置
- [ ] `.opencode/opencode.json` 中不存在 `plugin` 配置

3) 脚本与 hooks
- [ ] `.opencode/skills/**` 中 hooks 命令使用项目内相对路径
