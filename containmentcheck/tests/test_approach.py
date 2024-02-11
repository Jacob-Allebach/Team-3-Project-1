"""Tests for the approach module."""

from containmentcheck.approach import ContainmentCheckApproach

# Add test cases to ensure:
# - correctness of the functions in the module under test
# - coverage of the source code of the functions in the module under test


def test_approach_list():
    assert ContainmentCheckApproach.list.value == "list"


def test_approach_tuple():
    assert ContainmentCheckApproach.tuple.value == "tuple"


def test_approach_set():
    assert ContainmentCheckApproach.set.value == "set"
