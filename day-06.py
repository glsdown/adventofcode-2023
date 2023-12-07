
import sys

import aocd

# Set the day and year
DAY = "06"
YEAR = "2023"


def get_input(path):
    """Load the data from the file"""

    # Open the file
    with open(f"{path}/day-{DAY}.txt", "r") as f:
        time, distance = [line.strip().split(":")[1] for line in f.readlines()]

    time = [int(i) for i in time.strip().split() if i.isdigit()]
    distance = [int(d) for d in distance.strip().split() if d.isdigit()]

    return time, distance


def part_1(path, submit):
    """Part 1/Star 1"""

    # Get the data
    time, distance = get_input(path)

    data = list(zip(time, distance))
    
    # Hold for i ms, gives i * (n - i) distance
    # Need to find number of values of i where i * (time - i) > distance
    # Therefore need to solve for x:
    # x ** 2 - x * time + distance < 0
    answer = 1
    for time, distance in data:

        # Get solutions
        solution = (- time - (time ** 2 - 4 * distance) ** 0.5) / 2
        solution_2 = (- time + (time ** 2 - 4 * distance) ** 0.5) / 2
        
        # Find number of integers between them
        total = abs(int(solution) - int(solution_2))
        if solution == int(solution) or solution_2 == int(solution_2):
            total -= 1

        # Add to the total
        answer *= total

    # Print out the response
    print(f"Task 1 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="a", day=int(DAY), year=int(YEAR))


def part_2(path, submit):
    """Part 2/Star 2"""

    # Get the data
    time, distance = get_input(path)

    time = int("".join(str(i) for i in time))
    distance = int("".join(str(i) for i in distance))

    # Get solutions
    solution = (- time - (time ** 2 - 4 * distance) ** 0.5) / 2
    solution_2 = (- time + (time ** 2 - 4 * distance) ** 0.5) / 2
    
    # Find number of integers between them
    answer = abs(int(solution) - int(solution_2))
    if solution == int(solution) or solution_2 == int(solution_2):
        answer -= 1

    # Print out the response
    print(f"Task 2 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="b", day=int(DAY), year=int(YEAR))


if __name__ == "__main__":
    """
    Run using e.g.
        `python day-06.py -test`
        `python day-06.py`
        `python day-06.py -submit`
        `python day-06.py -test -2`
        `python day-06.py -2`
        `python day-06.py -test -both`
        `python day-06.py -both`
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
