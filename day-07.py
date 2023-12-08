import functools
import sys
from collections import Counter

import aocd

# Set the day and year
DAY = "07"
YEAR = "2023"

CARDS = {
    "2": 0,
    "3": 1,
    "4": 2,
    "5": 3,
    "6": 4,
    "7": 5,
    "8": 6,
    "9": 7,
    "T": 8,
    "J": 9,
    "Q": 10,
    "K": 11,
    "A": 12,
}

# Part 2 J is now a joker character
CARDS_WITH_JOKER = {**CARDS, "J": -1}


def get_input(path):
    """Load the data from the file"""

    # Open the file
    with open(f"{path}/day-{DAY}.txt", "r") as f:
        values = [line.strip().split() for line in f.readlines()]

    return values


def check_result(hand):
    """Identify the score for the hand"""

    if len(set(hand)) == 1:
        # Five of a kind
        return 6

    # Get the counts of each card
    counts = Counter(hand)

    if 4 in set(counts.values()):
        # Four of a kind
        return 5

    if set(counts.values()) == {2, 3}:
        # Full house
        return 4

    if 3 in set(counts.values()):
        # Three of a kind
        return 3

    if list(counts.values()).count(2) == 2:
        # Two pair
        return 2

    if 2 in set(counts.values()):
        # One pair
        return 1

    # High card
    return 0


def check_best_possible_result(hand):
    """If the hand contains a J, we want to find the best possible result"""

    if "J" not in hand:
        return check_result(hand)

    return max(check_result(hand.replace("J", c)) for c in CARDS.keys() if c != "J")


def compare_hands(hand_1, hand_2):
    """Compare the hands"""

    # Check the results
    result_1 = hand_1["result"]
    result_2 = hand_2["result"]

    if result_1 > result_2:
        return 1
    elif result_1 < result_2:
        return -1

    # Both results the same, then look at the hands
    hand_1 = hand_1["hand"]
    hand_2 = hand_2["hand"]

    for i in range(len(hand_1)):
        if hand_1[i] > hand_2[i]:
            return 1
        elif hand_1[i] < hand_2[i]:
            return -1

    return 0


def part_1(path, submit):
    """Part 1/Star 1"""

    # Get the data
    data = get_input(path)

    hands = []
    for hand, bid in data:
        hands.append(
            {
                "orig_hand": hand,
                "hand": [CARDS[h] for h in hand],
                "bid": int(bid),
                "result": check_result(hand),
            }
        )

    hands = sorted(hands, key=functools.cmp_to_key(compare_hands))

    answer = 0
    for rank, hand in enumerate(hands):
        answer += hand["bid"] * (rank + 1)

    # Print out the response
    print(f"Task 1 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="a", day=int(DAY), year=int(YEAR))


def part_2(path, submit):
    """Part 2/Star 2"""

    # Get the data
    data = get_input(path)

    hands = []
    for hand, bid in data:
        hands.append(
            {
                "orig_hand": hand,
                "hand": [CARDS_WITH_JOKER[h] for h in hand],
                "bid": int(bid),
                "result": check_best_possible_result(hand),
            }
        )

    hands = sorted(hands, key=functools.cmp_to_key(compare_hands))

    answer = 0
    for rank, hand in enumerate(hands):
        answer += hand["bid"] * (rank + 1)

    # Print out the response
    print(f"Task 2 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="b", day=int(DAY), year=int(YEAR))


if __name__ == "__main__":
    """
    Run using e.g.
        `python day-07.py -test`
        `python day-07.py`
        `python day-07.py -submit`
        `python day-07.py -test -2`
        `python day-07.py -2`
        `python day-07.py -test -both`
        `python day-07.py -both`
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
