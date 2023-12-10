
import sys
from itertools import pairwise

import aocd

# Set the day and year
DAY = "09"
YEAR = "2023"


def get_input(path):
    """Load the data from the file"""

    # Open the file
    with open(f"{path}/day-{DAY}.txt", "r") as f:
        values = [[int(i.strip()) for i in line.strip().split()] for line in f.readlines()]

    return values

def find_differences(sequence):
    """Find the differences path
    """

    differences = sequence.copy()
    new_sequences = [differences]
    while not all(d == 0 for d in differences):
        differences = [b - a for a, b in pairwise(differences)]
        new_sequences.append(differences)

    return new_sequences

def part_1(path, submit):
    """Part 1/Star 1"""

    # Get the data
    data = get_input(path)
    
    answer = 0
    for sequence in data: 
        new_sequences = find_differences(sequence)
        
        next = 0
        for i in range(len(new_sequences)-1, -1, -1):
            next = new_sequences[i][-1] + next
            new_sequences[i].append(next)

        answer += next

    # Print out the response
    print(f"Task 1 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="a", day=int(DAY), year=int(YEAR))


def part_2(path, submit):
    """Part 2/Star 2"""

    # Get the data
    data = get_input(path)

    answer = 0
    for sequence in data: 
        new_sequences = find_differences(sequence)
        
        next = 0
        for i in range(len(new_sequences)-1, -1, -1):
            next = new_sequences[i][0] - next
            new_sequences[i] = [next] + new_sequences

        answer += next

    # Print out the response
    print(f"Task 2 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="b", day=int(DAY), year=int(YEAR))


if __name__ == "__main__":
    """
    Run using e.g.
        `python day-09.py -test`
        `python day-09.py`
        `python day-09.py -submit`
        `python day-09.py -test -2`
        `python day-09.py -2`
        `python day-09.py -test -both`
        `python day-09.py -both`
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
