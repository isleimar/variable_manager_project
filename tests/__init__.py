
# This file marks the tests directory as a Python package.

# tests/conftest.py
# Configuration file for pytest framework if additional setup is needed.

# tests/test_helpers.py
# Optional additional test utilities for the project.
# Example:
def mock_input(mocked_responses):
    """Helper function to mock multiple input calls."""
    def generator():
        for response in mocked_responses:
            yield response
    return generator().__next__

# Additional test helper methods can be defined here.