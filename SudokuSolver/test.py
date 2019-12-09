from typing import Dict, List, Any, Set
from utils import *


def grid_values(grid: str) -> dict:
    dictBoxes: Dict[str, str] = {}
    for index, box in enumerate(boxes):
        if grid[index] == ".":
            dictBoxes[box] = "123456789"
        else:
            dictBoxes[box] = grid[index]
    return dictBoxes


def eliminate(values: Dict) -> Dict:
    singleValueBoxLocations = set()

    for boxLocation, boxValuePossibilities in values.items():
        if len(boxValuePossibilities) == 1:
            singleValueBoxLocations.add(boxLocation)

    for boxLocation in singleValueBoxLocations:
        currPeers: Set[str] = peers[boxLocation]
        for peer in currPeers:
            values[peer] = values[peer].replace(values[boxLocation], '')

    return values


def only_choice(values):
    for unit in unitlist:
        dictCount: Dict[str, int] = {}
        for box in unit:
            for val in values[box]:  # looping over possible values in box
                if val not in dictCount:
                    dictCount[val] = 1
                else:
                    dictCount[val] = dictCount[val] + 1

        mySet = set()
        for key, value in dictCount.items():  # store the values which appear once in set
            if value == 1:
                mySet.add(key)

        # loop over boxes again in set and if valueList contains a number which appears only
        # once, set that box's value to that
        for box in unit:
            for val in values[box]:
                if val in mySet:
                    values[box] = val
                    break
    return values


def main():
    print("Sudoku solver!")

    dictBoxes: dict = grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')
    print("\n\n===initial dictBoxes with possible values===\n")
    display(dictBoxes)

    dictBoxes = eliminate(dictBoxes)
    print("\n\n===dictBoxes after eliminate()===\n")
    display(dictBoxes)

    dictBoxes = only_choice(dictBoxes)
    print("\n\n===dictBoxes after only_choice()===\n")
    display(dictBoxes)


def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        # Your code here: Use the Eliminate Strategy

        # Your code here: Use the Only Choice Strategy

        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values


# boxes = ['A1', 'A2', ..., 'I9']
# row_units[0] = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9']
# column_units[0] = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1']
# square_units[0] = ['A1', 'A2', 'A

if __name__ == "__main__":
    main()
