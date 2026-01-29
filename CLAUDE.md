# AGENT.md - Guidance for AI assistants working with this codebase

This codebase is for a Freeplay MCP server. 

## Core Philosophy: Simplicity First

- Never add obvious comments or docstrings, prefer clarity through good naming
- Use early returns/guard statements over nested if statements
- Let exceptions bubble up. Don't do catch-all error handling.
- Always prefer fewer lines of code
- Do not type ignore to resolve issues - get the types right and fix the problem
- Do not use `Any` (in python) or `any` (ts) unless it's already in use for a value


## Key Development Practices

- **Workflows**: Just because an API exists, doesn't mean we need a tool call for it. Composed workflows that may invoke mulitple APIs is preferred.