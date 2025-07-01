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
    Initialize the domains for all cells
    """
    def initialize_domains(self) -> dict:
        domains = {}

        for (x, y) in self.cells:
            if self.grid[x][y] == 0:
                domains[(x, y)] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            else:
                domains[(x, y)] = {self.grid[x][y]}
        
        return domains
    
    """
    Provide a dictionary of all cell's neighbors
    """
    def get_neighbours(self) -> dict:
        neighbors = {}

        for row in range(9):
            for column in range(9):
                peers = set()

                for i in range(9):
                    if i != column:
                        peers.add((row, i))
                    if i != row:
                        peers.add((i, column))
                
                """
                Finding the starting of our box to add the neighbours of the cell to the set
                """

                box_col = 0
                if 0 <= column <= 2:
                    box_col = 0
                elif 3 <= column <= 5:
                    box_col = 3
                else:
                    box_col = 6

                box_row = 0
                if 0 <= row <= 2:
                    box_row = 0
                elif 3 <= row <= 5:
                    box_row = 3
                else:
                    box_row = 6
                
                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):
                        if (i, j) != (row, column):
                            peers.add((i, j))
                neighbors[(row, column)] = peers
        return neighbors
    

    def __str__(self) -> None:
        for i in range(9):
            row = ""
            for j in range(9):
                cell = self.grid[i][j]
                row += f'{cell if cell != 0 else "*" }'
            print(row)

    """
    Checks if the sudoku is complete and returns either true or false
    """
    def is_complete(self) -> bool:
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return False
        
        return True