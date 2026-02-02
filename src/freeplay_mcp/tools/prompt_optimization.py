"""Prompt optimization tools."""

import asyncio
import logging
import os

import httpx
from fastmcp.dependencies import Progress

from ..response import DetailResponse

logger = logging.getLogger(__name__)

TERMINAL_STATUSES = {"completed", "failed", "cancelled"}
POLL_INTERVAL_SECONDS = 5


def _get_http_client() -> httpx.AsyncClient:
    api_key = os.environ.get("FREEPLAY_API_KEY")
    if not api_key:
        raise ValueError("FREEPLAY_API_KEY environment variable is required.")

    base_url = os.environ.get("FREEPLAY_BASE_URL", "https://app.freeplay.ai").rstrip("/")
    verify_ssl_env = os.environ.get("FREEPLAY_VERIFY_SSL", "").lower()
    verify_ssl = verify_ssl_env not in ("false", "0", "no")

    return httpx.AsyncClient(
        base_url=base_url,
        headers={"Authorization": f"Bearer {api_key}"},
        verify=verify_ssl,
        timeout=30.0,
    )


async def _start_optimization_job(
    client: httpx.AsyncClient,
    project_id: str,
    prompt_template_version_id: str,
    dataset_id: str,
    user_instructions: str | None,
    use_best_practices: bool,
    use_labels: bool,
    use_customer_feedback: bool,
    run_test_after_optimization: bool,
) -> dict:
    payload = {
        "prompt_template_version_id": prompt_template_version_id,
        "dataset_id": dataset_id,
        "use_best_practices": use_best_practices,
        "use_labels": use_labels,
        "use_customer_feedback": use_customer_feedback,
        "run_test_after_optimization": run_test_after_optimization,
    }
    if user_instructions:
        payload["user_instructions"] = user_instructions

    response = await client.post(
        f"/api/v2/projects/{project_id}/prompt-optimization-jobs",
        json=payload,
    )
    response.raise_for_status()
    return response.json()


async def _get_job_status(
    client: httpx.AsyncClient,
    project_id: str,
    job_id: str,
) -> dict:
    response = await client.get(
        f"/api/v2/projects/{project_id}/prompt-optimization-jobs/{job_id}",
    )
    response.raise_for_status()
    return response.json()


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
        run_test_after_optimization: Whether to run a comparison test after optimization (default: True)
    """
    async with _get_http_client() as client:
        # Start the optimization job
        start_result = await _start_optimization_job(
            client=client,
            project_id=project_id,
            prompt_template_version_id=prompt_template_version_id,
            dataset_id=dataset_id,
            user_instructions=user_instructions,
            use_best_practices=use_best_practices,
            use_labels=use_labels,
            use_customer_feedback=use_customer_feedback,
            run_test_after_optimization=run_test_after_optimization,
        )

        job_id = start_result["job_id"]
        if progress:
            total_steps = 4 if run_test_after_optimization else 1
            await progress.set_total(total_steps)
            await progress.set_message("Starting optimization job...")

        # Poll until completion
        while True:
            status_result = await _get_job_status(client, project_id, job_id)
            status = status_result["status"]
            job_progress = status_result.get("progress", {})

            if progress and job_progress:
                step = job_progress.get("step", 1)
                step_name = job_progress.get("step_name", "Processing...")
                await progress.set_message(f"Step {step}: {step_name}")

            if status in TERMINAL_STATUSES:
                break

            await asyncio.sleep(POLL_INTERVAL_SECONDS)

        # Format the response based on final status
        if status == "failed":
            error_msg = status_result.get("error_message", "Unknown error")
            return f"Optimization failed: {error_msg}"

        if status == "cancelled":
            return "Optimization was cancelled."

        # Success - format the results
        changes_summary = status_result.get("changes_summary", "No changes summary available.")
        data_sources = status_result.get("data_sources_used", {})
        human_labels_count = data_sources.get("human_labels_count", 0)
        customer_feedback_count = data_sources.get("customer_feedback_count", 0)

        sections: dict[str, str | dict | list] = {
            "status": "completed",
            "original_version_id": prompt_template_version_id,
            "optimized_version_id": status_result.get("optimized_version_id", "N/A"),
            "changes_summary": changes_summary,
            "data_sources_used": f"{human_labels_count} human labels, {customer_feedback_count} customer feedback items",
        }

        if run_test_after_optimization:
            if status_result.get("test_run_id"):
                sections["test_run_id"] = status_result["test_run_id"]
            if status_result.get("comparison_id"):
                sections["comparison_id"] = status_result["comparison_id"]

        return DetailResponse(
            title="Prompt Optimization Complete",
            sections=sections,
        ).render()
