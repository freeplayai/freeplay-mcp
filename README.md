# Freeplay MCP Server - Implementation Approach

## Overview

A **workflow-oriented** MCP server that provides high-level operations for common Freeplay tasks, rather than
exposing every API endpoint directly.

## Installation instructions

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
1. Add the Freeplay MCP server to your claude code. From the freeplay-mcp directly.
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


## Project Structure

```
freeplay-mcp/
├── pyproject.toml          # Dependencies managed via uv
├── src/
│   └── freeplay_mcp/
│       ├── __init__.py
│       ├── server.py       # FastMCP server + tool definitions
│       └── client.py       # Freeplay API client (handles auth, requests)
```

## Dependencies (pyproject.toml)

- `mcp[cli]` - MCP SDK with FastMCP
- `httpx` - Async HTTP client for API requests
- Python 3.12 (3.14 is not stable yet; MCP SDK requires 3.10+)

## Authentication

- API key passed via environment variable `FREEPLAY_API_KEY`
- All requests use Bearer token authentication
- Base URL configurable via `FREEPLAY_BASE_URL` (default: `https://app.freeplay.ai`)

## Proposed Workflow Tools (Not 1:1 API Mapping)

| Tool                    | Description                                           | Combines APIs                       |
|-------------------------|-------------------------------------------------------|-------------------------------------|
| `list_projects`         | List available projects                               | Foundation for all other operations |
| `list_prompt_templates` | List templates in a project                           | GET templates                       |
| `get_prompt_template`   | Get template with current versions                    | GET template + versions             |
| `create_prompt_version` | Create a new version of a prompt                      | POST version by name/ID             |
| `deploy_prompt_version` | Deploy a version to an environment (dev/staging/prod) | POST environments                   |
| `list_datasets`         | List prompt datasets in a project                     | GET datasets                        |
| `create_test_run`       | Run tests against a dataset for a prompt              | POST test-runs                      |
| `get_test_run_results`  | Get test run results with statistics                  | GET test-run results                |
| `search_completions`    | Search logged completions with filters                | POST search/completions             |
| `get_prompt_statistics` | Get evaluation statistics for a prompt                | POST statistics                     |

## Freeplay Action Workflows

e.g. ```create_and_deploy_prompt```

## Design Principles

1. **Workflow-first**: Tools represent common developer workflows, not raw API endpoints
2. **Sensible defaults**: Minimize required parameters; use smart defaults
3. **Rich output**: Format responses for human readability (not just JSON dumps)
4. **Error handling**: Clear error messages with actionable guidance
5. **Logging to stderr**: Never write to stdout (corrupts MCP JSON-RPC)

## Example Tool Signature

```python
@mcp.tool()
async def create_prompt_version(
        project_id: str,
        template_name: str,
        messages: list[dict],
        model: str = "gpt-4",
        temperature: float = 0.7
) -> str:
    """Create a new version of a prompt template.

    Args:
        project_id: The Freeplay project ID
        template_name: Name of the prompt template
        messages: List of message dicts with role/content
        model: Model identifier (default: gpt-4)
        temperature: Sampling temperature (default: 0.7)
    """
```

## Running the Server

```bash
# Install dependencies
uv sync

# Run server (stdio transport)
uv run python -m freeplay_mcp.server

# Or via MCP CLI
uv run mcp run src/freeplay_mcp/server.py
```

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

## Security Limitations

This MCP server, like all MCP servers, operates within the security model
defined by the MCP host (e.g., Claude Code). We cannot prevent:

- Data exfiltration through composition with other MCP servers
- Prompt injection attacks that span multiple tools
- Malicious MCP servers from accessing data retrieved by this tool

Users should only connect MCP servers they fully trust and understand
that all connected servers operate within a shared security context.

## Support

- **Docs**: https://docs.freeplay.ai
- **Issues**: https://github.com/freeplayai/freeplay-mcp/issues
- **Security**: security@freeplay.ai
