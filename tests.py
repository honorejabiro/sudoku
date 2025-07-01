import unittest
from sudoku import Sudoku
from solver import Backtrack

class TestSudokuSolver(unittest.TestCase):

    def setUp(self):
        # Define a sample Sudoku puzzle with a known solution
        self.grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        self.sudoku = Sudoku(self.grid)

    def test_solver_finds_solution(self):
        assignment = Backtrack({}, self.sudoku)
        self.assertTrue(assignment, "Backtracking failed to find a solution")
        
        # Apply assignment to the grid
        for (row, col), value in assignment.items():
            self.sudoku.grid[row][col] = value
        
        # Check that the final board is valid
        self.assertTrue(self.sudoku.is_complete(), "Final board is not complete")

    def test_assignment_valid(self):
        assignment = Backtrack({}, self.sudoku)
        for (row, col), value in assignment.items():
            for neighbor in self.sudoku.neighbors[(row, col)]:
                if neighbor in assignment:
                    self.assertNotEqual(assignment[neighbor], value,
                        f"Conflict between {(row, col)} and {neighbor}")

if __name__ == '__main__':
    unittest.main()
