"""Test cases for the util module."""

from containmentcheck.util import human_readable_boolean

# Add test cases to ensure:
# - correctness of the functions in the module under test
# - coverage of the source code of the functions in the module under test


def test_human_readable_boolean_true():
    assert human_readable_boolean(True) == "Yes"


def test_human_readable_boolean_false():
    assert human_readable_boolean(False) == "No"
