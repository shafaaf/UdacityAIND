from typing import Dict

from utils import *


def grid_values(grid: str) -> dict:
    """Convert grid string into {<box>: <value>} dict with '.' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '.' if it is empty.
    """
    dictBoxes: Dict[str, str] = {}
    for index, box in enumerate(boxes):
        dictBoxes[box] = grid[index]
    return dictBoxes


def main():
    print("Hello World!")
    dictBoxes: dict = grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')
    print(dictBoxes)


# boxes = ['A1', 'A2', ..., 'I9']
# row_units[0] = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9']
# column_units[0] = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1']
# square_units[0] = ['A1', 'A2', 'A

if __name__ == "__main__":
    main()
