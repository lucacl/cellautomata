import numpy as np
import matplotlib.pyplot as plt
from ca import CA
from cell import Cell

class CA_1D(CA):
    def __init__(self, dimensions, rule, states, neighbourhood, edge_type):
        if isinstance(dimensions, int):
            dimensions = (dimensions,)
        super().__init__(dimensions, rule, states, neighbourhood, edge_type)
        
    
    def init_neighbours(self):
        '''Generates the list of neighbours for each cell'''
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
                     
    
    def change_cell(self, pos, state):
        '''Change the state of a cell'''
        self.grid[pos].state = state
        
    
    def graph(self, steps):
        '''Graphs multiple iterations as a 2D graph'''
        data = []
        for _ in range(steps):
            data += [[x.state for x in self.grid]]
            self.step()
        data = np.array(data)            

        fig, ax = plt.subplots()
        ax.imshow(data, cmap="viridis", vmin = 0, vmax = self.states - 1, interpolation = "none")
        
        plt.xticks([])
        plt.yticks([])
        plt.suptitle(f"Rule {self.rule}", fontsize = 10)
        plt.title(f"1D CA with {self.states} states and {self.neighbourhood} neighbourhood, edge_type = {self.edge_type}", fontsize = 10)
        
        plt.show()