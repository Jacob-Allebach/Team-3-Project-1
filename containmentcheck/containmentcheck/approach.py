"""Configuration of the benchmarking tool with an approach."""

from enum import Enum

# Define the name for the approach for performing containment checking of structured types


class ContainmentCheckApproach(str, Enum):
    """Defines the different container types"""

    list = "list"
    set = "set"
    tuple = "tuple"
