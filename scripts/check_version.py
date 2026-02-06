#!/usr/bin/env python3
"""
Check if a version already exists on PyPI.
This script is specifically designed for the GitHub Actions workflow.
"""

import sys

from version_utils import version_exists_on_pypi


def main() -> None:
    """Check if the given version exists on PyPI or TestPyPI."""
    if len(sys.argv) < 3:
        print("Usage: python check_version.py <version> <release_type> [repository]")
        print("Repository (optional): pypi | testpypi (default: pypi)")
        sys.exit(1)

    version = sys.argv[1]
    release_type = sys.argv[2]
    repository = sys.argv[3] if len(sys.argv) > 3 else "pypi"

    if repository not in ["pypi", "testpypi"]:
        print(f"Error: Invalid repository '{repository}'. Must be 'pypi' or 'testpypi'")
        sys.exit(1)

    repo_name = "TestPyPI" if repository == "testpypi" else "PyPI"
    print(f"Checking if version {version} ({release_type}) exists on {repo_name}...")

    exists = version_exists_on_pypi(version, repository=repository)

    if exists:
        print(f"ERROR: Version {version} already exists on {repo_name}!")
        if release_type == "prerelease":
            print(
                "This should not happen for prerelease versions. Please check the alpha version logic."
            )
        else:
            print("Please bump the version in pyproject.toml before publishing.")
        sys.exit(1)
    else:
        print(f"Version check passed: {version} does not exist on {repo_name}")


if __name__ == "__main__":
    main()
