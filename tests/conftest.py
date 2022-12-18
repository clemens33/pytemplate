"""pytest configuration for tests."""

import pytest


@pytest.fixture
def example_fixture():
    """Example fixture."""

    return "Hello, World fixture!"
