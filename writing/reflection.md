# Containment Checking

## Table of Contents

<!---toc start-->

* [Containment Checking](#containment-checking)
  * [Table of Contents](#table-of-contents)
  * [Jacob Allebach](#jacob-allebach)
  * [Re-type the sentence "I adhered to the Allegheny College Honor Code while completing this project."](#re-type-the-sentence-i-adhered-to-the-allegheny-college-honor-code-while-completing-this-project)
  * [Program Output](#program-output)
    * [Report at least two examples of program output from when you can the `systemsense` program](#report-at-least-two-examples-of-program-output-from-when-you-can-the-systemsense-program)
      * [First output from running the `systemsense` program](#first-output-from-running-the-systemsense-program)
      * [Second output from running the `systemsense` program](#second-output-from-running-the-systemsense-program)
    * [Report at least five examples of program output to demonstrate that your `containmentcheck` program works correctly](#report-at-least-five-examples-of-program-output-to-demonstrate-that-your-containmentcheck-program-works-correctly)
      * [First output from running the `containmentcheck` program](#first-output-from-running-the-containmentcheck-program)
      * [Second output from running the `containmentcheck` program](#second-output-from-running-the-containmentcheck-program)
      * [Third output from running the `containmentcheck` program](#third-output-from-running-the-containmentcheck-program)
      * [Fourth output from running the `containmentcheck` program](#fourth-output-from-running-the-containmentcheck-program)
      * [Fifth output from running the `containmentcheck` program](#fifth-output-from-running-the-containmentcheck-program)
  * [Experiment Design](#experiment-design)
  * [Research Questions](#research-questions)
  * [Data Tables](#data-tables)
  * [Performance Analysis](#performance-analysis)
  * [Source Code](#source-code)
    * [Pick a segment of source code in `containmentcheck` and describe in detail how it works](#pick-a-segment-of-source-code-in-containmentcheck-and-describe-in-detail-how-it-works)
    * [Describe in detail how the `containmentcheck` program is organized into modules](#describe-in-detail-how-the-containmentcheck-program-is-organized-into-modules)
  * [Professional Development](#professional-development)
    * [What is challenging about designing an experiment to evaluate a collection's performance?](#what-is-challenging-about-designing-an-experiment-to-evaluate-a-collections-performance)
    * [How do the empirical results suggest that you don't yet know the entire story about the performance of containment checking?](#how-do-the-empirical-results-suggest-that-you-dont-yet-know-the-entire-story-about-the-performance-of-containment-checking)
    * [Take Home Points](#take-home-points)

<!---toc end-->

## Jacob Allebach

## Re-type the sentence "I adhered to the Allegheny College Honor Code while completing this project."

I adhered to the Allegheny College Honor Code while completing this project.

**IMPORTANT:** If you do not type the required sentence then the course
instructor will not know that you adhered to the Allegheny College Honor Code
while completing the project.

## Program Output

### Report at least two examples of program output from when you can the `systemsense` program

#### First output from running the `systemsense` program

```console
Displaying System Information

╭────────────────────────────────────────────────────────── System Information ──────────────────────────────────────────────────────────╮
│ ╭──────────────────┬─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮ │
│ │ System Parameter │ Parameter Value                                                                                                 │ │
│ ├──────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤ │
│ │ battery          │ 69.34% battery life remaining, 2:45:37 seconds remaining                                                        │ │
│ │ cpu              │ x86_64                                                                                                          │ │
│ │ cpucores         │ 4 cores                                                                                                         │ │
│ │ cpufrequencies   │ Min: 0.0 Mhz, Max: 0.0 Mhz                                                                                      │ │
│ │ datetime         │ 2024-02-07 23:39:56.506737                                                                                      │ │
│ │ disk             │ Using 9.36 GB of 1006.85 GB                                                                                     │ │
│ │ hostname         │ DESKTOP-DVJG7I0                                                                                                 │ │
│ │ memory           │ Using 0.50 GB of 3.74 GB                                                                                        │ │
│ │ platform         │ Linux-5.15.133.1-microsoft-standard-WSL2-x86_64-with-glibc2.38                                                  │ │
│ │ pythonversion    │ 3.11.6                                                                                                          │ │
│ │ runningprocesses │ 38                                                                                                              │ │
│ │ swap             │ Using 0.00 GB of 1.00 GB                                                                                        │ │
│ │ system           │ Linux                                                                                                           │ │
│ │ systemload       │ Average Load: 0.11, CPU Utilization: 2.85%                                                                      │ │
│ │ virtualenv       │ /mnt/c/Users/Okz/CS202Repositories/computer-science-202-algorithm-analysis-project-1-Jacob-Allebach/systemsens… │ │
│ ╰──────────────────┴─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯ │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

Displaying Benchmark Results

╭────────────────────────────────────────────────────────── Benchmark Results ───────────────────────────────────────────────────────────╮
│ ╭────────────────┬───────────────────────────────────────────────────────────────╮                                                     │
│ │ Benchmark Name │ Benchmark Results (sec)                                       │                                                     │
│ ├────────────────┼───────────────────────────────────────────────────────────────┤                                                     │
│ │ addition       │ [0.6892663470061962, 0.7320733450033003, 0.7459980429994175]  │                                                     │
│ │ concatenation  │ [4.564174165992881, 4.727627282001777, 6.895602928008884]     │                                                     │
│ │ exponentiation │ [4.78881434899813, 4.472210609004833, 4.190871048995177]      │                                                     │
│ │ multiplication │ [0.6183006530045532, 0.5947689549939241, 0.6935934530047234]  │                                                     │
│ │ rangelist      │ [0.3362526739947498, 0.2809464790043421, 0.25239088099624496] │                                                     │
│ ╰────────────────┴───────────────────────────────────────────────────────────────╯                                                     │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

#### Second output from running the `systemsense` program

```console
Displaying System Information

╭────────────────────────────────────────────────────────── System Information ──────────────────────────────────────────────────────────╮
│ ╭──────────────────┬─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮ │
│ │ System Parameter │ Parameter Value                                                                                                 │ │
│ ├──────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤ │
│ │ battery          │ 67.48% battery life remaining, 2:15:46 seconds remaining                                                        │ │
│ │ cpu              │ x86_64                                                                                                          │ │
│ │ cpucores         │ 4 cores                                                                                                         │ │
│ │ cpufrequencies   │ Min: 0.0 Mhz, Max: 0.0 Mhz                                                                                      │ │
│ │ datetime         │ 2024-02-07 23:42:28.055113                                                                                      │ │
│ │ disk             │ Using 9.36 GB of 1006.85 GB                                                                                     │ │
│ │ hostname         │ DESKTOP-DVJG7I0                                                                                                 │ │
│ │ memory           │ Using 0.51 GB of 3.74 GB                                                                                        │ │
│ │ platform         │ Linux-5.15.133.1-microsoft-standard-WSL2-x86_64-with-glibc2.38                                                  │ │
│ │ pythonversion    │ 3.11.6                                                                                                          │ │
│ │ runningprocesses │ 40                                                                                                              │ │
│ │ swap             │ Using 0.00 GB of 1.00 GB                                                                                        │ │
│ │ system           │ Linux                                                                                                           │ │
│ │ systemload       │ Average Load: 0.19, CPU Utilization: 4.64%                                                                      │ │
│ │ virtualenv       │ /mnt/c/Users/Okz/CS202Repositories/computer-science-202-algorithm-analysis-project-1-Jacob-Allebach/systemsens… │ │
│ ╰──────────────────┴─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯ │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

Displaying Benchmark Results

╭────────────────────────────────────────────────────────── Benchmark Results ───────────────────────────────────────────────────────────╮
│ ╭────────────────┬────────────────────────────────────────────────────────────────╮                                                    │
│ │ Benchmark Name │ Benchmark Results (sec)                                        │                                                    │
│ ├────────────────┼────────────────────────────────────────────────────────────────┤                                                    │
│ │ addition       │ [0.7081943850062089, 0.8368257280089892, 0.8435725359886419]   │                                                    │
│ │ concatenation  │ [4.5653230079915375, 4.928292098004022, 7.408778482989874]     │                                                    │
│ │ exponentiation │ [4.1762541019998025, 9.526995086998795, 5.247003837997909]     │                                                    │
│ │ multiplication │ [0.5859761659958167, 0.5746483489929233, 0.5874316489935154]   │                                                    │
│ │ rangelist      │ [0.25626958400243893, 0.2563550850027241, 0.26474939299805555] │                                                    │
│ ╰────────────────┴────────────────────────────────────────────────────────────────╯                                                    │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### Report at least five examples of program output to demonstrate that your `containmentcheck` program works correctly

Document and justify your choice for all of the experiment parameters

Make sure that at least one of the outputs show the `help` menu

#### First output from running the `containmentcheck` program

Command: `poetry run containmentcheck --help`

Output:

```console
 Usage: containmentcheck [OPTIONS]

 Conduct an experiment to measure the performance of containment checking.

╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --size                                 INTEGER                          [default: 5]                                                   │
│ --maximum                              INTEGER                          [default: 25]                                                  │
│ --exceed                --no-exceed                                     [default: no-exceed]                                           │
│ --approach                             [list|set|tuple]                 [default: ContainmentCheckApproach.list]                       │
│ --install-completion                   [bash|zsh|fish|powershell|pwsh]  Install completion for the specified shell. [default: None]    │
│ --show-completion                      [bash|zsh|fish|powershell|pwsh]  Show completion for the specified shell, to copy it or         │
│                                                                         customize the installation.                                    │
│                                                                         [default: None]                                                │
│ --help                                                                  Show this message and exit.                                    │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```

Running the help command to show the possible valid inputs.

#### Second output from running the `containmentcheck` program

Command: `poetry run containmentcheck --size 32000000 --maximum 50000000 --approach list`

Output:

```console
Conducting an experiment to measure the performance of containment checking!
        Type of the data container: list
        Size of the data container: 32000000
        Maximum value for a number in the data container: 50000000
        Should the value to search for exceed the maximum number? No

Total time for running  10 runs in 3 benchmark campaigns:
[0.5869363710080506, 0.35052407399052754, 0.4997580060007749]

Average time for running  10 runs in 3 benchmark campaigns:
[0.058693637100805066, 0.03505240739905276, 0.04997580060007749]
```

A command to test the list approach with the recommended values from the readme.

#### Third output from running the `containmentcheck` program

Command: `poetry run containmentcheck --size 32000000 --maximum 50000000 --approach tuple`

Output:

```console
Conducting an experiment to measure the performance of containment checking!
        Type of the data container: tuple
        Size of the data container: 32000000
        Maximum value for a number in the data container: 50000000
        Should the value to search for exceed the maximum number? No

Total time for running  10 runs in 3 benchmark campaigns:
[0.1781485520041315, 0.17819595300534274, 0.14570254299906082]

Average time for running  10 runs in 3 benchmark campaigns:
[0.01781485520041315, 0.017819595300534275, 0.014570254299906082]
```

A command to test the tuple approach with the recommended values from the readme.

#### Fourth output from running the `containmentcheck` program

Command: `poetry run containmentcheck --size 32000000 --maximum 50000000 --approach set`

Output:

```console
Conducting an experiment to measure the performance of containment checking!
        Type of the data container: set
        Size of the data container: 32000000
        Maximum value for a number in the data container: 50000000
        Should the value to search for exceed the maximum number? No

Total time for running  10 runs in 3 benchmark campaigns:
[99.45688242198958, 104.59604528799537, 100.7573357650108]

Average time for running  10 runs in 3 benchmark campaigns:
[9.945688242198958, 10.459604528799536, 10.07573357650108]
```

A command to test the set approach with the recommended values from the readme.

#### Fifth output from running the `containmentcheck` program

Command: `poetry run containmentcheck --size 32000000 --maximum 50000000 --approach list --exceed`

Output:

```console
Conducting an experiment to measure the performance of containment checking!
        Type of the data container: list
        Size of the data container: 32000000
        Maximum value for a number in the data container: 50000000
        Should the value to search for exceed the maximum number? Yes

Total time for running  10 runs in 3 benchmark campaigns:
[3.536845541995717, 3.571743189007975, 3.796420452010352]

Average time for running  10 runs in 3 benchmark campaigns:
[0.35368455419957173, 0.35717431890079754, 0.3796420452010352]
```

A command to test the list approach with default values and exceed enabled.

## Experiment Design

Explain the setup for your experiment that you plan to run to
characterize the performance of the different configurations of containment
checking algorithms. Remember, a containment check determines whether or not a
specified value exists inside of some type of data container! For instance, you
should consider the following parameters as a part of your experiment:

- The data container: `set`, `list`, and `tuple`
- The size of the data container: small values (e.g., 1 million numbers) to big
  values (e.g., 32 million numbers)
- Whether or not the value that it being searched for is in the list
- The maximum value of the numbers that are inside of the data container

You must justify every part of your experiment design and then furnish
output examples to demonstrate that your program generates correct data!

You must meet in person with the course instructor to discuss the design
of your experiment before you conduct the experiment itself.

### My Experiment

The experiment I'm running on this program is testing each approach type (list, tuple, set)
and seeing how much the maximum number, size, and non-existent values affect
the speed of the algorithms.

The values used for the control case will be a container size of 1000000 (1 million), a
maximum number of 5000000 (5 million) and `exceed set to false`. This will serve as the
baseline and comparison point to all the rest of the tests.

The values used for the maximum number tests will be 100 (1 hundred) as the small value
and 2000000000 (2 billion) as the large value. Additionally, the size of the container
for all of this portion will be 1000000 (1 million) and `exceed` will be false in order
to keep the rest of the variables consistent.

The values used for the container size tests will be 10000 (10 thousand) as the small
value and 10000000 (10 million) as the large value. The maximum number will be set to
5000000 (5 million) and `exceed` will be false for all tests to keep those variables
consistent.

For the non-existent values tests, the only variable that will change is `exceed` being
set to false and true. The size will be set to 1000000 (1 million) and the maximum number
will be 5000000 (5 million) to keep those variables consistent throughout these tests.

## Research Questions

Clearly state at least three research questions that you want to ask and
answer by using the `containmentcheck` program. You should provide the research
questions in a list that starts with "RQ" and ends with a question mark. Please
see the engineering effort about the intersection algorithms for examples of
research questions that the course instructor created for that project.

You must meet in person with the course instructor to discuss the research
questions before you conduct the experiment itself.

### RQ

* How much does a larger maximum number value in the container affect the speed of the `in` operator compared to a small number?
* How much does a large container size affect the speed of the `in` operator compared to a small number?
* How much is speed affected when using the `in` operator to search for a value that is not in the container?

## Data Tables

Use Markdown to provide one or more data tables that summarize the results
from running the `containmentcheck` program in different configurations. You
should provide enough data tables and output values to ensure that you can
answer all of your research questions and use the empirical results to classify
the likely worst-case time complexity of each of the algorithms.

You must meet in person with the course instructor to discuss the analysis
of your data before you submit the final version of your assignment.

Approach | Maximum Value | Container Size | Exceed | Time 1 | Time 2 | Time 3 |
---------|---------------|----------------|--------|--------|--------|--------|
 List | 5,000,000 | 1,000,000 | False | 0.10627889399995638 | 0.11102569500002346 | 0.11526079300000447 |
 Tuple| 5,000,000 | 1,000,000 | False | 0.1016628940000146 | 0.09177049400000215 | 0.09299969400001373 |
 Set  | 5,000,000 | 1,000,000 | False | 1.3523091119999435 | 1.3616508119999935 | 1.274951912000006 |
 List | 100 | 1,000,000 | False | 1.4400000054592965e-05 | 3.999999989900971e-06 | 2.499999936844688e-06 |
 Tuple| 100 | 1,000,000 | False | 7.699999969190685e-06 | 3.000000106112566e-06 | 2.900000026784255e-06 |
 Set  | 100 | 1,000,000 | False | 0.13275989500016294 | 0.11513739599990913 | 0.12016179600004762 |
 List | 2,000,000,000 | 1,000,000 | False | 0.18887618799999473 | 0.18629048899992995 | 0.1805565890001617 |
 Tuple| 2,000,000,000 | 1,000,000 | False | 0.15915989099994476 | 0.1423708910001551 | 0.1351233919999686 |
 Set  | 2,000,000,000 | 1,000,000 | False | 1.4009660230001373 | 1.3648533220000445 | 1.3015629210001407 |
 List | 5,000,000 | 10,000 | False | 0.0020670999999765627 | 0.0011968999999680818 | 0.0015773000000081083 |
 Tuple| 5,000,000 | 10,000 | False | 0.0011167000000114058 | 0.00109359999987646 | 0.0008669999999710853 |
 Set  | 5,000,000 | 10,000 | False | 0.005273600000009537 | 0.0041636999999354884 | 0.004012700999965091 |
 List | 5,000,000 | 10,000,000 | False | 1.1126290170000175 | 0.9291830150000351 | 0.8701489130000937 |
 Tuple| 5,000,000 | 10,000,000 | False | 0.2895830060001572 | 0.2964557049999712 | 0.2836229059998914 |
 Set  | 5,000,000 | 10,000,000 | False | 22.32453848099999 | 22.730821889000026 | 22.534443623000016 |
 List | 5,000,000 | 1,000,000 | True | 0.10637318300018705 | 0.12087098000006335 | 0.12409078100017723 |
 Tuple| 5,000,000 | 1,000,000 | True | 0.09330711600000541 | 0.09802781700000196 | 0.10081401699994785 |
 Set  | 5,000,000 | 1,000,000 | True | 1.3530289230000108 | 1.284104601999843 | 1.3516725229999338 |

## Performance Analysis

Provide at least three paragraphs that explain which containment checking
algorithm is fastest, by how much it is faster, and how you knew that it was
faster, referencing the data in the aforementioned command outputs and the data
tables to support your response. You should make sure that you answer each of
the at least three research questions that you posed in a previous section.

You must meet in person with the course instructor to discuss the analysis
of your data before you submit the final version of your assignment.

Make sure that your responses explain WHY certain configurations are faster!
It is not sufficient to ONLY explain WHICH configuration is faster!

### Analysis of My Experiment

For the control test, the list approach averaged about 0.11 seconds and the tuple
approach hovered around 0.095 seconds, whereas the set approach settled around 1.3 seconds.
A few reasons for this could be that the set is unordered, whereas the list and tuple are
both ordered and can have duplicates, so searching through them is more linear.
Additionally, the function that searches through a set takes a list as an input and
**converts** it to a set before searching it, meaning it has to use extra time and processing
power to convert it before the search happens.

Changing the maximum value able to be generated affected the programs' speeds quite a bit.
The small value of 100 decreased times drastically, with the list and tuple approaches
performing thousands of times better than the control tests. The set approach only performed
about ten times better than its control counterpart, but its still quite significant of an
improvement. The large value of 2,000,000,000 did increase the times of each approach type,
but not by a massive amount like the small value did. The list and tuple approaches both
performed only about 50%-80% slower with the large value and the set performed almost exactly
the same as the control test. I think the reasoning behind these results is that when the
maximum value is made extremely small, there's a much higher likelihood that the random number
being searched for will show up earlier in the list or tuple as there are much fewer possible
numbers to be generated overall. As far as the set goes, it would stand to reason that there
being fewer numbers in the list that gets converted into the set would mean that there are
much fewer numbers for the set to process when being searched through, thus increasing the
speed of that search as well. On the other hand, the times not increasing drastically when
using large numbers probably has to do with the larger amount of variance the values will have.
In the control test, the maximum value is set to 5,000,000 with a container size of 1,000,000,
resulting in about a 4/5 chance that the value being searched for is not present in the container.
This means that there will always be at least 4,000,000 values that are not represented in the
resulting container, making it unlikely that the randomly generated number to search for will
be in the generated container. For the large maximum value of 2,000,000,000, it increases the
chances of the random search value not being in the container to about 1,999/2,000. Because
the container size is not changing, it means that instead of the search taking drasically
longer, it's just forced to search through the entire list or tuple more often. This is why
the set stays about the same as the control for the large value because the set contains
about the same number of values to hash either way.

For the second significant discovery from the data, I found that changing the data container
size greatly affects the speeds of the searches. For the small size of 10,000, every data
container performed the search faster, with the tuple being slightly faster than the list
and the set only being about 5 times slower than those. Accordingly, the large container size
of 10,000,000 slowed down the searches by quite a bit, though I think it's important to note
that the tuple wasn't slowed down nearly as much as the list and set. The list performed about
10 times worse than the control test, and the set was worse by about 20 times, but the tuple
was only twice as slow as the control, making it far and away the fastest container at searching
large data sets. I think the most convincing argument for why it's so much faster than the others
is that the list and set are both mutable data types while the tuple is immutable. Becuase of the
tuple's immutability, it doesn't have to worry about the data within the container changing during
the search, meaning it can parse through a larger group of values much faster than the list and
set.

Lastly, and somewhat least, is the topic of how non-existent values affect search time. The reason
I imply this one is the least important is that the result isn't all that striking. For every data
container type, the searches performed almost exactly the same as the control test when `exceed`
was set to true. I think the reasoning for this is rather similar to the idea I was discussing in
the second paragraph above, which is that the control test already has about a 4/5 chance that the
value being searched for doesn't exist in the container. This means that there's only about a 1/5
chance the control test will be any different from a test where `exceed` is made true, as it's
already likely that the value being searched for will not be in the container. Thus, not much can
be discovered about this portion of the data.

## Source Code

### Pick a segment of source code in `containmentcheck` and describe in detail how it works

Use a fenced code block to provide the requested source code
Write at least one paragraph to explain the request source code

```python
def generate_random_number(maximum: int, exceed: bool) -> int:
    """generate a random number that is either up to the maximum
    or exceeding it by one, depending on the input parameter values"""
    if exceed:
        return maximum+1
    return random.randrange(maximum)
```

This chunk of code is from the file `generate.py` and is the full code of the function titled
`generate_random_number`. This function serves to generate a random number based on the two
inputs it is given. The first input to the function is `maximum`, which represents the number
value that will be used as the upper bounds to the number generation. The second input is
`exceed`, and this boolean determines whether or not the output will be within the bounds of
`maximum` or greater than it. Moving on the code within the function, it's not too advanced,
with only one if statement and two return statements. The if statement checks for if `exceed`
is set to true. If it is, then the function returns an integer 1 larger than `maximum`. The
purpose of this is to provide a value that will not be in the list generated by the code
previously. If `exceed` is false, however, then the function will return a random value
between 0 and `maximum`.

### Describe in detail how the `containmentcheck` program is organized into modules

There are many different files that make up the entire `containmentcheck` program. Going in
alphabetical order, the `analyze.py` file is used to calculate the averages for each value
in a given list by dividing each one by the data count provided. The `approach.py` file is
used to establish the `ContainmentCheckApproach` class, allowing quick conversions from the
strings `list`, `tuple`, and `set` to their actual data container counterparts and vice-versa.
Next, the `containment.py` file actually performs the searches, having three different
functions that each perform a search for one data container type. The `generate.py` file is
specifically for generating random values and producing containers filled with those random
values. Skipping over the main file for a second, the `util.py` file is exclusively used
to convert a boolean into the string `Yes` for true and `No` for false. Lastly, the `main.py`
file puts it all together, by utilizing the various files to construct data containers according
to the given inputs before running a few benchmark tests on the search functionalities and
outputting that time data.

## Professional Development

### What is challenging about designing an experiment to evaluate a collection's performance?

Provide a one-paragraph response that answers this question in your own words.

I think the most challenging part about designing an experiment is trying to find the exact
values that will provide the best insight into how a given variable affects the collection's
performance. Without knowing how to structure an experiment going into this one made it
somewhat difficult to judge if the values I was choosing were going to prove effective at
impacting the performance of searching through containers. Although I think I could have
picked better values, I don't think I was that far off in what I set out to find, and the
resulting conclusions still provided a bit of new insight on how these containers function.

### How do the empirical results suggest that you don't yet know the entire story about the performance of containment checking?

Provide a one-paragraph response that answers this question in your own words.

Even just with the tests that I ran during my experiment, it's very clear that the data
is quite variable in what the exact numbers will be output and how fast the containment
checking will be. Despite the large amount of variance, I think the conclusions I came
to helped bridge the gap slightly between not knowing and understanding, even if only
a little..

### Take Home Points

Provide a two to three sentence statement about the key takeaways from
conducting this experiment. Please note that the course instructor will display
some student takeaways on the course web site and use them to facilitate
follow-on class discussions.

My biggest takeaway from this entire experience is that it's important to know what kinds
of inputs would be considered large, small, or standard for whatever task you're performing.
Having that kind of information is crucial in being able to come up with good values to test
to make sure the experiment is being performed correctly.
