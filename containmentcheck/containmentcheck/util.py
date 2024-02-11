"""Utility functions to support benchmarking containment in a collection."""


def human_readable_boolean(value) -> str:
    """Produce a human-readable Yes or No for a boolean value of True or False."""
    if value:
        return "Yes"
    return "No"
