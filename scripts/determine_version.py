#!/usr/bin/env python3
"""
Determine the version to publish based on release type.
This script is specifically designed for the GitHub Actions workflow.
"""

import os
import sys

from version_utils import (
    get_next_alpha_version,
    get_version_from_pyproject,
    update_version_in_pyproject,
)


def main() -> None:
    """Determine version based on release type from environment or command line."""
    if len(sys.argv) < 2:
        print("Usage: python determine_version.py <release_type> [repository]")
        print("Release type: stable | prerelease")
        print("Repository (optional): pypi | testpypi (default: pypi)")
        sys.exit(1)

    release_type = sys.argv[1]
    repository = sys.argv[2] if len(sys.argv) > 2 else "pypi"

    if release_type not in ["stable", "prerelease"]:
        print(
            f"Error: Invalid release type '{release_type}'. Must be 'stable' or 'prerelease'."
        )
        sys.exit(1)

    if repository not in ["pypi", "testpypi"]:
        print(f"Error: Invalid repository '{repository}'. Must be 'pypi' or 'testpypi'")
        sys.exit(1)

    base_version = get_version_from_pyproject()
    repo_name = "TestPyPI" if repository == "testpypi" else "PyPI"

    print(f"Release type: {release_type}")
    print(f"Base version from pyproject.toml: {base_version}")
    print(f"Target repository: {repo_name}")

    if release_type == "stable":
        final_version = base_version
        print(f"Using stable version: {final_version}")
        print(f"Ensure {final_version} is the intended version in pyproject.toml")
    else:
        final_version = get_next_alpha_version(base_version, repository=repository)
        print(f"Generated prerelease version: {final_version}")

        update_version_in_pyproject(final_version)
        print(f"Updated pyproject.toml temporarily for build: {final_version}")
        print("Note: This change won't be committed to git - next run starts fresh")

    with open(os.environ.get("GITHUB_OUTPUT", "/dev/stdout"), "a") as f:
        f.write(f"version={final_version}\n")
        f.write(f"release_type={release_type}\n")


if __name__ == "__main__":
    main()
