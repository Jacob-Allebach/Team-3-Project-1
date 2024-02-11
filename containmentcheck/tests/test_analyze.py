"""Test cases for the analyze module."""

from containmentcheck.analyze import calculate_average_values

# Add test cases to ensure:
# - correctness of the functions in the module under test
# - coverage of the source code of the functions in the module under test


def test_analyze():
    assert calculate_average_values([10.0, 20.0, 30.0, 40.0], 10) == [
        1.0,
        2.0,
        3.0,
        4.0,
    ]
