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

530070000 \n
600195000 \n
098000060 \n
800060003 \n
400803001 \n
700020006 \n
060000280 \n
000419005 \n
000080079

2. Run the solver:

```bash
python3 solver.py sample_grid.txt
```
If you usually use older versionof python you can run 

```bash
python solver.py sample_grid.txt
```
