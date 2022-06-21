import numpy as np
import matplotlib.pyplot as plt
from CA import CA
from cell import Cell

class CA_1D(CA):
    
    def __init__(self, n, rules, neighbourhood, edge_type):
        super().__init__(n, rules, neighbourhood, edge_type)
        
        self.checkrules()
    
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
                     
                
    def checkrules(self):
        if isinstance(self.rules, int):
            binary = format(self.rules, "b")
            fullbinary = str(binary).zfill(8)
            neighbour_sets = ['111', '110', '101', '100', '011', '010', '001', '000']
            dictionary = {}
            for i, x in enumerate(neighbour_sets):
                dictionary |= {x: int(fullbinary[i])}
            self.rules = dictionary
                
        
    def graph(self, steps):
        data = []
        for _ in range(steps):
            data += [[x.state for x in self.grid]]
            self.step()
        data = np.array(data)            

        nrows = steps
        ncols = len(self.grid)

        fig, ax = plt.subplots()
        ax.imshow(data, cmap="Greens", origin="upper", vmin=0)

        # optionally add grid
        ax.set_xticks(np.arange(ncols+1)-0.5, minor=True)
        ax.set_yticks(np.arange(nrows+1)-0.5, minor=True)
        #ax.grid(which="minor")
        ax.tick_params(which="minor", size=0)

        plt.show()
