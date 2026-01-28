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
    limit: int = 20,
    offset: int = 0,
    start_date: str | None = None,
    end_date: str | None = None,
    environment: str | None = None,
    template_name: str | None = None,
    prompt_template_id: str | None = None,
    model: str | None = None,
    provider: str | None = None,
    session_id: str | None = None,
    completion_id: str | None = None,
    agent_name: str | None = None,
    review_status: str | None = None,
    cost_min: float | None = None,
    cost_max: float | None = None,
    latency_min: float | None = None,
    latency_max: float | None = None,
) -> str:
    """Search logged completions in a Freeplay project.

    Args:
        project_id: The Freeplay project ID (required)
        limit: Maximum number of results to return (default: 20)
        offset: Number of results to skip for pagination (default: 0)
        start_date: Filter completions after this ISO date (e.g., "2024-01-01")
        end_date: Filter completions before this ISO date
        environment: Filter by environment (e.g., "production", "staging")
        template_name: Filter by prompt template name
        prompt_template_id: Filter by prompt template ID
        model: Filter by model name (e.g., "gpt-4", "claude-3")
        provider: Filter by provider (e.g., "openai", "anthropic")
        session_id: Filter by session ID
        completion_id: Filter by specific completion ID
        agent_name: Filter by agent name
        review_status: Filter by review status
        cost_min: Filter by minimum cost
        cost_max: Filter by maximum cost
        latency_min: Filter by minimum latency (ms)
        latency_max: Filter by maximum latency (ms)
    """
    try:
        client = get_client()
        result = await client.search_completions(
            project_id=project_id,
            limit=limit,
            offset=offset,
            start_date=start_date,
            end_date=end_date,
            environment=environment,
            template_name=template_name,
            prompt_template_id=prompt_template_id,
            model=model,
            provider=provider,
            session_id=session_id,
            completion_id=completion_id,
            agent_name=agent_name,
            review_status=review_status,
            cost_min=cost_min,
            cost_max=cost_max,
            latency_min=latency_min,
            latency_max=latency_max,
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
            model_name = metadata.get("model", "N/A")

            lines.append(f"- ID: {comp_id}")
            lines.append(f"  Template: {template} | Env: {env} | Model: {model_name}")
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


@mcp.tool()
async def search_traces(
    project_id: str,
    limit: int = 20,
    offset: int = 0,
    start_date: str | None = None,
    end_date: str | None = None,
    environment: str | None = None,
    template_name: str | None = None,
    prompt_template_id: str | None = None,
    model: str | None = None,
    provider: str | None = None,
    session_id: str | None = None,
    agent_name: str | None = None,
    review_status: str | None = None,
    cost_min: float | None = None,
    cost_max: float | None = None,
    latency_min: float | None = None,
    latency_max: float | None = None,
) -> str:
    """Search traces in a Freeplay project.

    Traces represent structured execution flows/chains within a session,
    and can have parent-child relationships.

    Args:
        project_id: The Freeplay project ID (required)
        limit: Maximum number of results to return (default: 20)
        offset: Number of results to skip for pagination (default: 0)
        start_date: Filter traces after this ISO date (e.g., "2024-01-01")
        end_date: Filter traces before this ISO date
        environment: Filter by environment (e.g., "production", "staging")
        template_name: Filter by prompt template name
        prompt_template_id: Filter by prompt template ID
        model: Filter by model name (e.g., "gpt-4", "claude-3")
        provider: Filter by provider (e.g., "openai", "anthropic")
        session_id: Filter by session ID
        agent_name: Filter by agent name
        review_status: Filter by review status
        cost_min: Filter by minimum cost
        cost_max: Filter by maximum cost
        latency_min: Filter by minimum latency (ms)
        latency_max: Filter by maximum latency (ms)
    """
    try:
        client = get_client()
        result = await client.search_traces(
            project_id=project_id,
            limit=limit,
            offset=offset,
            start_date=start_date,
            end_date=end_date,
            environment=environment,
            template_name=template_name,
            prompt_template_id=prompt_template_id,
            model=model,
            provider=provider,
            session_id=session_id,
            agent_name=agent_name,
            review_status=review_status,
            cost_min=cost_min,
            cost_max=cost_max,
            latency_min=latency_min,
            latency_max=latency_max,
        )

        traces = result.get("data", result.get("traces", []))
        pagination = result.get("pagination", {})
        has_next = pagination.get("has_next", False)

        if not traces:
            return "No traces found matching the search criteria."

        lines = [f"Found {len(traces)} traces (has_next: {has_next}):", ""]

        for trace in traces:
            trace_id = trace.get("trace_id", trace.get("id", "unknown"))
            name = trace.get("name", "N/A")
            kind = trace.get("kind", "N/A")
            agent = trace.get("agent_name", "N/A")
            start_time = trace.get("start_time", "unknown")
            end_time = trace.get("end_time", "unknown")
            parent_id = trace.get("parent_id", None)

            lines.append(f"- ID: {trace_id}")
            lines.append(f"  Name: {name} | Kind: {kind} | Agent: {agent}")
            lines.append(f"  Time: {start_time} -> {end_time}")
            if parent_id:
                lines.append(f"  Parent: {parent_id}")

            # Show truncated input/output if available
            trace_input = trace.get("input", "")
            if trace_input:
                content = str(trace_input)[:100]
                if len(str(trace_input)) > 100:
                    content += "..."
                lines.append(f"  Input: {content}")

            lines.append("")

        return "\n".join(lines)

    except Exception as e:
        logger.exception("Error searching traces")
        return f"Error searching traces: {e}"


@mcp.tool()
async def search_sessions(
    project_id: str,
    limit: int = 20,
    offset: int = 0,
    start_date: str | None = None,
    end_date: str | None = None,
    environment: str | None = None,
    template_name: str | None = None,
    prompt_template_id: str | None = None,
    model: str | None = None,
    provider: str | None = None,
    session_id: str | None = None,
    agent_name: str | None = None,
    review_status: str | None = None,
    cost_min: float | None = None,
    cost_max: float | None = None,
    latency_min: float | None = None,
    latency_max: float | None = None,
) -> str:
    """Search sessions in a Freeplay project.

    Sessions are top-level containers that group related traces and completions together.

    Args:
        project_id: The Freeplay project ID (required)
        limit: Maximum number of results to return (default: 20)
        offset: Number of results to skip for pagination (default: 0)
        start_date: Filter sessions after this ISO date (e.g., "2024-01-01")
        end_date: Filter sessions before this ISO date
        environment: Filter by environment (e.g., "production", "staging")
        template_name: Filter by prompt template name
        prompt_template_id: Filter by prompt template ID
        model: Filter by model name (e.g., "gpt-4", "claude-3")
        provider: Filter by provider (e.g., "openai", "anthropic")
        session_id: Filter by specific session ID
        agent_name: Filter by agent name
        review_status: Filter by review status
        cost_min: Filter by minimum cost
        cost_max: Filter by maximum cost
        latency_min: Filter by minimum latency (ms)
        latency_max: Filter by maximum latency (ms)
    """
    try:
        client = get_client()
        result = await client.search_sessions(
            project_id=project_id,
            limit=limit,
            offset=offset,
            start_date=start_date,
            end_date=end_date,
            environment=environment,
            template_name=template_name,
            prompt_template_id=prompt_template_id,
            model=model,
            provider=provider,
            session_id=session_id,
            agent_name=agent_name,
            review_status=review_status,
            cost_min=cost_min,
            cost_max=cost_max,
            latency_min=latency_min,
            latency_max=latency_max,
        )

        sessions = result.get("data", result.get("sessions", []))
        pagination = result.get("pagination", {})
        has_next = pagination.get("has_next", False)

        if not sessions:
            return "No sessions found matching the search criteria."

        lines = [f"Found {len(sessions)} sessions (has_next: {has_next}):", ""]

        for session in sessions:
            sess_id = session.get("session_id", session.get("id", "unknown"))
            env = session.get("environment", "N/A")
            start_time = session.get("start_time", "unknown")
            metadata = session.get("custom_metadata", {})

            lines.append(f"- ID: {sess_id}")
            lines.append(f"  Environment: {env}")
            lines.append(f"  Time: {start_time}")
            if metadata:
                meta_str = ", ".join(f"{k}={v}" for k, v in list(metadata.items())[:3])
                if len(metadata) > 3:
                    meta_str += ", ..."
                lines.append(f"  Metadata: {meta_str}")

            lines.append("")

        return "\n".join(lines)

    except Exception as e:
        logger.exception("Error searching sessions")
        return f"Error searching sessions: {e}"


def main() -> None:
    """Run the Freeplay MCP server."""
    logger.info("Starting Freeplay MCP server")
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
