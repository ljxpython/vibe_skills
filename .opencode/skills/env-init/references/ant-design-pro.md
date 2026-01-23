# Ant Design Pro 初始化

## 强制规范

- 必须使用官方 pro-cli 命令初始化
- 必须选择 `umi@4` + `simple`
- 必须使用 yarn 安装依赖

## 标准流程（必须执行）

1. 安装 pro-cli：
   - `npm i @ant-design/pro-cli -g`
2. 创建项目：
   - `pro create myapp`
3. 选择 Umi 版本：
   - `umi@4`
4. 选择脚手架类型：
   - `simple`
5. 安装依赖：
   - `cd myapp && yarn`
6. 启动验证：
   - `yarn start`
   - 成功标准：终端无报错，页面正常启动

## 必须对用户汇报

- 是否成功执行初始化与依赖安装
- 若失败，返回错误信息并建议下一步

## 参考来源

- https://pro.ant.design/zh-CN/docs/getting-started/
