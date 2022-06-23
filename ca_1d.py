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
                     
    
    def change_cell(self, pos, state):
        self.grid[pos].state = state
        
    
    def graph(self, steps):
        data = []
        for _ in range(steps):
            data += [[x.state for x in self.grid]]
            self.step()
        data = np.array(data)            

        fig, ax = plt.subplots()
        ax.imshow(data, cmap="viridis", vmin = 0, vmax = self.states - 1, interpolation = "none")
        
        plt.xticks([])
        plt.yticks([])
        plt.suptitle(f"Rule {self.rule}")
        plt.title(f"1D CA with {self.states} states and {self.neighbourhood} neighbourhood, edge_type = {self.edge_type}")
        plt.show()
