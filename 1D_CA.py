from CA import CA
from cell import Cell

class CA_1D(CA):
    
    def init_neighbours(self):
        for i, cell in enumerate(self.grid):
            for j in self.neighbourhood:
                k = i + j
                if k < 0 or k >= len(self.grid):
                    if self.edge_type == "wrap":
                        x = self.grid[k % len(self.grid)]
                    elif self.edge_type == "mirror":
                        x = cell
                    elif self.edge_type.isdigit():
                        x = Cell(int(self.edge_type))
                else:
                    x = self.grid[k]
                cell.neighbourhood.append(x)