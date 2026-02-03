"""Prompt dataset management tools."""

import asyncio
import logging
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'swagger', 'python-api'))

from swagger_client.api.prompt_datasets_api import PromptDatasetsApi
from swagger_client.models.create_prompt_dataset_request import CreatePromptDatasetRequest
from swagger_client.models.create_prompt_test_cases_request import CreatePromptTestCasesRequest

from ..api_client import get_api_client
from ..response import ActionResponse, ListItem, ListResponse

logger = logging.getLogger(__name__)


def _get_datasets_api() -> PromptDatasetsApi:
    """Get or create the Prompt Datasets API."""
    return PromptDatasetsApi(get_api_client())


async def create_prompt_dataset(
    project_id: str,
    name: str,
    description: str | None = None,
    input_names: list[str] | None = None,
) -> str:
    """Create a new prompt dataset.

    Creates an empty dataset for organizing prompt test cases. Use this to
    create datasets manually or as part of automated workflows.

    Args:
        project_id: The Freeplay project ID
        name: Name for the dataset (must be unique within project)
        description: Optional description of the dataset's purpose
        input_names: Optional list of expected input variable names
    """
    api = _get_datasets_api()
    
    create_body = CreatePromptDatasetRequest(
        name=name,
        description=description,
        input_names=input_names,
    )
    
    result = await asyncio.to_thread(
        api.post_create_prompt_dataset,
        project_id,
        body=create_body,
    )
    
    if isinstance(result, dict):
        dataset_id = result.get('id', 'unknown')
    else:
        dataset_id = getattr(result, 'id', 'unknown')
    
    details = {
        "dataset_id": dataset_id,
        "name": name,
    }
    if description:
        details["description"] = description
    
    return ActionResponse(
        message="Dataset created successfully",
        details=details,
    ).render()


async def add_completions_to_dataset(
    project_id: str,
    dataset_id: str,
    completions: list[dict],
    max_test_cases: int = 100,
) -> str:
    """Add test cases to a dataset from completion data.

    Extracts input_variables from completions and creates test cases in the dataset.
    Useful for building datasets from production data or search results.

    Args:
        project_id: The Freeplay project ID
        dataset_id: The dataset ID to add test cases to
        completions: List of completion objects (from search_completions results)
        max_test_cases: Maximum number of test cases to add (default: 100)
    """
    api = _get_datasets_api()
    
    # Extract input_variables from completions
    test_cases = []
    for comp in completions[:max_test_cases]:
        if isinstance(comp, dict):
            input_variables = comp.get('input_variables', {})
        else:
            input_variables = getattr(comp, 'input_variables', {})
        
        if input_variables:
            test_cases.append({"inputs": input_variables})
    
    if not test_cases:
        return "No valid input_variables found in completions. No test cases created."
    
    # Bulk create test cases
    create_body = CreatePromptTestCasesRequest(data=test_cases)
    
    await asyncio.to_thread(
        api.post_bulk_create_prompt_dataset_test_cases,
        project_id,
        dataset_id,
        body=create_body,
    )
    
    return ActionResponse(
        message="Test cases added to dataset",
        details={
            "dataset_id": dataset_id,
            "test_cases_added": len(test_cases),
            "completions_processed": len(completions),
        },
    ).render()


async def list_datasets(
    project_id: str,
    page: int = 1,
    page_size: int = 50,
) -> str:
    """List prompt datasets in a project.

    Returns a list of all prompt datasets with their IDs, names, and test case counts.

    Args:
        project_id: The Freeplay project ID
        page: Page number for pagination (default: 1)
        page_size: Number of datasets per page (default: 50)
    """
    api = _get_datasets_api()
    
    result = await asyncio.to_thread(
        api.get_get_prompt_datasets,
        project_id,
        page=page,
        page_size=page_size,
    )
    
    if isinstance(result, dict):
        datasets = result.get('data', [])
    else:
        datasets = getattr(result, 'data', [])
    
    if not datasets:
        return "No datasets found in this project."
    
    items = []
    for dataset in datasets:
        if isinstance(dataset, dict):
            dataset_id = dataset.get('id', 'unknown')
            name = dataset.get('name', 'Unnamed')
            test_case_count = dataset.get('test_case_count', 0)
            description = dataset.get('description', '')
        else:
            dataset_id = getattr(dataset, 'id', 'unknown')
            name = getattr(dataset, 'name', 'Unnamed')
            test_case_count = getattr(dataset, 'test_case_count', 0)
            description = getattr(dataset, 'description', '')
        
        lines = [f"Test Cases: {test_case_count}"]
        if description:
            lines.append(f"Description: {description}")
        
        items.append(ListItem(
            id=dataset_id,
            title=name,
            lines=lines,
        ))
    
    return ListResponse(
        header=f"Found {len(items)} datasets",
        items=items,
    ).render()
