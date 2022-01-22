# pylint: disable-all
import unittest
from sudoku import sudoku_solver

class SudokuSolverTest(unittest.TestCase):
    def test_valid_grid(self):
        solved_grid = [
            [7, 1, 3, 2, 4, 5, 8, 9, 6],
            [5, 8, 9, 6, 1, 3, 2, 4, 7],
            [4, 6, 2, 7, 9, 8, 1, 3, 5],
            [1, 2, 8, 3, 5, 4, 6, 7, 9],
            [9, 5, 4, 8, 7, 6, 3, 2, 1],
            [3, 7, 6, 9, 2, 1, 4, 5, 8],
            [6, 9, 7, 4, 8, 2, 5, 1, 3],
            [8, 4, 1, 5, 3, 9, 7, 6, 2],
            [2, 3, 5, 1, 6, 7, 9, 8, 4]
        ]
        input_grid = [
            [7,0,0,  0,0,0,  0,0,6],
            [0,0,0,  6,0,0,  0,4,0],
            [0,0,2,  0,0,8,  0,0,0],

            [0,0,8,  0,0,0,  0,0,0],
            [0,5,0,  8,0,6,  0,0,0],
            [0,0,0,  0,2,0,  0,0,0],

            [0,0,0,  0,0,0,  0,1,0],
            [0,4,0,  5,0,0,  0,0,0],
            [0,0,5,  0,0,7,  0,0,4]
        ]
        solver = sudoku_solver(input_grid)
        self.assertListEqual(solver, solved_grid)

    def test_incorrect_grid(self):
        input_grid = [
            [7,0,0,  0,0,0,  0,0,6],
            [0,0,0,  6,0,0,  0,4,0],
            [0,0,2,  0,0,8,  0,0,0],

            [0,0,8,  0,0,0,  0,0,0],
            [0,5,0,  8,0,6,  0,0,0],
            [0,0,0,  0,2,0,  0,0,0],

            [0,0,0,  0,0,0,  0,1,0],
            [0,4,0,  5,0,0,  0,0],
            [0,0,5,  0,0,7,  0,0,0]
        ]
        solver = sudoku_solver(input_grid)
        self.assertEqual(solver, "invalid grid", "Input Validation: Should return `invalid grid` when grid is missing a number")

    def test_incorrect_grid_2(self):
        input_grid = [
            [7,0,0,  0,0,0,  0,0,6],
            [0,0,0,  6,0,0,  0,4,0],
            [0,0,2,  0,0,8,  0,0,0],

            [0,0,8,  0,0,0,  0,0,0],
            [0,5,0,  8,0,6,  0,0,0],
            [0,0,0,  0,2,0,  0,0,0],

            [0,0,0,  0,0,0,  0,1,0],
            [0,0,5,  0,0,7,  0,0,0]
        ]
        solver = sudoku_solver(input_grid)
        self.assertEqual(solver, "invalid grid", "Input Validation: Should return `invalid grid` when grid is missing a column")

    def test_incorrect_grid_3(self):
        input_grid = 70004300053
        solver = sudoku_solver(input_grid)
        self.assertEqual(solver, "invalid grid", "Input Validation: Should return `invalid grid` when the grid is not a list of list")
