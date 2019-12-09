from typing import Dict, List, Any, Set

from techniques import grid_values, eliminate, only_choice, reduce_puzzle, search
from utils import *


def individualTechniques():
    print("individualTechniques!")
    dictBoxes: dict = grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')
    print("\n\n===initial dictBoxes with possible values===\n")
    display(dictBoxes)

    dictBoxes = eliminate(dictBoxes)
    print("\n\n===dictBoxes after eliminate()===\n")
    display(dictBoxes)

    dictBoxes = only_choice(dictBoxes)
    print("\n\n===dictBoxes after only_choice()===\n")
    display(dictBoxes)


def eliminationAndOnlyChoiceTogether():
    print("eliminationAndOnlyChoiceTogether")
    dictBoxes: dict = grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')
    print("\n\n===initial dictBoxes with possible values===\n")
    display(dictBoxes)

    reducedDictBoxes = reduce_puzzle(dictBoxes)
    print("\n\n===reducedDictBoxes after reduce_puzzle()===\n")
    display(reducedDictBoxes)


def eliminationAndOnlyChoiceTogetherHardPuzzle():
    hardGrid = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
    dictBoxes: dict = grid_values(hardGrid)
    print("\n\n===initial dictBoxes with possible values===\n")
    display(dictBoxes)

    reducedDictBoxes = reduce_puzzle(dictBoxes)
    print("\n\n===reducedDictBoxes after reduce_puzzle()===\n")
    display(reducedDictBoxes)


def searchWithHardPuzzle():
    hardGrid = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
    values: dict = grid_values(hardGrid)
    print("\n\n===initial dictBoxes with possible values===\n")
    display(values)

    attempt = search(values)
    print("\n\n===Final solution===\n")
    display(attempt)


def main():
    #individualTechniques()
    #eliminationAndOnlyChoiceTogether()
    #eliminationAndOnlyChoiceTogetherHardPuzzle()
    searchWithHardPuzzle()


# boxes = ['A1', 'A2', ..., 'I9']
# row_units[0] = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9']
# column_units[0] = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1']
# square_units[0] = ['A1', 'A2', 'A

if __name__ == "__main__":
    main()
