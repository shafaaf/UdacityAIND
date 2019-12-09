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


def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        # Your code here: Use the Eliminate Strategy
        values = eliminate(values)

        # Your code here: Use the Only Choice Strategy
        values = only_choice(values)

        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])

        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after

        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values


def search(values):
    "Using depth-first search and propagation, try all possible values."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False  ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes):
        return values  ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n, s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt
