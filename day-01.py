import re
import sys
from collections import defaultdict

import aocd

# Set the day and year
DAY = "01"
YEAR = "2023"


def get_input(path, part=1):
    """Load the data from the file"""

    # Open the file
    if "test" in path:
        file_name = f"{path}/day-{DAY}-{part}.txt"
    else:
        file_name = f"{path}/day-{DAY}.txt"

    with open(file_name, "r") as f:
        if part == 1:
            values = [re.sub(r"[^0-9]", "", line.strip()) for line in f.readlines()]
        else:
            values = [
                re.findall(
                    r"(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]+))",
                    line.strip(),
                )
                for line in f.readlines()
            ]

    return values


def part_1(path, submit):
    """Part 1/Star 1"""

    # Get the data
    data = get_input(path)

    # Complete the task
    answer = sum([int(f"{value[0]}{value[-1]}") for value in data])

    # Print out the response
    print(f"Task 1 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="a", day=int(DAY), year=int(YEAR))


def part_2(path, submit):
    """Part 2/Star 2"""

    # Get the data
    data = get_input(path, part=2)
    print(data)

    options = defaultdict(
        int,
        {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        },
    )

    # Replace the words
    def replace_digit(word):
        try:
            return str(int(word))
        except:
            return options[word]

    data = ["".join([replace_digit(i) for i in value]) for value in data]

    # Add the values
    answer = sum([int(f"{value[0]}{value[-1]}") for value in data])

    # Print out the response
    print(f"Task 2 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="b", day=int(DAY), year=int(YEAR))


if __name__ == "__main__":
    """
    Run using e.g.
        `python day-01.py -test`
        `python day-01.py`
        `python day-01.py -test -2`
        `python day-01.py -2`
        `python day-01.py -test -both`
        `python day-01.py -both`
        `python day-01.py -submit`
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
