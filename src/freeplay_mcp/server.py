"""Freeplay MCP Server - Workflow-oriented tools for the Freeplay API."""

import json
import logging
import sys

from mcp.server.fastmcp import FastMCP

from freeplay_mcp.client import FreeplayClient

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
    """Build a search completions API request without executing it.

    Returns the HTTP request details as JSON for the calling agent to execute.
    This allows the agent to inspect, modify, or execute the request as needed.

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

        # Build request body with only provided parameters
        body: dict = {
            "project_id": project_id,
            "limit": limit,
            "offset": offset,
        }

        if query is not None:
            body["query"] = query
        if start_date is not None:
            body["start_date"] = start_date
        if end_date is not None:
            body["end_date"] = end_date
        if environment is not None:
            body["environment"] = environment
        if template_name is not None:
            body["template_name"] = template_name

        # Build the request object
        request_info = {
            "method": "POST",
            "url": f"{client.base_url}/api/v2/search/completions",
            "headers": {
                "Authorization": "Bearer {FREEPLAY_API_KEY}",
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
            "body": body,
        }

        return json.dumps(request_info, indent=2)

    except Exception as e:
        logger.exception("Error building search completions request")
        return json.dumps({"error": str(e)})


def main() -> None:
    """Run the Freeplay MCP server."""
    logger.info("Starting Freeplay MCP server")
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
