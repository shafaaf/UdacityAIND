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


def main():
    print("Hello World!")
    dictBoxes: dict = grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')
    dictBoxes = eliminate(dictBoxes)
    display(dictBoxes)


# boxes = ['A1', 'A2', ..., 'I9']
# row_units[0] = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9']
# column_units[0] = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1']
# square_units[0] = ['A1', 'A2', 'A

if __name__ == "__main__":
    main()
