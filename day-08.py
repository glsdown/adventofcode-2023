import sys
from math import lcm

import aocd

# Set the day and year
DAY = "08"
YEAR = "2023"


def get_input(path, part=1):
    """Load the data from the file"""

    # Get the file name
    if "test" in path:
        file_name = f"{path}/day-{DAY}-{part}.txt"
    else:
        file_name = f"{path}/day-{DAY}.txt"

    # Open the file
    with open(file_name, "r") as f:
        values = [line.strip() for line in f.readlines()]

    map_direction = {
        "L": 0,
        "R": 1,
    }
    instructions = [map_direction[i] for i in values[0].strip()]

    keys = {
        v.split("=")[0].strip(): [
            i.strip()
            for i in v.split("=")[1].replace("(", "").replace(")", "").split(",")
        ]
        for v in values[2:]
    }

    return instructions, keys


def part_1(path, submit):
    """Part 1/Star 1"""

    # Get the data
    instructions, keys = get_input(path)

    print(instructions, keys)

    current = "AAA"
    answer = 0

    while current != "ZZZ":
        current = keys[current][instructions[answer % len(instructions)]]
        answer += 1

    # Print out the response
    print(f"Task 1 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="a", day=int(DAY), year=int(YEAR))


def part_2(path, submit):
    """Part 2/Star 2"""

    # Get the data
    instructions, keys = get_input(path, part=2)

    current = [i for i in keys if i[-1] == "A"]
    answers = [0 for i in current]

    for i in range(len(current)):
        while current[i][-1] != "Z":
            current[i] = keys[current[i]][instructions[answers[i] % len(instructions)]]
            answers[i] += 1

    answer = lcm(*answers)

    # Print out the response
    print(f"Task 2 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="b", day=int(DAY), year=int(YEAR))


if __name__ == "__main__":
    """
    Run using e.g.
        `python day-08.py -test`
        `python day-08.py`
        `python day-08.py -submit`
        `python day-08.py -test -2`
        `python day-08.py -2`
        `python day-08.py -test -both`
        `python day-08.py -both`
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
