"""Freeplay MCP Server - Workflow-oriented tools for the Freeplay API."""

import logging
import sys

from mcp.server.fastmcp import FastMCP

from freeplay_mcp.freeplay_client import FreeplayClient

# Configure logging to stderr (stdout corrupts MCP JSON-RPC)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP("freeplay")

# Lazy-initialized client (created on first tool call)
_client: FreeplayClient | None = None


def get_client() -> FreeplayClient:
    """Get or create the Freeplay API client."""
    global _client
    if _client is None:
        _client = FreeplayClient()
    return _client


@mcp.tool()
async def list_projects() -> str:
    """List all Freeplay projects accessible to the authenticated user.

    Returns a formatted list of projects with their IDs and names.
    Use a project ID from this list for other Freeplay operations.
    """
    try:
        client = get_client()
        projects = await client.list_projects()

        if not projects:
            return "No projects found."

        lines = ["Available Freeplay Projects:", ""]
        for project in projects:
            project_id = project.get("id", "unknown")
            name = project.get("name", "Unnamed")
            description = project.get("description", "")

            line = f"- {name} (ID: {project_id})"
            if description:
                line += f"\n  {description}"
            lines.append(line)

        return "\n".join(lines)

    except Exception as e:
        logger.exception("Error listing projects")
        return f"Error listing projects: {e}"


@mcp.tool()
async def search_completions(
    project_id: str,
    query: str | None = None,
    limit: int = 20,
    offset: int = 0,
    start_date: str | None = None,
    end_date: str | None = None,
    environment: str | None = None,
    template_name: str | None = None,
) -> str:
    """Search logged completions in a Freeplay project.

    Args:
        project_id: The Freeplay project ID (required)
        query: Text query to search in completions
        limit: Maximum number of results to return (default: 20)
        offset: Number of results to skip for pagination (default: 0)
        start_date: Filter completions after this ISO date (e.g., "2024-01-01")
        end_date: Filter completions before this ISO date
        environment: Filter by environment (e.g., "production", "staging")
        template_name: Filter by prompt template name
    """
    try:
        client = get_client()
        result = await client.search_completions(
            project_id=project_id,
            query=query,
            limit=limit,
            offset=offset,
            start_date=start_date,
            end_date=end_date,
            environment=environment,
            template_name=template_name,
        )

        completions = result.get("data", result.get("completions", []))
        pagination = result.get("pagination", {})
        has_next = pagination.get("has_next", False)

        if not completions:
            return "No completions found matching the search criteria."

        lines = [f"Found {len(completions)} completions (has_next: {has_next}):", ""]

        for comp in completions:
            comp_id = comp.get("completion_id", comp.get("id", "unknown"))
            metadata = comp.get("completion_metadata", {})
            start_time = metadata.get("start_time", "unknown")
            template_info = metadata.get("prompt_template", {})
            template = template_info.get("name", "N/A") if template_info else "N/A"
            env = metadata.get("environment", "N/A")
            model = metadata.get("model", "N/A")

            lines.append(f"- ID: {comp_id}")
            lines.append(f"  Template: {template} | Env: {env} | Model: {model}")
            lines.append(f"  Time: {start_time}")

            # Show truncated input/output if available
            if messages := comp.get("messages"):
                last_msg = messages[-1] if messages else {}
                content = str(last_msg.get("content", ""))[:100]
                if len(str(last_msg.get("content", ""))) > 100:
                    content += "..."
                lines.append(f"  Last message: {content}")

            lines.append("")

        return "\n".join(lines)

    except Exception as e:
        logger.exception("Error searching completions")
        return f"Error searching completions: {e}"


def main() -> None:
    """Run the Freeplay MCP server."""
    logger.info("Starting Freeplay MCP server")
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
