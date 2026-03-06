"""Logging analysis tools."""

import asyncio

from pydantic import BaseModel

from freeplay_mcp.vendor.swagger_client.models.search_request import (
    SearchRequest,  # type: ignore[import-untyped]
)

from ..api_client import get_search_api
from ..response import ToolResponse


class LoggingIssue(BaseModel):
    field: str
    description: str
    fix_suggestion: str
    missing_count: int
    total_count: int


class LoggingAnalysisResponse(ToolResponse):
    template_name: str
    completions_analyzed: int
    issues: list[LoggingIssue]
    all_fields_present: list[str]
    completions_missing_prompt_template: int

    def _render_text(self) -> str:
        lines = [
            f"Logging Analysis for template: {self.template_name}",
            f"Completions analyzed: {self.completions_analyzed}",
            "",
        ]

        if self.completions_missing_prompt_template > 0:
            pct = (
                self.completions_missing_prompt_template
                / self.completions_analyzed
                * 100
            )
            lines.append("=" * 60)
            lines.append("CRITICAL: PROMPT TEMPLATE NOT LINKED")
            lines.append("=" * 60)
            lines.append(
                f"{self.completions_missing_prompt_template}/{self.completions_analyzed} completions ({pct:.0f}%) have no associated prompt template."
            )
            lines.append("")
            lines.append("Why this matters:")
            lines.append(
                "  - You cannot track prompt versions or see which prompt produced each completion"
            )
            lines.append(
                "  - A/B testing and prompt iteration become impossible to measure"
            )
            lines.append(
                "  - You lose the ability to correlate prompt changes with quality metrics"
            )
            lines.append("")
            lines.append("Recommended fix:")
            lines.append(
                "  Integrate Freeplay prompt management into your application:"
            )
            lines.append(
                "  1. Store your prompts in Freeplay using the prompt template editor"
            )
            lines.append(
                "  2. Fetch prompts at runtime using the Freeplay SDK's get_prompt() method"
            )
            lines.append(
                "  3. Use the SDK's record_completion() which automatically links the prompt template"
            )
            lines.append("")
            lines.append(
                "  This ensures every completion is tied to a specific prompt version,"
            )
            lines.append(
                "  enabling proper observability and prompt lifecycle management."
            )
            lines.append("")
            lines.append("=" * 60)
            lines.append("")

        if not self.issues:
            if self.completions_missing_prompt_template == 0:
                lines.append(
                    "No logging issues found. All recommended fields are being logged."
                )
                lines.append("")
            lines.append("Fields present:")
            for field in self.all_fields_present:
                lines.append(f"  - {field}")
            return "\n".join(lines)

        lines.append("MISSING FIELDS (action required):")
        lines.append("")

        for issue in self.issues:
            pct = (
                (issue.missing_count / issue.total_count * 100)
                if issue.total_count > 0
                else 100
            )
            lines.append(
                f"- {issue.field} (missing in {issue.missing_count}/{issue.total_count} completions, {pct:.0f}%)"
            )
            lines.append(f"  Why: {issue.description}")
            lines.append(f"  Fix: {issue.fix_suggestion}")
            lines.append("")

        if self.all_fields_present:
            lines.append("Fields already being logged:")
            for field in self.all_fields_present:
                lines.append(f"  - {field}")

        return "\n".join(lines)


LOGGABLE_FIELDS = {
    "session_id": {
        "description": "Groups related completions together for multi-turn conversations",
        "fix": "Pass a session_id when logging completions. Generate a UUID at conversation start and reuse it.",
    },
    "input_variables": {
        "description": "Template variables used to fill prompt placeholders - critical for debugging",
        "fix": "Pass the input_variables dict when recording completions. Include all template variables.",
    },
    "metadata.environment": {
        "description": "Deployment environment (staging/production) for filtering",
        "fix": "Set the environment field when recording completions based on your deployment context.",
    },
    "metadata.model": {
        "description": "Model name used - important when you use multiple models",
        "fix": "Pass the model name from your LLM configuration when recording completions.",
    },
    "metadata.provider": {
        "description": "Provider (openai/anthropic/etc) - useful for multi-provider setups",
        "fix": "Pass the provider name when recording completions.",
    },
}


def _is_empty(value: object) -> bool:
    if value is None:
        return True
    if isinstance(value, dict) and not value:
        return True
    if isinstance(value, str) and not value.strip():
        return True
    if isinstance(value, (list, tuple)) and not value:
        return True
    return False


def _analyze_completions(
    completions: list, check_prompt_template: bool = True
) -> tuple[list[LoggingIssue], list[str], int]:
    total = len(completions)
    if total == 0:
        return [], [], 0

    field_missing_counts: dict[str, int] = {field: 0 for field in LOGGABLE_FIELDS}
    missing_prompt_template_count = 0

    for comp in completions:
        session_id = comp.get("session_id")
        input_variables = comp.get("input_variables")
        metadata = comp.get("completion_metadata") or {}
        environment = metadata.get("environment")
        model = metadata.get("model")
        provider = metadata.get("provider")
        prompt_template = metadata.get("prompt_template")

        if check_prompt_template and _is_empty(prompt_template):
            missing_prompt_template_count += 1
        if _is_empty(session_id):
            field_missing_counts["session_id"] += 1
        if _is_empty(input_variables):
            field_missing_counts["input_variables"] += 1
        if _is_empty(environment):
            field_missing_counts["metadata.environment"] += 1
        if _is_empty(model):
            field_missing_counts["metadata.model"] += 1
        if _is_empty(provider):
            field_missing_counts["metadata.provider"] += 1

    issues = []
    present = []

    for field, info in LOGGABLE_FIELDS.items():
        missing_count = field_missing_counts[field]
        if missing_count > 0:
            issues.append(
                LoggingIssue(
                    field=field,
                    description=info["description"],
                    fix_suggestion=info["fix"],
                    missing_count=missing_count,
                    total_count=total,
                )
            )
        else:
            present.append(field)

    issues.sort(key=lambda x: x.missing_count, reverse=True)
    return issues, present, missing_prompt_template_count


async def find_logging_issues(
    project_id: str,
    template_name: str | None = None,
    environment: str | None = None,
    limit: int = 50,
) -> str:
    """Analyze recent completions for a prompt template and identify missing logged fields. This is a read-only analysis operation.

    Fetches recent completions and checks which important fields are not being logged.
    Returns a list of missing fields with explanations and fix suggestions. Use this to
    identify gaps in your observability instrumentation.

    Args:
        project_id: The Freeplay project ID
        template_name: Optional prompt template name to filter by. If not provided,
            analyzes all completions and checks for missing prompt template associations.
        environment: Optional environment filter (e.g., "prod", "dev", "local")
        limit: Number of recent completions to analyze (default: 50)
    """
    api = get_search_api()
    conditions = []
    if template_name:
        conditions.append(
            {"field": "prompt_template", "op": "eq", "value": template_name}
        )
    if environment:
        conditions.append({"field": "environment", "op": "eq", "value": environment})
    if len(conditions) == 0:
        filters: dict = {}
    elif len(conditions) == 1:
        filters = conditions[0]
    else:
        filters = {"and": conditions}

    body = SearchRequest(filters=filters)
    result = await asyncio.to_thread(
        api.post_search_completions, project_id, body=body, page=1, page_size=limit
    )

    completions = result.data

    if not completions:
        return LoggingAnalysisResponse(
            template_name=template_name or "(all completions)",
            completions_analyzed=0,
            issues=[],
            all_fields_present=[],
            completions_missing_prompt_template=0,
        ).render()

    check_prompt_template = template_name is None
    issues, present, missing_prompt_template_count = _analyze_completions(
        completions, check_prompt_template
    )

    return LoggingAnalysisResponse(
        template_name=template_name or "(all completions)",
        completions_analyzed=len(completions),
        issues=issues,
        all_fields_present=present,
        completions_missing_prompt_template=missing_prompt_template_count,
    ).render()
