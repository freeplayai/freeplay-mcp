# Freeplay MCP Server

An MCP (Model Context Protocol) server that enables AI agents to interact with the Freeplay platform. Agents can browse projects, test prompts, run completions, and analyze prompt performance—all through natural language.

## ⚠️ EXPERIMENTAL

**This MCP server is experimental and will change.** Use at your own risk.

Current limitations:
- Does not support destructive deletion actions
- Does not support deployment operations
- Uses your regular Freeplay API key (not scoped to limit access)

**Security warning:** Because this uses your full API key, a malicious or compromised agent could extract the key and write its own code outside the MCP to perform destructive actions against your Freeplay account.

Additionally, all MCP servers share a security context within the host, enabling data exfiltration, prompt injection across tools, and cross-server data access.

Only use this with agents and MCP servers you fully trust.

---

## Installation

### Claude Code

1. Clone this repository locally.
   ```shell
   git clone git@github.com:freeplayai/freeplay-mcp.git
   ```
1.
   ```shell
   cd freeplay-mcp
   uv sync # install dependencies
   ```
1. Add the Freeplay MCP server to your claude code. From the freeplay-mcp directly.
    ```shell
   claude mcp add --transport stdio freeplay-mcp-v1 -- uv run main.py
    ```
1. Configure `.env` and:
   ```shell
   source .env 
   ```
1. Start Claude code and run `/mcp` to check installation.

## Authentication

- API key passed via environment variable `FREEPLAY_API_KEY`
- All requests use Bearer token authentication
- Base URL configurable via `FREEPLAY_BASE_URL` (default: `https://app.freeplay.ai`)

## Support

- **Docs**: https://docs.freeplay.ai
- **Issues**: https://github.com/freeplayai/freeplay-mcp/issues
- **Security**: security@freeplay.ai
