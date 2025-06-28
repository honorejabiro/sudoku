"""# We define the Revise Function
# We define the AC3 function
# We define the backtracking
# We read the grid
# We create the sudoku object
# We get the variables"""

from sudoku import Sudoku
from copy import deepcopy
from collections import deque
import sys

"""
Using MRV (Minimum Remaining Value) qwe get the variable with the leas number of domains after the inferences made
"""
def select_unnassigned_var(assignment, csp):
    lowest_domains = float("inf")
    res = None
    for i in csp.variables:
        if i not in assignment:
            curr = len(csp.domains[i])
            if curr < lowest_domains:
                lowest_domains = curr
                res = i
    return res

"""
Checks if the domain you want to assign is consistent to the assignment and all other constraints
"""
def consistent(num, assignment, var, csp) -> False:
    for neighbor in csp.neighbors[var]:
        if (
                neighbor in assignment and assignment[neighbor] == num
            ) or (
                neighbor not in assignment and len(csp.domains[neighbor]) == 1 and csp.domains[neighbor] == {num}
            ):
                return False
    return True

"""
Return a list of ordered values, from value with the least amount to rule out other numbers to the one with most ability to rule out others LCV
"""
def order_domain_values(var, assignment, csp):
    hashmap = {}
    for value in csp.domains[var]:
        curr = 0
        for neighbor in csp.neighbors[var]:
            if neighbor not in assignment:
                if value in csp.domains[neighbor]:
                    curr += 1
        hashmap[value] = curr
    
    sorted_vars = sorted(hashmap, key=lambda val: hashmap[val])
    return sorted_vars


        
"""
Backtracking function that assigns numbers to empty cells and backtracks when the number is invalid
"""
def Backtrack(assignment, csp) -> dict:
    if len(assignment) == len(csp.variables):
        return assignment
    
    # Get the value with minimum value domains to chose from MRV
    
    var = select_unnassigned_var(assignment, csp)

    for value in order_domain_values(var, assignment, csp):
        if consistent(value, assignment, var, csp):
            assignment[var] = value
            saved_domains = deepcopy(csp.domains)

            # Maintaing Arc Consistency, this is where the inference occurs we check if the assignment 
            if MAC(csp, var)

    
def main(sys):
    if len(sys.argv) < 2:
        print("Please include the text file for the grid")
        return
    
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    grid = []
    for line in lines:
        row = [int(char) for char in line.strip()]
        grid.append(row)
    
    sudoku = Sudoku(grid)
    assignment = Backtrack({}, sudoku)
    
