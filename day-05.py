import sys

import aocd

# Set the day and year
DAY = "05"
YEAR = "2023"

OPERATIONS = [
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
]


def get_input(path):
    """Load the data from the file"""

    # Open the file
    with open(f"{path}/day-{DAY}.txt", "r") as f:
        values = f.read().split("\n\n")

    seeds = [int(i) for i in values[0].split(":")[-1].split()]
    maps = {
        v.split(" map:\n")[0]: [
            [int(j) for j in i.split()]
            for i in v.split(" map:\n")[1].strip().split("\n")
        ]
        for v in values[1:]
    }

    return seeds, maps


def map_value(value, maps):
    """Identify what the value is mapped to"""
    for dest, source, length in maps:
        if source <= value < source + length:
            return dest + (value - source)
    return value


def part_1(path, submit):
    """Part 1/Star 1"""

    # Get the data
    seeds, maps = get_input(path)

    locations = {}
    for seed in seeds:
        value = seed
        for operation in OPERATIONS:
            value = map_value(value, maps[operation])
            locations[seed] = value

    # Find the closest
    answer = min(locations.values())

    # Print out the response
    print(f"Task 1 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="a", day=int(DAY), year=int(YEAR))


def part_2(path, submit):
    """Part 2/Star 2"""

    # Get the data
    seeds, maps = get_input(path)

    all_seeds = []
    for jump in range(0, len(seeds), 2):
        all_seeds += [i for i in range(seeds[jump], seeds[jump] + seeds[jump + 1])]

    locations = {}
    for seed in all_seeds:
        value = seed
        for operation in OPERATIONS:
            value = map_value(value, maps[operation])
            locations[seed] = value

    # Find the closest
    answer = min(locations.values())

    # Print out the response
    print(f"Task 2 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="b", day=int(DAY), year=int(YEAR))


if __name__ == "__main__":
    """
    Run using e.g.
        `python day-05.py -test`
        `python day-05.py`
        `python day-05.py -submit`
        `python day-05.py -test -2`
        `python day-05.py -2`
        `python day-05.py -test -both`
        `python day-05.py -both`
    """
    # Identify the folder that the input is in
    test = "-test" in sys.argv
    if test:
        path = "input-tests"
    else:
        path = "inputs"
    # Identify if they need to submit the answer
    submit = "-test" not in sys.argv and "-submit" in sys.argv
    # Identify which one to run - 1 is default
    if "-2" in sys.argv:
        part_2(path, submit)
    elif "-both" in sys.argv:
        part_1(path, submit)
        part_2(path, submit)
    else:
        part_1(path, submit)
