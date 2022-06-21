import numpy as np
import matplotlib.pyplot as plt
from CA import CA
from cell import Cell

class CA_1D(CA):
    
    def init_neighbours(self, neighbourhood, edge_type):
        for i, cell in enumerate(self.grid):
            for j in neighbourhood:
                k = i + j
                if k < 0 or k >= len(self.grid):
                    if edge_type == "wrap":
                        x = self.grid[k % len(self.grid)]
                        
                    elif edge_type == "mirror":
                        x = cell
                        
                    elif edge_type.isdigit():
                        x = Cell(int(edge_type))
                else:
                    x = self.grid[k]
                cell.neighbourhood.append(x)
                     
        
    def graph(self, steps):
        data = []
        for _ in range(steps):
            data += [[x.state for x in self.grid]]
            self.step()
        data = np.array(data)            

        nrows = steps
        ncols = len(self.grid)

        fig, ax = plt.subplots()
        ax.imshow(data, cmap="Greys", origin="upper", vmin=0)

        # optionally add grid
        ax.set_xticks(np.arange(ncols+1)-0.5, minor=True)
        ax.set_yticks(np.arange(nrows+1)-0.5, minor=True)
        #ax.grid(which="minor")
        ax.tick_params(which="minor", size=0)

        plt.show()