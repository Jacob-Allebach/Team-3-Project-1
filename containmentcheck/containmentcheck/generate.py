"""Generate random data values and collections as containers."""

import random


def generate_random_number(maximum: int, exceed: bool) -> int:
    """generate a random number that is either up to the maximum
    or exceeding it by one, depending on the input parameter values"""
    if exceed:
        return maximum + 1
    return random.randrange(maximum)


def generate_random_container(
    size: int,
    maximum: int,
    make_tuple: bool = False,
):
    """generate a list of random values for a specific size
    and with a number up to a specific maximum"""
    random_list = []
    for i in range(size):
        random_list.append(generate_random_number(maximum, False))
    # convert the list to a tuple if this was requested
    if make_tuple:
        return tuple(random_list)
    return random_list
