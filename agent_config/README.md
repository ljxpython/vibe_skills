# agent_config

This folder is a *shareable*, *sanitized* configuration bundle for multiple agent runtimes.

Goals:
- Keep configs as close to runnable as possible.
- Remove all secrets (API keys, bearer tokens, private endpoints with embedded creds).
- Prefer environment variables for secrets.

## What is included

Current structure:

- user/
  - codex/
    - config.toml
    - AGENTS.md
    - mcp-stdio-preload.cjs
    - prompts/
  - opencode/
    - opencode.json
    - oh-my-opencode.json
    - superpowers/hooks/hooks.json
  - claude/
    - mcp_servers.json

Notes:
- This bundle intentionally does NOT include project-specific files.
- This repo previously had agent_config/project; it has been removed per request.

## Safety / redaction policy

This folder must never contain:
- OpenAI-style keys: sk-...
- Anthropic-style keys: sk-ant-... / sk_ant...
- GitHub tokens: ghp_...
- AWS access keys: AKIA...
- Any bearer token / session token / password.

Placeholders you must replace locally:
- YOUR_CODEX_PROXY_API_KEY
- YOUR_ZHIPUAI_API_KEY

Environment variables you must set locally (recommended):
- XYZ_API_KEY
- CRS_API_KEY

## Setup: Codex

Files:
- user/codex/config.toml

This `config.toml` is "minimal runnable" and uses env vars for secrets.

1) Export required env vars:

```bash
export XYZ_API_KEY="..."
# optional
export CRS_API_KEY="..."
```

2) Use the config:
- If your Codex reads `~/.codex/config.toml`, copy the contents of `user/codex/config.toml` into your local `~/.codex/config.toml`.
- Keep your real tokens ONLY in env vars (never in the file).

## Setup: OpenCode

Files:
- user/opencode/opencode.json
- user/opencode/oh-my-opencode.json

OpenCode config contains placeholder API keys.

1) Edit `user/opencode/opencode.json` and replace:
- `YOUR_CODEX_PROXY_API_KEY`
- `YOUR_ZHIPUAI_API_KEY`

2) Place the files where OpenCode expects them:
- Typical location is `~/.config/opencode/`.

## Setup: Claude Code (MCP servers)

Files:
- user/claude/mcp_servers.json

This is a sanitized `mcpServers` definition.

1) Place it where Claude Code expects it (commonly `~/.config/claude/mcp_servers.json`).
2) Review paths inside the file:
- Some MCP servers point to local directories (e.g. repositories).
- Adjust paths to match your machine.

## Quick verification (no secrets)

Run these checks before sharing `agent_config/`:

- Search for common secret prefixes:
  - sk-
  - sk-ant-
  - sk_ant
  - ghp_
  - AKIA
- Search for suspicious fields:
  - apiKey
  - token
  - secret
  - password

If anything looks like a real credential, replace it with a placeholder or env var.
