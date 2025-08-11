"""
Unit tests for the pyproject.toml file.

This is unusual in real-world projects, but useful here to ensure
that our project configuration is correct while learning.
"""

from pathlib import Path
from importlib.metadata import PackageNotFoundError, version
import toml
import pytest
import pandas as pd
import numpy as np
import geopandas as gpd
import folium
import matplotlib


# Define project root directory
PROJECT_DIR = Path(__file__).resolve().parents[2]


def test_dependencies_installed():
    """
    Test that key dependencies from pyproject.toml are installed
    and have accessible versions.
    """
    deps = (
        pd.__version__,
        np.__version__,
        gpd.__version__,
        folium.__version__,
        matplotlib.__version__,
    )
    assert len(deps) == 5, "Some dependencies are missing or not imported correctly."


def test_pyproject_metadata():
    """
    Test that pyproject.toml contains correct metadata for this project.
    """
    pyproject_path = PROJECT_DIR / "pyproject.toml"
    assert pyproject_path.exists(), f"pyproject.toml file not found at {pyproject_path}"

    pyproject = toml.load(pyproject_path)

    # Check basic metadata
    assert pyproject["project"]["name"] == "food-takeaway-location-lisbon"
    assert pyproject["project"]["version"] == "0.1.0"
    assert "Identify the most strategic location" in pyproject["project"]["description"]

    # Ensure author is correctly set
    authors = pyproject["project"]["authors"]
    assert any(
        author["name"].startswith("diogolamy") or "diogolamy" in author["email"]
        for author in authors
    ), "Your author details are missing or incorrect in pyproject.toml."


def test_package_installed():
    """
    Test that the project package is installed with the correct version.
    """
    try:
        installed_version = version("food-takeaway-location-lisbon")
    except PackageNotFoundError:
        pytest.fail(
            "The package is not installed. "
            "If installed, check the [project.name] in pyproject.toml."
        )

    assert installed_version == "0.1.0", (
        f"Expected version 0.1.0 but found {installed_version}. "
        "Check the version in pyproject.toml."
    )
