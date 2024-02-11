"""Analyze data values created from an experiment."""
from typing import Union


def calculate_average_values(
    data_list: Union[list[int], list[float]], data_count: int
) -> list[float]:
    """Calculate the average values for the data in the provided list"""
    data_list_averages = []
    for i in data_list:
        data_list_averages.append(i / data_count)
    return data_list_averages
