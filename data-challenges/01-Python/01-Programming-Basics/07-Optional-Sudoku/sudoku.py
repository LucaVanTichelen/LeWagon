# pylint: disable=missing-docstring


def sudoku_validator(grid):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i, k in enumerate(grid):
        if grid[i].sort() != numbers:
            return False
    