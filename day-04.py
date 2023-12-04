import sys
from collections import defaultdict

import aocd

# Set the day and year
DAY = "04"
YEAR = "2023"


def get_input(path):
    """Load the data from the file"""

    # Open the file
    with open(f"{path}/day-{DAY}.txt", "r") as f:
        values = [
            line.strip().split(":")[-1].strip().split("|") for line in f.readlines()
        ]

    return values


def part_1(path, submit):
    """Part 1/Star 1"""

    # Get the data
    data = get_input(path)

    # Complete the task
    answer = 0
    for winners, selected in data:
        count = set(
            [i for i in winners.strip().split(" ") if i.isdigit()]
        ).intersection(set(selected.strip().split(" ")))
        if count:
            answer += 2 ** (len(count) - 1)

    # Print out the response
    print(f"Task 1 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="a", day=int(DAY), year=int(YEAR))


def part_2(path, submit):
    """Part 2/Star 2"""

    # Get the data
    data = get_input(path)

    # Find how many winning cards there are
    winning_counts = []
    for winners, selected in data:
        count = set(
            [i for i in winners.strip().split(" ") if i.isdigit()]
        ).intersection(set(selected.strip().split(" ")))
        winning_counts.append(len(count))

    # Identify which scratch cards are added from winning cards
    scratchcards = defaultdict(int)
    for i, count in enumerate(winning_counts):
        scratchcards[i] += 1
        for j in range(1, count + 1):
            scratchcards[i + j] += 1 * scratchcards[i]

    # Find the total number of scratch cards
    answer = sum(scratchcards.values())

    # Print out the response
    print(f"Task 2 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="b", day=int(DAY), year=int(YEAR))


if __name__ == "__main__":
    """
    Run using e.g.
        `python day-04.py -test`
        `python day-04.py`
        `python day-04.py -submit`
        `python day-04.py -test -2`
        `python day-04.py -2`
        `python day-04.py -test -both`
        `python day-04.py -both`
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
