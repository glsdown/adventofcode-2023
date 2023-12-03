
import sys
from collections import defaultdict

import aocd

# Set the day and year
DAY = "03"
YEAR = "2023"


def get_input(path):
    """Load the data from the file"""

    # Open the file
    with open(f"{path}/day-{DAY}.txt", "r") as f:
        values = [line.strip() for line in f.readlines()]

    return values


def parse_data(data):
    """Understand where the numbers and symbols are"""

        # Find all the values
    symbols = set()
    number_list = []
    potential_gears = set()
    for row in range(len(data)):
        number = ""
        number_coords = []
        for col in range(len(data[0])):
            current = data[row][col]
            # If it's a number we want to keep track of it
            if current.isdigit():
                number += current
                number_coords.append((col, row))
            else:
                # If we've reached the end of the number, then want to record that
                if number:
                    number_list.append({"value": int(number), "coords": number_coords})

                number = ""
                number_coords = []
                # Keep track of where the symbols are
                if current != ".":
                    symbols.add((col, row))
                    if current == "*":
                        potential_gears.add((col, row))
            # Deal with when the number is the 'last' thing in the row
            if col == len(data[0]) - 1 and number:
                number_list.append({"value": int(number), "coords": number_coords})

    return symbols, number_list, potential_gears

def check_part_number(number, symbols):
    """Check if the number is a part number i.e. is next to a symbol"""

    value = number["value"]
    coords = number["coords"]

    # Check the diagonals of the end ones
    ends = [(coords[0][0] - 1, coords[0][1]), (coords[-1][0] + 1, coords[-1][1]) ]
    for end in ends:
        for offset in [-1, 0, 1]:
            if (end[0], end[1] + offset) in symbols:
                return value

    # Check above and below
    for coord in coords:
        for offset in [-1, 1]:
            if (coord[0], coord[1] + offset) in symbols:
                return value
    
    # If no symbol found, return 0
    return 0


def find_adjacent_part_numbers(part_numbers, max_row, max_col):
    """Find co-ordinates of adjacent cells that overlap with exactly 2 part_numbers"""

    coordinate_counts = defaultdict(list)

    for part in part_numbers:
        coords = part["coords"]
        outside = set()

        # Check the diagonals of the end ones
        ends = [(coords[0][0] - 1, coords[0][1]), (coords[-1][0] + 1, coords[-1][1]) ]
        for end in ends:
            for offset in [-1, 0, 1]:
                outside.add((end[0], end[1] + offset))

        # Check above and below
        for coord in coords:
            for offset in [-1, 1]:
                outside.add((coord[0], coord[1] + offset))
        
        for c in outside:
            if 0 <= c[0] < max_col and 0 <= c[1] < max_row:
                coordinate_counts[c].append(part["value"])
    
    return coordinate_counts

def part_1(path, submit):
    """Part 1/Star 1"""

    # Get the data
    data = get_input(path)
    
    # Parse the data
    symbols, number_list, _ = parse_data(data)

    # Find the sum of the part numbers
    answer = sum(check_part_number(number, symbols) for number in number_list)        

    # Print out the response
    print(f"Task 1 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="a", day=int(DAY), year=int(YEAR))


def part_2(path, submit):
    """Part 2/Star 2"""

    # Get the data
    data = get_input(path)

    # Parse the data
    symbols, number_list, potential_gears = parse_data(data)

    part_numbers = [number for number in number_list if check_part_number(number, symbols)]

    coordinate_counts = find_adjacent_part_numbers(part_numbers, max_row=len(data), max_col=len(data[0]))

    # Find the co-ordinates with just two numbers overlapping
    answer = 0
    for k, v in coordinate_counts.items():
        if k in potential_gears and len(v) == 2:
            answer += v[0] * v[1]

    # Print out the response
    print(f"Task 2 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="b", day=int(DAY), year=int(YEAR))


if __name__ == "__main__":
    """
    Run using e.g.
        `python day-03.py -test`
        `python day-03.py`
        `python day-03.py -submit`
        `python day-03.py -test -2`
        `python day-03.py -2`
        `python day-03.py -test -both`
        `python day-03.py -both`
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
