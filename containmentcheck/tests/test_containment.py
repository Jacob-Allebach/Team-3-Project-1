"""Test cases for the containment module."""

from containmentcheck.containment import (
    containment_check_list,
    containment_check_set,
    containment_check_tuple,
)

# Add test cases to ensure:
# - correctness of the functions in the module under test
# - coverage of the source code of the functions in the module under test


def test_containment_check_list_true():
    assert containment_check_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 5) is True


def test_containment_check_list_false():
    assert containment_check_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 0) is False


def test_containment_check_tuple_true():
    assert containment_check_tuple((1, 2, 3, 4, 5, 6, 7, 8, 9), 5) is True


def test_containment_check_tuple_false():
    assert containment_check_tuple((1, 2, 3, 4, 5, 6, 7, 8, 9), 0) is False


def test_containment_check_set_true():
    assert containment_check_set([1, 2, 3, 4, 5, 6, 7, 8, 9], 5) is True


def test_containment_check_set_false():
    assert containment_check_set([1, 2, 3, 4, 5, 6, 7, 8, 9], 0) is False
