"""Prompt optimization tools."""

import asyncio
import logging

from fastmcp.dependencies import Progress

from freeplay_mcp.vendor.swagger_client.api.prompt_optimization_api import (
    PromptOptimizationApi,  # type: ignore[import-untyped]
)
from freeplay_mcp.vendor.swagger_client.models.start_prompt_optimization_job_request import (  # type: ignore[import-untyped]
    StartPromptOptimizationJobRequest,
)

from ..api_client import get_api_client
from ..response import DetailResponse

logger = logging.getLogger(__name__)

TERMINAL_STATUSES = {"completed", "failed", "cancelled"}
POLL_INTERVAL_SECONDS = 5


async def optimize_prompt(
    project_id: str,
    prompt_template_version_id: str,
    dataset_id: str,
    user_instructions: str | None = None,
    use_best_practices: bool = True,
    use_labels: bool = True,
    use_customer_feedback: bool = True,
    run_test_after_optimization: bool = True,
    progress: Progress = Progress(),
) -> str:
    """Optimize a prompt template using AI-powered analysis.

    Analyzes the prompt template version against examples from the dataset and
    generates an improved version. The optimization considers human labels,
    customer feedback, and best practices based on the flags provided.

    This is a long-running operation that may take several minutes. When
    run_test_after_optimization is True, the job will also run baseline and
    optimized test runs and create a comparison.

    Args:
        project_id: The Freeplay project ID
        prompt_template_version_id: The prompt template version ID to optimize
        dataset_id: The dataset ID containing examples to analyze
        user_instructions: Optional specific instructions for the optimization (e.g., "focus on reducing hallucinations")
        use_best_practices: Whether to apply general prompt engineering best practices (default: True)
        use_labels: Whether to use human labels from the dataset in analysis (default: True)
        use_customer_feedback: Whether to incorporate customer feedback data (default: True)
        run_test_after_optimization: Whether to run a comparison test after optimization (default: False)
    """
    api = PromptOptimizationApi(get_api_client())

    request = StartPromptOptimizationJobRequest(
        prompt_template_version_id=prompt_template_version_id,
        dataset_id=dataset_id,
        user_instructions=user_instructions,
        use_best_practices=use_best_practices,
        use_labels=use_labels,
        use_customer_feedback=use_customer_feedback,
        run_test_after_optimization=run_test_after_optimization,
    )

    start_result = await asyncio.to_thread(
        api.post_start_prompt_optimization_job,
        project_id,
        body=request,
    )

    job_id = start_result.job_id
    if progress:
        total_steps = 4 if run_test_after_optimization else 1
        await progress.set_total(total_steps)
        await progress.set_message("Starting optimization job...")

    while True:
        status_result = await asyncio.to_thread(
            api.get_get_prompt_optimization_job,
            project_id,
            job_id,
        )
        status = status_result.status
        job_progress = status_result.progress or {}

        if progress and job_progress:
            step = job_progress.get("step", 1) if isinstance(job_progress, dict) else 1
            step_name = job_progress.get("step_name", "Processing...") if isinstance(job_progress, dict) else "Processing..."
            await progress.set_message(f"Step {step}: {step_name}")

        if status in TERMINAL_STATUSES:
            break

        await asyncio.sleep(POLL_INTERVAL_SECONDS)

    if status == "failed":
        error_msg = status_result.error_message or "Unknown error"
        return f"Optimization failed: {error_msg}"

    if status == "cancelled":
        return "Optimization was cancelled."

    changes_summary = status_result.changes_summary or "No changes summary available."
    data_sources = status_result.data_sources_used or {}
    human_labels_count = data_sources.get("human_labels_count", 0) if isinstance(data_sources, dict) else 0
    customer_feedback_count = data_sources.get("customer_feedback_count", 0) if isinstance(data_sources, dict) else 0

    sections: dict[str, str | dict | list] = {
        "status": "completed",
        "original_version_id": prompt_template_version_id,
        "optimized_version_id": status_result.optimized_version_id or "N/A",
        "changes_summary": changes_summary,
        "data_sources_used": f"{human_labels_count} human labels, {customer_feedback_count} customer feedback items",
    }

    if run_test_after_optimization:
        if status_result.test_run_id:
            sections["test_run_id"] = status_result.test_run_id
        if status_result.comparison_id:
            sections["comparison_id"] = status_result.comparison_id

    return DetailResponse(
        title="Prompt Optimization Complete",
        sections=sections,
    ).render()
