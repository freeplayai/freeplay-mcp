"""Insight-based prompt optimization tools."""

import asyncio
import logging
import os
import sys
from datetime import datetime

import httpx
from fastmcp.dependencies import Progress

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'swagger', 'python-api'))

from swagger_client.api.prompt_datasets_api import PromptDatasetsApi
from swagger_client.models.create_prompt_dataset_request import CreatePromptDatasetRequest
from swagger_client.models.create_prompt_test_cases_request import CreatePromptTestCasesRequest
from swagger_client.models.search_request import SearchRequest

from ..api_client import get_api_client, get_search_api
from ..response import DetailResponse
from .prompt_optimization import optimize_prompt

logger = logging.getLogger(__name__)


def _get_prompt_datasets_api() -> PromptDatasetsApi:
    """Get or create the Prompt Datasets API."""
    return PromptDatasetsApi(get_api_client())


async def optimize_prompt_from_insight(
    project_id: str,
    insight_name: str,
    prompt_template_version_id: str,
    max_test_cases: int = 100,
    user_instructions: str | None = None,
    use_best_practices: bool = True,
    use_labels: bool = True,
    use_customer_feedback: bool = True,
    run_test_after_optimization: bool = True,
    progress: Progress = Progress(),
) -> str:
    """Optimize a prompt based on completions matching an insight.

    Automatically creates a dataset from completions associated with a specific insight,
    then uses that dataset to optimize the prompt template. This eliminates the need to
    manually create and populate a dataset before optimization.

    The workflow:
    1. Creates a new dataset named "Insight: {insight_name} - {timestamp}"
    2. Searches for completions filtered by the insight name using the Search API
    3. Extracts input_variables from matching completions
    4. Bulk creates test cases in the new dataset (up to max_test_cases)
    5. Runs prompt optimization using the new dataset

    The insight_name should match the exact name of the insight as returned by the
    list_insights tool or as shown in the Freeplay UI.

    Args:
        project_id: The Freeplay project ID
        insight_name: The exact name of the insight to filter by (e.g., "Response Quality Issues")
        prompt_template_version_id: The prompt template version ID to optimize
        max_test_cases: Maximum number of test cases to create from insight completions (default: 100)
        user_instructions: Optional specific instructions for the optimization
        use_best_practices: Whether to apply general prompt engineering best practices (default: True)
        use_labels: Whether to use human labels from the dataset in analysis (default: True)
        use_customer_feedback: Whether to incorporate customer feedback data (default: True)
        run_test_after_optimization: Whether to run a comparison test after optimization (default: True)
    """
    if progress:
        await progress.set_total(5)
        await progress.set_message("Step 1/5: Creating dataset...")

    # Step 1: Create a new dataset
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dataset_name = f"Insight: {insight_name} - {timestamp}"
    
    datasets_api = _get_prompt_datasets_api()
    create_dataset_body = CreatePromptDatasetRequest(
        name=dataset_name,
        description=f"Auto-generated dataset from insight '{insight_name}' for prompt optimization",
    )
    
    dataset_result = await asyncio.to_thread(
        datasets_api.post_create_prompt_dataset,
        project_id,
        body=create_dataset_body,
    )
    
    if isinstance(dataset_result, dict):
        dataset_id = dataset_result.get('id')
    else:
        dataset_id = getattr(dataset_result, 'id', None)
    
    if not dataset_id:
        return "Error: Failed to create dataset. Could not retrieve dataset ID."

    if progress:
        await progress.set_message(f"Step 2/5: Searching completions for insight '{insight_name}'...")

    # Step 2: Search for completions filtered by insight name
    # Use the dedicated insight_name filter field from the Search API
    search_api = get_search_api()
    
    filters = {
        "field": "insight_name",
        "op": "eq",
        "value": insight_name,
    }
    
    search_body = SearchRequest(filters=filters)
    
    search_result = await asyncio.to_thread(
        search_api.post_search_completions,
        project_id,
        body=search_body,
        page=1,
        page_size=max_test_cases,
    )
    
    completions = search_result.data if hasattr(search_result, 'data') else []
    
    if not completions:
        # Clean up the empty dataset
        await asyncio.to_thread(
            datasets_api.delete_delete_prompt_dataset,
            project_id,
            dataset_id,
        )
        return f"Error: No completions found matching insight '{insight_name}'. Dataset was not created."

    if progress:
        await progress.set_message(f"Step 3/5: Extracting test cases from {len(completions)} completions...")

    # Step 3: Extract input_variables from completions and prepare test cases
    test_cases = []
    for comp in completions:
        if isinstance(comp, dict):
            input_variables = comp.get('input_variables', {})
        else:
            input_variables = getattr(comp, 'input_variables', {})
        
        if input_variables:
            test_cases.append({"inputs": input_variables})
        
        if len(test_cases) >= max_test_cases:
            break
    
    if not test_cases:
        # Clean up the empty dataset
        await asyncio.to_thread(
            datasets_api.delete_delete_prompt_dataset,
            project_id,
            dataset_id,
        )
        return "Error: No input_variables found in the completions. Cannot create test cases."

    if progress:
        await progress.set_message(f"Step 4/5: Creating {len(test_cases)} test cases in dataset...")

    # Step 4: Bulk create test cases
    create_test_cases_body = CreatePromptTestCasesRequest(data=test_cases)
    
    await asyncio.to_thread(
        datasets_api.post_bulk_create_prompt_dataset_test_cases,
        project_id,
        dataset_id,
        body=create_test_cases_body,
    )

    if progress:
        await progress.set_message("Step 5/5: Starting prompt optimization...")

    # Step 5: Run optimization with the new dataset
    optimization_result = await optimize_prompt(
        project_id=project_id,
        prompt_template_version_id=prompt_template_version_id,
        dataset_id=dataset_id,
        user_instructions=user_instructions,
        use_best_practices=use_best_practices,
        use_labels=use_labels,
        use_customer_feedback=use_customer_feedback,
        run_test_after_optimization=run_test_after_optimization,
        progress=progress,
    )

    # Prepend dataset creation info to the optimization result
    dataset_info = f"\nDataset Created:\n  ID: {dataset_id}\n  Name: {dataset_name}\n  Test Cases: {len(test_cases)}\n\n"
    
    return dataset_info + optimization_result
