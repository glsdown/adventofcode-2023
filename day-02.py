
import sys
from collections import defaultdict

import aocd

# Set the day and year
DAY = "02"
YEAR = "2023"

def get_values(line):
    game, results = line.split(":")

    # Identify the game number
    game = int(game.split(" ")[-1])

    # Parse the results
    results = [dict([i[::-1] for i in w]) for w in [[w.split() for w in r.split(",")] for r in results.split(";")]]

    # Get the maximum counts reuired
    colour_dict = defaultdict(int)
    for result in results:
        for colour, count in result.items():
            if int(count) > colour_dict[colour]:
                colour_dict[colour] = int(count)

    return {
        "game": game,
        "min_required": colour_dict
    }

def get_input(path):
    """Load the data from the file"""

    # Open the file
    with open(f"{path}/day-{DAY}.txt", "r") as f:
        values = [line.strip() for line in f.readlines()]

    return values


def part_1(path, submit):
    """Part 1/Star 1"""

    # Get the data
    data = get_input(path)
    
    results = [get_values(d) for d in data]

    min_counts = {
        "red": 12,
        "green": 13,
        "blue": 14
    } 

    # Find out which games have enough of each colour
    answer = 0
    for result in results:
        if all([result["min_required"][colour] <= min_counts[colour] for colour in min_counts]):
            answer += result["game"]

    # Print out the response
    print(f"Task 1 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="a", day=int(DAY), year=int(YEAR))


def part_2(path, submit):
    """Part 2/Star 2"""

    # Get the data
    data = get_input(path)

    results = [get_values(d) for d in data]

    # Get the powers
    answer = 0 
    for result in results:
        answer += (result["min_required"]["red"] * result["min_required"]["green"] * result["min_required"]["blue"])

    # Print out the response
    print(f"Task 2 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="b", day=int(DAY), year=int(YEAR))


if __name__ == "__main__":
    """
    Run using e.g.
        `python day-02.py -test`
        `python day-02.py`
        `python day-02.py -test -2`
        `python day-02.py -2`
        `python day-02.py -test -both`
        `python day-02.py -both`
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
