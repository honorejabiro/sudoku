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
Using MRV (Minimum Remaining Value) we get the variable with the least number of domains after the inferences made
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
def consistent(num, assignment, var, csp) -> bool:
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
Implementing the Revised function for the AC3 function
"""
def REVISE(csp, X, Y):
    revised = False
    if len(csp.domains[Y]) == 1:
        y_val = next(iter(csp.domains[Y]))
        for x in csp.domains[X].copy():
            if x == y_val:
                csp.domains[X].remove(x)
                revised = True
    return revised


"""
Implementing the ac3 algorithm
"""
def ac3(csp, queue):
    inferences = {}
    while queue:
        X, Y = queue.pop()
        if REVISE(csp, X, Y):
            if not csp.domains[X]:
                return False
            inferences[X] = csp.domains[X].copy()
            for Z in csp.neighbors[X] - {Y}:
                queue.append((Z, X))
    return inferences

    

"""
Implement all inferences with each assignment given
"""
def inference(csp, var):
    queue = deque()
    queue = [(neighbor, var) for neighbor in csp.neighbors[var]]
    return ac3(csp, queue)
        
"""
Backtracking function that assigns numbers to empty cells and backtracks when the number is invalid
"""
def Backtrack(assignment, csp) -> dict:
    if len(assignment) == len(csp.variables):
        return assignment
    
    var = select_unnassigned_var(assignment, csp)

    saved_domains = deepcopy(csp.domains)   # <- Move here, once per variable
    
    for value in order_domain_values(var, assignment, csp):
        if consistent(value, assignment, var, csp):
            assignment[var] = value
            csp.domains[var] = {value}

            inferences = inference(csp, var)
            if inferences is not False:
                for variable, val in inferences.items():
                    csp.domains[variable] = val
                    if len(val) == 1 and variable not in assignment:
                        assignment[variable] = next(iter(val))

                result = Backtrack(assignment, csp)
                if result:
                    return result
                
                for variable in inferences:
                    if variable in assignment:
                        del assignment[variable]

            # Restore domains and assignment before trying next value
            csp.domains = deepcopy(saved_domains)
            if var in assignment:
                del assignment[var]

    # If no value worked
    return False




    
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
    if not assignment:
        print("No solution found")
        return 
    
    print(assignment)
    
    for (x, y), value in assignment.items():
        sudoku.grid[x][y] = value
    
    if sudoku.is_complete():
        print("You win! Final board:")
        print(sudoku)
    else:
        print("Partial solution or failure.")

    

if __name__ == "__main__":
    main(sys)