# 推荐使用mcp



## aug mcp
https://docs.augmentcode.com/context-services/mcp/quickstart-claude-code
```shell

npm install -g @augmentcode/auggie@prerelease

# 这个是在页面进行登录
auggie login

# 这个是输出token
auggie token print  

```
augument 登录后，如下配置吧：
```shell

# claude 配置
claude mcp add-json auggie-mcp --scope user '{"type":"stdio","command":"auggie","args":["--mcp"]}'


# 其他配置
{
  "mcpServers": {
    "augment-context-engine": {
      "command": "auggie",
      "args": [
        "--mcp"
      ]
    }
  }
}

```

