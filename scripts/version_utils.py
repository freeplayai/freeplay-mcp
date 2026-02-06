#!/usr/bin/env python3
"""
Version utilities for the publish workflow.
Handles version extraction, alpha version calculation, and PyPI version checking.
"""

import json
import re
import sys
import urllib.request
from typing import Optional

from packaging.version import parse


PACKAGE_NAME = "freeplay-mcp"


def get_version_from_pyproject() -> str:
    """Extract version from pyproject.toml."""
    try:
        with open("pyproject.toml", "r") as f:
            content = f.read()
        match = re.search(r'version = "([^"]+)"', content)
        return match.group(1) if match else ""
    except Exception as e:
        print(f"Error reading pyproject.toml: {e}", file=sys.stderr)
        sys.exit(1)


def update_version_in_pyproject(new_version: str) -> None:
    """Update version in pyproject.toml."""
    try:
        with open("pyproject.toml", "r") as f:
            content = f.read()
        content = re.sub(r'version = "[^"]+"', f'version = "{new_version}"', content)
        with open("pyproject.toml", "w") as f:
            f.write(content)
    except Exception as e:
        print(f"Error updating pyproject.toml: {e}", file=sys.stderr)
        sys.exit(1)


def get_all_pypi_versions(
    package_name: str = PACKAGE_NAME, repository: str = "pypi"
) -> list[str]:
    """Get all versions from PyPI or TestPyPI for the given package."""
    if repository == "testpypi":
        url = f"https://test.pypi.org/pypi/{package_name}/json"
    else:
        url = f"https://pypi.org/pypi/{package_name}/json"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.load(response)
            return list(data["releases"].keys())
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return []
        raise


def get_latest_pypi_version(
    package_name: str = PACKAGE_NAME, repository: str = "pypi"
) -> str:
    """Get the latest version (including prereleases) from PyPI or TestPyPI."""
    all_versions = get_all_pypi_versions(package_name, repository)
    if not all_versions:
        return "0.0.0"

    sorted_versions = sorted(all_versions, key=parse)
    return sorted_versions[-1]


def get_next_alpha_version(
    version: str, package_name: str = PACKAGE_NAME, repository: str = "pypi"
) -> str:
    """Get the next available alpha version for the given version."""
    alpha_pattern = re.compile(r"^(.+)a(\d+)$")
    alpha_match = alpha_pattern.match(version)

    if alpha_match:
        base_version = alpha_match.group(1)
        print(
            f"Input version {version} is already an alpha version, using base: {base_version}"
        )
    else:
        base_version = version

    all_versions = get_all_pypi_versions(package_name, repository)

    base_alpha_pattern = re.compile(f"^{re.escape(base_version)}a(\\d+)$")
    alpha_numbers: list[int] = []

    for pypi_version in all_versions:
        match = base_alpha_pattern.match(pypi_version)
        if match:
            alpha_numbers.append(int(match.group(1)))

    if alpha_numbers:
        next_num = max(alpha_numbers) + 1
    else:
        next_num = 1

    return f"{base_version}a{next_num}"


def version_exists_on_pypi(
    version: str, package_name: str = PACKAGE_NAME, repository: str = "pypi"
) -> bool:
    """Check if a specific version exists on PyPI or TestPyPI."""
    all_versions = get_all_pypi_versions(package_name, repository)
    return version in all_versions


def determine_publish_version(
    release_type: str, base_version: Optional[str] = None
) -> tuple[str, bool]:
    """
    Determine the version to publish based on release type.

    Returns:
        Tuple of (version_to_publish, should_update_pyproject)
    """
    if base_version is None:
        base_version = get_version_from_pyproject()

    if release_type == "stable":
        return base_version, False
    else:
        alpha_version = get_next_alpha_version(base_version)
        return alpha_version, True


def main() -> None:
    """Main function for command-line usage."""
    if len(sys.argv) < 2:
        print("Usage: python version_utils.py <command> [repository]")
        print("Commands:")
        print("  get-version          - Get version from pyproject.toml")
        print("  get-pypi-latest      - Get latest version from PyPI/TestPyPI")
        print(
            "  get-next-alpha       - Get next alpha version (requires base version as input)"
        )
        print(
            "  check-exists         - Check if version exists on PyPI/TestPyPI (requires version as input)"
        )
        print("")
        print("Repository (optional): pypi | testpypi (default: pypi)")
        sys.exit(1)

    command = sys.argv[1]
    repository = sys.argv[2] if len(sys.argv) > 2 else "pypi"

    if repository not in ["pypi", "testpypi"]:
        print(
            f"Error: Invalid repository '{repository}'. Must be 'pypi' or 'testpypi'",
            file=sys.stderr,
        )
        sys.exit(1)

    if command == "get-version":
        print(get_version_from_pyproject())
    elif command == "get-pypi-latest":
        print(get_latest_pypi_version(repository=repository))
    elif command == "get-next-alpha":
        base_version = (
            input().strip() if not sys.stdin.isatty() else get_version_from_pyproject()
        )
        print(get_next_alpha_version(base_version, repository=repository))
    elif command == "check-exists":
        version = input().strip() if not sys.stdin.isatty() else ""
        if not version:
            print("Error: Version required", file=sys.stderr)
            sys.exit(1)
        exists = version_exists_on_pypi(version, repository=repository)
        print("true" if exists else "false")
        sys.exit(0 if not exists else 1)
    else:
        print(f"Unknown command: {command}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
