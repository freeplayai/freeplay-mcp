# Freeplay MCP Server

An MCP (Model Context Protocol) server that enables AI agents to interact with the Freeplay platform. Agents can browse projects, test and score prompt changes, find insights about recent production behavior, and search through logs to analyze performance.

## ⚠️ EXPERIMENTAL

**This MCP server is an *experimental release* and will change.** Use at your own risk and keep an eye on what your agents are doing.

Current limitations:
- Does not support deployment operations or destructive deletion actions --> use the Freeplay UI
- Uses your regular Freeplay API key (not specially scoped to limit access for agents)

**Security warning:** Because this uses your full API key, an agent could extract the key and write its own code outside the MCP to perform destructive actions against your Freeplay account.

Additionally, all MCP servers share a security context within the host, enabling data exfiltration, prompt injection across tools, and cross-server data access.

Only use this with agents and MCP servers you fully trust.

And even for agents you do trust, keep in mind they can always attempt to formulate their own API calls outside the scope of the tools included with this MCP server.

---

## Installation

### Claude Code (with uv)

1. Clone this repository locally.
   ```shell
   git clone git@github.com:freeplayai/freeplay-mcp.git
   ```
1.
   ```shell
   cd freeplay-mcp
   uv sync # install dependencies
   ```
1. Add the Freeplay MCP server to your Claude Code. From the freeplay-mcp directory.
    ```shell
   claude mcp add --transport stdio freeplay-mcp-v1 -- uv run main.py
    ```
1. Configure `.env` and:
   ```shell
   source .env
   ```
1. Start Claude code and run `/mcp` to check installation.

### Claude Code (with Docker)

1. Clone this repository locally.
   ```shell
   git clone git@github.com:freeplayai/freeplay-mcp.git
   cd freeplay-mcp
   ```

2. Build the Docker image.
   ```shell
   docker build -t freeplay-mcp .
   ```
   For production deployments, consider using a hardened base image such as [Chainguard](https://www.chainguard.dev/) or [Distroless](https://github.com/GoogleContainerTools/distroless).

3. Set your environment variables (in .env, then source it).
   ```shell
   export FREEPLAY_API_KEY="your-api-key"
   export FREEPLAY_BASE_URL="https://app.freeplay.ai"
   ```

4. Add the Freeplay MCP server to Claude Code.
   ```sh
   claude mcp add --transport stdio freeplay-mcp-v1 -- docker run -i --rm -e FREEPLAY_API_KEY=$FREEPLAY_API_KEY -e FREEPLAY_BASE_URL=$FREEPLAY_BASE_URL freeplay-mcp
   ```

5. Start Claude Code and run `/mcp` to check installation.

## Authentication

- API key passed via environment variable `FREEPLAY_API_KEY`
- All requests use Bearer token authentication
- Base URL configurable via `FREEPLAY_BASE_URL` (default: `https://app.freeplay.ai`)


## Development

```bash
# Install dev dependencies
uv sync --dev

# Lint (with auto-fix)
uv run ruff check --fix src/

# Type check
uv run basedpyright src/
```

## Claude Desktop Configuration

### Using uv

```json
{
  "mcpServers": {
    "freeplay": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/freeplay-mcp",
        "run",
        "python",
        "-m",
        "freeplay_mcp.server"
      ],
      "env": {
        "FREEPLAY_API_KEY": "your-api-key"
      }
    }
  }
}
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
        "-e", "FREEPLAY_API_KEY",
        "-e", "FREEPLAY_BASE_URL",
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
