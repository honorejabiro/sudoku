# Sudoku Solver

A Sudoku puzzle solver implemented in Python using backtracking with constraint propagation via AC3 algorithm.

## Features

- Uses Minimum Remaining Value (MRV) heuristic to select variables
- Orders domain values with Least Constraining Value (LCV) heuristic
- Implements AC3 algorithm for arc consistency to prune domains
- Backtracking search with inference for efficient solving
- Includes unit tests for solver validation

## Usage

1. Place your Sudoku puzzle grid in a text file (e.g., `puzzle.txt`) with 9 lines, each line containing 9 digits (`0` for empty cells).

Example:

530070000
600195000
098000060
800060003
400803001
700020006
060000280
000419005
000080079

2. Run the solver:

```bash
python3 solver.py sample_grid.txt
 or
python solver.py sample_gird.txt
