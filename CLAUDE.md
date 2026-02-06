# CLAUDE.md - Guidance for AI assistants working with this codebase

This codebase is for a Freeplay MCP server.

## Project Structure

```
freeplay-mcp/
├── pyproject.toml
├── src/freeplay_mcp/
│   ├── api_client.py            # Shared API client setup, lazy initialization, helpers
│   ├── server.py                # MCP server entry point, registers tools from TOOLS list
│   ├── response.py              # Utilities/Models for MCP tool responses
│   ├── secrets.py               # Utilities to help obscure things such as API keys
│   ├── tools/                   # One file per tool or tool group
│   │   ├── __init__.py          # Exports all tool functions
│   │   ├── projects.py
│   │   ├── completions.py
│   │   └── ...
│   └── vendor/                 # Vendored dependencies
│       └── swagger_client/      # Auto-generated API client
├── main.py
├── Dockerfile
└── README.md
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

## Safety Classification System

All operations must be classified by risk level with appropriate safeguards:

**Level 0: Read (Unrestricted)**
- No confirmation needed
- Cannot modify any state
- Only operations that do not require agent confirmation
- Examples: search, list, get, analyze

**Level 1: Create (Visible)**
- Creates new resources but doesn't affect production
- Must require explicit confirmation with resource name and preview
- Examples: create prompt version (without deploy), create dataset, add test cases

**Level 2: Execute (Confirmable)**
- Runs operations that consume resources or create significant data
- Must require explicit confirmation with operation name
- Examples: run test, trigger optimization, run evaluations

**Level 3: Deploy (Requires Confirmation)**
- Affects production systems
- Must require explicit user confirmation
- Should show diff/impact before proceeding (e.g., summarizing before/after test run results before deploying a new prompt template version)
- Examples: deploy to production, enable evaluation criteria

**Level 4: Destroy with Version History (Strongly Protected)**
- Deletes or permanently modifies data with rollback support
- Should NEVER be executed by an agent without explicit confirmation
- Examples: delete prompt template version, delete test run

**Level 5: Destroy Resources (DISALLOWED)**
- Deletes or permanently modifies data without version history and rollback support
- Should NEVER be executed by an agent under any circumstances
- Examples: delete dataset, delete prompt template, remove test cases

## Adding a New Tool

### Tool Count: Why Less Is More

**Target: 20-25 total tools.** Based on Anthropic's best practices:

1. **Tool selection degrades as tool count grows.** Agents spend more turns deliberating and more often pick the wrong tool. Keep tools focused on workflows, not thin API wrappers.
2. **Each tool's docstring competes for attention.** More tools = more noise = worse performance on any individual tool.
3. **Maintenance burden scales linearly.** Every tool needs docstring polish, safety classification, tests, and version management.

**Every new tool must justify its existence** by unblocking a skill workflow or capability that currently requires raw API calls.

**Prefer few well-designed read tools over many narrow getters.** For example, `list_datasets` that returns enough detail to avoid needing a separate `get_dataset` is better than having both.

### File structure
1. Create a new file in `tools/` (or add to existing file if related)
2. Export the function from `tools/__init__.py`
3. Add to the `TOOLS` list in `server.py`

### Design principles
- **Tools are workflows, not API wrappers.** Don't create a 1:1 mapping with swagger endpoints. Design tools around what a user wants to accomplish, which may involve multiple API calls.
- **Start from the caller.** Before writing implementation, define the function signature and docstring. What would an LLM need to know to use this tool effectively?
- **Docstrings are the interface.** The docstring becomes the tool description shown to the LLM. Be clear and concise. Explain what the tool does in 1-2 sentences, then document every parameter with its type and purpose.
- **Consolidate related operations.** One tool that handles variations via parameters is better than multiple similar tools.

### Tool schema best practices
- Use descriptive parameter names (`project_id` not `pid`, `template_name` not `name`)
- Prefer `str` for IDs and structured input (e.g., JSON strings) - LLMs handle strings well
- Use sensible defaults to minimize required parameters
- Mark truly optional parameters with `| None = None`
- Keep parameter count reasonable - if you need many params, the tool might be doing too much
- Include examples in parameter descriptions (e.g., `environment: e.g. "staging", "production"`)

## Swagger Client

The auto-generated swagger client is vendored at `src/freeplay_mcp/vendor/swagger_client/`. Key patterns:
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

## Type Checking and Linting

```bash
uv run ruff check src/        # Lint
uv run ruff check --fix src/  # Lint + auto-fix
uv run basedpyright src/      # Type check
```

The swagger client is untyped, so pyright rules for unknown types are disabled. All other strict checks apply.