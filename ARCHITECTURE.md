# Freeplay MCP Architecture

## Overview

This MCP server follows a **composable tools** architecture where each tool does one thing well, and workflows are guided by Claude Code skills.

## Design Principles

1. **Atomic Tools** - Each tool performs a single, well-defined operation
2. **Composable** - Tools can be combined to create complex workflows
3. **Guided by Skills** - Skills (in plugin) guide when and how to use tools
4. **Resource Context** - Resources provide upfront context to reduce tool calls

## Architecture Layers

```
┌─────────────────────────────────────────────────────────────┐
│ Claude Code Plugin (freeplay-plugin/)                       │
│ ┌─────────────────┐  ┌──────────────┐  ┌────────────────┐ │
│ │ Skills          │  │ Commands     │  │ Agents         │ │
│ │ - When to use   │  │ - User slash │  │ - Specialized  │ │
│ │ - How to combine│  │   commands   │  │   subagents    │ │
│ └─────────────────┘  └──────────────┘  └────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│ MCP Server (freeplay-mcp/)                                  │
│ ┌──────────┐  ┌──────────┐  ┌──────────────────────────┐  │
│ │ Tools    │  │Resources │  │ API Client               │  │
│ │ - Atomic │  │ - Context│  │ - Swagger-generated      │  │
│ │ - Single │  │ - Projects│  │ - Auth & config          │  │
│ │   purpose│  │ - Prompts│  │                          │  │
│ └──────────┘  └──────────┘  └──────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│ Freeplay API                                                │
└─────────────────────────────────────────────────────────────┘
```

## Tool Categories

### 1. Project & Context Tools
- `list_projects` - List all projects
- Resource: `freeplay://context/all` - All projects and prompts

### 2. Search Tools
- `search_completions` - Generic completion search with filters
- `search_traces` - Search traces
- `search_sessions` - Search sessions
- `search_completions_by_insight` - Focused insight search

### 3. Prompt Management Tools
- `list_prompt_templates` - List prompts in a project
- `get_prompt_version` - Get specific version details
- `create_prompt_version_and_deploy` - Create and deploy version

### 4. Dataset Tools
- `list_datasets` - List all datasets in a project
- `create_prompt_dataset` - Create new dataset
- `add_completions_to_dataset` - Populate dataset from completions

### 5. Insight Tools
- `list_insights` - List available insights
- `search_completions_by_insight` - Find completions for an insight

### 6. Optimization Tools (Task-enabled)
- `optimize_prompt` - Run optimization on a dataset
- `optimize_prompt_from_insight` - All-in-one insight optimization

### 7. Analysis Tools
- `find_logging_issues` - Analyze logging patterns

## Example Workflows

### Insight-Based Optimization (Atomic)

Using individual tools for full control:

```python
# 1. Discover insights
list_insights(project_id="...")

# 2. Preview data
completions = search_completions_by_insight(
    project_id="...",
    insight_name="Response Quality Issues"
)

# 3. Create dataset
dataset = create_prompt_dataset(
    project_id="...",
    name="Quality Dataset",
)

# 4. Populate dataset
add_completions_to_dataset(
    project_id="...",
    dataset_id=dataset_id,
    completions=completions,
)

# 5. Optimize
optimize_prompt(
    project_id="...",
    prompt_template_version_id="...",
    dataset_id=dataset_id,
)
```

### Insight-Based Optimization (Convenience)

Using the all-in-one tool:

```python
optimize_prompt_from_insight(
    project_id="...",
    insight_name="Response Quality Issues",
    prompt_template_version_id="...",
)
```

## File Organization

```
freeplay-mcp/
├── src/freeplay_mcp/
│   ├── server.py              # Tool & resource registration
│   ├── api_client.py          # Shared API client setup
│   ├── resources.py           # MCP resources
│   ├── response.py            # Response formatters
│   └── tools/
│       ├── __init__.py        # Tool exports
│       ├── projects.py        # Project tools
│       ├── completions.py     # Completion search
│       ├── traces.py          # Trace search
│       ├── sessions.py        # Session search
│       ├── prompts.py         # Prompt management
│       ├── datasets.py        # Dataset management (NEW)
│       ├── insights.py        # Insight tools (ENHANCED)
│       ├── prompt_optimization.py  # Core optimization
│       ├── insight_optimization.py # Insight convenience tool
│       └── logging_analysis.py     # Analysis tools
└── swagger/                   # Auto-generated API client
```

## Skills (Claude Code Plugin)

Skills live in `freeplay-plugin/skills/` and guide workflows:

```
skills/
├── insight-optimization/
│   └── SKILL.md              # When/how to optimize from insights
└── deployed-prompts/
    └── SKILL.md              # Prompt deployment guidance
```

## Best Practices

### When to Create a New Tool

Create a new tool when:
- ✅ It performs a single, atomic operation
- ✅ It could be useful on its own
- ✅ It's composable with other tools
- ✅ It maps to a specific API endpoint or small group of related endpoints

### When to Create a Skill

Create a skill when:
- ✅ Multiple tools need to be combined in a specific order
- ✅ There are decision points in the workflow
- ✅ Context or best practices need to be communicated
- ✅ The workflow is triggered by specific user intents

### When to Create a Convenience Tool

Create a convenience tool (like `optimize_prompt_from_insight`) when:
- ✅ The workflow is common and repetitive
- ✅ All atomic tools exist individually
- ✅ Users would benefit from a one-step option
- ✅ The workflow has minimal decision points

## Resource Strategy

Resources provide **upfront context** to reduce tool calls:

- `freeplay://context/all` - All projects and their prompts
  - Helps LLM disambiguate project names vs. prompt names
  - Loaded once at conversation start
  - Always fresh (no caching)

## Migration Notes

### Old CLI Script → New Architecture

The old `create_insight_dataset.py` script has been superseded by:

1. **Atomic tools**:
   - `search_completions_by_insight` (replaces search function)
   - `create_prompt_dataset` (replaces dataset creation)
   - `add_completions_to_dataset` (replaces test case upload)

2. **Convenience tool**:
   - `optimize_prompt_from_insight` (entire workflow)

3. **Skill**:
   - `skills/insight-optimization/SKILL.md` (guides usage)

The CLI script can be archived or deleted as all functionality is now in the MCP server.
