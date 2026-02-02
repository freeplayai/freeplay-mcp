"""Freeplay MCP Server - Workflow-oriented tools for the Freeplay API."""

import logging
import sys

from fastmcp import FastMCP

from .tools import (
    list_projects,
    search_completions,
    search_traces,
    search_sessions,
    list_prompt_templates,
    get_prompt_version,
    create_prompt_version_and_deploy,
    find_logging_issues,
    optimize_prompt,
    generate_comparison_insights,
)

# Configure logging to stderr (stdout corrupts MCP JSON-RPC)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP("freeplay")

# Register all tools with the MCP server
TOOLS = [
    list_projects,
    search_completions,
    search_traces,
    search_sessions,
    list_prompt_templates,
    get_prompt_version,
    create_prompt_version_and_deploy,
    find_logging_issues,
]

for tool in TOOLS:
    mcp.tool()(tool)

# Register task-enabled tools (long-running async operations)
mcp.tool(task=True)(optimize_prompt)
mcp.tool(task=True)(generate_comparison_insights)


def main() -> None:
    """Run the Freeplay MCP server."""
    logger.info("Starting Freeplay MCP server")
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
