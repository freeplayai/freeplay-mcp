# CLAUDE.md - Guidance for AI assistants working with this codebase

This codebase is for a Freeplay MCP server.

## Project Structure

```
src/freeplay_mcp/
├── api_client.py        # Shared API client setup, lazy initialization, helpers
├── server.py            # MCP server entry point, registers tools from TOOLS list
└── tools/               # One file per tool or tool group
    ├── __init__.py      # Exports all tool functions
    ├── projects.py
    ├── completions.py
    └── ...
```

## Core Philosophy: Simplicity First

- Never add obvious comments or docstrings, prefer clarity through good naming. An exception is for the tool
  definitions. These should be concise but clear and written for an LLM who does not have context on the whole system.
- Use early returns/guard statements over nested if statements
- Let exceptions bubble up. Don't do catch-all error handling.
- Always prefer fewer lines of code
- Do not type ignore to resolve issues - get the types right and fix the problem
- Do not use `Any` (in python) or `any` (ts) unless it's already in use for a value

## Key Development Practices

- **Respond in plaintext**: MCP results will be read by an LLM, so we should return clearly structured
  text responses.
- **Do not print**: Stdio is used for returning a response. It is critical to avoid print statements other than for
  a response.

## Adding a New Tool

### File structure
1. Create a new file in `tools/` (or add to existing file if related)
2. Export the function from `tools/__init__.py`
3. Add to the `TOOLS` list in `server.py`

### Design principles
- **Tools are workflows, not API wrappers.** Don't create a 1:1 mapping with swagger endpoints. Design tools around
  what a user wants to accomplish, which may involve multiple API calls.
- **Start from the caller.** Before writing implementation, define the function signature and docstring. What would
  an LLM need to know to use this tool effectively?
- **Docstrings are the interface.** The docstring becomes the tool description shown to the LLM. Be clear and concise.
  Explain what the tool does in 1-2 sentences, then document every parameter with its type and purpose.

### Tool schema best practices
- Use descriptive parameter names (`project_id` not `pid`, `template_name` not `name`)
- Prefer `str` for IDs and structured input (e.g., JSON strings) - LLMs handle strings well
- Use sensible defaults to minimize required parameters
- Mark truly optional parameters with `| None = None`
- Keep parameter count reasonable - if you need many params, the tool might be doing too much
- Include examples in parameter descriptions (e.g., `environment: e.g. "staging", "production"`)

## Swagger Client

The auto-generated swagger client lives at `swagger/python-api/`. Key patterns:
- API responses are dicts - access fields with `result.get('field')` or `result['field']`
- Use `asyncio.to_thread()` to call the synchronous swagger methods
- Request models are in `swagger_client.models`
- Do not use any `/review-themes` endpoints, these are not available for consumption.

## Environment Variables

- `FREEPLAY_API_KEY` (required) - Bearer token for API auth
- `FREEPLAY_BASE_URL` (optional) - Default: `https://app.freeplay.ai`
- `FREEPLAY_VERIFY_SSL` (optional) - Set to `false` for local dev

## Running the Server

```bash
uv run freeplay-mcp
```