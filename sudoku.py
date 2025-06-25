class Sudoku:
    """
    Represents the sudoku with the 9x9 structure 2D matrix.
    """
    def __init__(self, grid):
        # Getting the structure of our sudoku and assigning its variables, domains, constraits
        self.grid = grid
        self.cells = [(i, j) for i in range(9) for j in range(9)]
        self.variables = [cell for cell in self.cells if self.grid[cell[0]][cell[1]] == 0]
        self.domains = self.initialize_domains()
        self.neighbors = self.get_neighbours()
    
    
    """
    Initializer the domains for all cells
    """
    def initialize_domains(self) -> dict:
        domains = {}

        for cell in self.cells:
            if self.grig[cell] == 0:
                domains[cell] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            else:
                domains[cell] = {self.grid[cell]}
        
        return domains
                                        
