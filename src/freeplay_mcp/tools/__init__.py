"""Freeplay MCP tools module.

This module exports all available tools for the Freeplay MCP server.
"""

from .projects import list_projects
from .completions import search_completions
from .traces import search_traces
from .sessions import search_sessions
from .prompts import list_prompt_templates, get_prompt_version, create_prompt_version, get_deployed_prompts
from .logging_analysis import find_logging_issues
from .prompt_optimization import optimize_prompt
from .insights import list_insights

__all__ = [
    "list_projects",
    "search_completions",
    "search_traces",
    "search_sessions",
    "list_prompt_templates",
    "get_prompt_version",
    "create_prompt_version",
    "get_deployed_prompts",
    "find_logging_issues",
    "optimize_prompt",
    "list_insights",
]
