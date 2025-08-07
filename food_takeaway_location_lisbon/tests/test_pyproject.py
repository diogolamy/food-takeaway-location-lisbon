"""
Test the pyproject.toml file
"""


def test_import_main_package():
    try:
        import food_takeaway_location_lisbon
    except ImportError:
        assert False, "Failed to import food_takeaway_location_lisbon"
