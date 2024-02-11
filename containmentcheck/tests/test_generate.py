"""Test suite for the generate module."""

from containmentcheck.generate import (
    generate_random_container,
    generate_random_number,
)

# Add test cases to ensure:
# - correctness of the functions in the module under test
# - coverage of the source code of the functions in the module under test


def test_generate_random_number():
    max = 10
    assert generate_random_number(max, False) < max


def test_generate_random_number_exceed():
    max = 10
    assert generate_random_number(max, True) > max


def test_generate_random_container_list():
    assert generate_random_container(10, 1, False) == [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ]


def test_generate_random_container_tuple():
    assert generate_random_container(10, 1, True) == (
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    )
