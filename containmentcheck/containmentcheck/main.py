"""Perform an experiment to study efficiency of containment checking for collections."""

import timeit

import typer
from rich.console import Console

from containmentcheck.analyze import calculate_average_values
from containmentcheck.approach import ContainmentCheckApproach
from containmentcheck.containment import (
    containment_check_list,
    containment_check_set,
    containment_check_tuple,
)
from containmentcheck.generate import (
    generate_random_container,
    generate_random_number,
)
from containmentcheck.util import human_readable_boolean

# create a Typer object to support the command-line interface
cli = typer.Typer()

# create a console for rich text output
console = Console()


def perform_containment_check_benchmark(
    containment_check_lambda, runs: int = 10, repeats: int = 3
) -> None:
    """Run an experiment using the timeit package for the specific function."""
    # use the timeit module to evaluate performance with the current configuration
    # reference to learn about the timeit module:
    # https://docs.python.org/3/library/timeit.html
    # key insights:
    # --> each benchmark run will have a total of number_runs and timeit will report the total across number_runs
    # --> each of the entire benchmark run will be repeated a total of number_repeats times
    # Read the reference for using the lambda function:
    # https://stackoverflow.com/questions/5086430/how-to-pass-parameters-of-a-function-when-using-timeit-timer
    execution_times = timeit.Timer(containment_check_lambda).repeat(
        repeat=repeats, number=runs
    )
    # display the results of the benchmarking campaign
    console.print(
        f":abacus: Total time for running {runs} runs in {repeats} benchmark campaigns:"
    )
    console.print(execution_times)
    console.print()
    console.print(
        f":abacus: Average time for running {runs} runs in {repeats} benchmark campaigns:"
    )
    console.print(calculate_average_values(execution_times, runs))
    # see the examples of the expected output to understand how to format the benchmark results


@cli.command()
def containmentcheck(
    size: int = typer.Option(5),
    maximum: int = typer.Option(25),
    exceed: bool = typer.Option(False),
    approach: ContainmentCheckApproach = ContainmentCheckApproach.list,
) -> None:
    """Conduct an experiment to measure the performance of containment checking."""
    # create the starting data container and random number
    random_container = None
    # generate a random value that goes up to the maximum value;
    # if the value of exceed is True then generate a number beyond the maximum
    random_number = generate_random_number(maximum, exceed)
    # display diagnostic details about the configuration of the experiment
    console.print(
        ":sparkles: Conducting an experiment to measure the performance of containment checking!"
    )
    console.print(f"\tType of the data container: {approach.value}")
    console.print(f"\tSize of the data container: {size}")
    console.print(
        f"\tMaximum value for a number in the data container: {maximum}"
    )
    console.print(
        f"\tShould the value to search for exceed the maximum number? {human_readable_boolean(exceed)}"
    )
    console.print()
    # conduct an experiment for containment checking with the list data structure
    if approach.value == ContainmentCheckApproach.list:
        # generate the container of inputs consisting of random integer values
        random_container = generate_random_container(
            size, maximum, make_tuple=False
        )
        # create the containment check lambda function
        containment_check_lambda = lambda: containment_check_list(
            random_container,  # type: ignore
            random_number,
        )
        perform_containment_check_benchmark(containment_check_lambda)
    # conduct an experiment for containment checking with the tuple data structure
    elif approach.value == ContainmentCheckApproach.tuple:
        # generate the container of inputs consisting of random integer values
        random_container = generate_random_container(
            size, maximum, make_tuple=True
        )
        # create the containment check lambda function
        containment_check_lambda = lambda: containment_check_tuple(
            random_container,  # type: ignore
            random_number,
        )
        perform_containment_check_benchmark(containment_check_lambda)
    # conduct an experiment for containment checking with the set data structure
    elif approach.value == ContainmentCheckApproach.set:
        # generate the container of inputs consisting of random integer values
        random_container = generate_random_container(
            size, maximum, make_tuple=False
        )
        # generate a random value that goes up to the maximum value;
        containment_check_lambda = lambda: containment_check_set(
            random_container,  # type: ignore
            random_number,
        )
        perform_containment_check_benchmark(containment_check_lambda)
