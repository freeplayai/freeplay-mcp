# Freeplay MCP Server

An MCP (Model Context Protocol) server that enables AI agents to interact with [Freeplay](https://freeplay.ai), the ops
platform for AI engineering teams.

Use it to analyze production logs, identify quality issues, iterate on prompts and agents using real data, and run
experiments to validate changes before deploying.

## ⚠️ EXPERIMENTAL

**This MCP server is an *experimental release* and will change.** Use at your own risk and keep an eye on what your
agents are doing.

Current limitations:

- Does not support deployment operations or destructive deletion actions — use the Freeplay UI
- Uses your regular Freeplay API key (not specially scoped to limit access for agents)

**Security warning:** Because this uses your full API key, an agent could extract the key and formulate its own API
calls outside the scope of the tools included with this MCP server, including destructive actions against your Freeplay
account.

Additionally, all MCP servers share a security context within the host, enabling data exfiltration, prompt injection
across tools, and cross-server data access.

Only use this with agents and MCP servers you fully trust.

---

## Installation

### Claude Code

If using Claude Code, it is recommended to use the freeplay-plugin, which includes skills and this MCP 
server: https://github.com/freeplayai/freeplay-plugin.

The simplest way to install only the Freeplay MCP server is via `uvx`:

```shell
claude mcp add freeplay -- uvx freeplay-mcp
```

Set your API key in your MCP client process:

```shell
export FREEPLAY_API_KEY="your-api-key"
export FREEPLAY_BASE_URL="https://app.freeplay.ai"
```

Start Claude Code and run `/mcp` to check installation.

### Claude Desktop

Add to your Claude Desktop config (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):

```json
{
   "mcpServers": {
      "freeplay": {
         "command": "uvx",
         "args": [
            "freeplay-mcp"
         ],
         "env": {
            "FREEPLAY_API_KEY": "your-api-key",
            "FREEPLAY_BASE_URL": "https://app.freeplay.ai"
         }
      }
   }
}
```

### Docker

For containerized deployments:

1. Clone and build:
   ```shell
   git clone https://github.com/freeplayai/freeplay-mcp.git
   cd freeplay-mcp
   docker build -t freeplay-mcp .
   ```
2. Set your environment variables (in .env, then source it).
   ```shell
   export FREEPLAY_API_KEY="your-api-key"
   export FREEPLAY_BASE_URL="https://app.freeplay.ai"
   ```

3. Add to Claude Code:
   ```shell
   claude mcp add --transport stdio freeplay-mcp -- docker run -i --rm -e FREEPLAY_API_KEY=$FREEPLAY_API_KEY -e FREEPLAY_BASE_URL=$FREEPLAY_BASE_URL freeplay-mcp
   ```

For production deployments, consider using a hardened base image such as [Chainguard](https://www.chainguard.dev/)
or [Distroless](https://github.com/GoogleContainerTools/distroless).

4. Start Claude Code and run `/mcp` to check installation.

## Authentication

- API key passed via environment variable `FREEPLAY_API_KEY`
- All requests use Bearer token authentication
- Base URL configurable via `FREEPLAY_BASE_URL` (default: `https://app.freeplay.ai`)

## Development

```bash
# Clone and install
git clone https://github.com/freeplayai/freeplay-mcp.git
cd freeplay-mcp
uv sync --group dev

# Lint (with auto-fix)
make lint

# Type check
make type-check

# Run both
make check
```

### Using Docker

```json
{
  "mcpServers": {
    "freeplay": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "FREEPLAY_API_KEY",
        "-e",
        "FREEPLAY_BASE_URL",
        "freeplay-mcp"
      ],
      "env": {
        "FREEPLAY_API_KEY": "your-api-key",
        "FREEPLAY_BASE_URL": "https://app.freeplay.ai"
      }
    }
  }
}
```

## Support

- **Docs**: https://docs.freeplay.ai
- **Issues**: https://github.com/freeplayai/freeplay-mcp/issues
- **Security**: security@freeplay.ai
