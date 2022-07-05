import math
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from cell import Cell

class Cyclic_CA:     
    def __init__(self, dimensions: tuple, states: int, neighbourhood: list, edge_type: str):
        self.dimensions = dimensions
        self.grid = [Cell(0) for _ in range(math.prod(dimensions))]
        self.states = states
        self.neighbourhood = neighbourhood
        self.edge_type = edge_type
        
        self.init_neighbours()
    
    
    def init_neighbours(self):
        '''Generates the list of neighbours for each cell'''
        self.grid = np.array(self.grid).reshape(self.dimensions)
        
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                for y, x in self.neighbourhood:
                    if i + y < 0 or i + y >= len(self.grid) or j + x < 0 or j + x >= len(row):
                        if self.edge_type == "wrap":
                            z = self.grid[(i + y) % len(self.grid)][(j + x) % len(row)]
                            
                        elif self.edge_type == "mirror":
                            z = cell
                            
                        elif self.edge_type.isdigit():
                            z = Cell(int(self.edge_type))
                    else:
                        z = self.grid[i + y][j + x]
                    cell.neighbourhood.append(z)
                        
        self.grid = list(self.grid.reshape(-1))
    
    
    def randomise_grid(self):
        '''Randomises the state of all cells in the grid'''
        for cell in self.grid:
            cell.state = random.randint(0, self.states - 1)
        
        
    def change_cell(self, pos, state):
        '''Change the state of a specified cell'''
        i, j = pos
        self.grid[i*self.dimensions[1] + j].state = state
            
    
    def step(self, threshold = 1):
        for cell in self.grid:
            cell.old_state = cell.state
            
        for cell in self.grid:
            if [x.old_state for x in cell.neighbourhood].count((cell.state + 1) % self.states) >= threshold:
                cell.state = (cell.state + 1) % self.states
    
    
    def run(self, steps):
        '''Iterates the CA multiple times'''
        for _ in range(steps):
            self.step()      
    
    
    def graph(self):
        '''Graphs the current iteration of the CA'''
        data = np.array([x.state for x in self.grid]).reshape(self.dimensions)
         
        fig, ax = plt.subplots()
        ax.imshow(data, cmap="viridis", vmin = 0, vmax = self.states - 1, interpolation = "none")
        
        plt.xticks([])
        plt.yticks([])
        plt.title(f"2D CA with states = {self.states},neighbourhood = {self.neighbourhood}, edge_type = {self.edge_type}", fontsize = 10)
        
        plt.show()

        
    def anim_graph(self, steps):
        fig, ax = plt.subplots()
        
        ims = []
        for i in range(steps):
            data = np.array([x.state for x in self.grid]).reshape(self.dimensions)
            im = ax.imshow(data, cmap="viridis", vmin = 0, vmax = self.states - 1, 
                           interpolation = "none", animated = True)
            if i == 0:
                ax.imshow(data, cmap="viridis", vmin = 0, vmax = self.states - 1, 
                          interpolation = "none")
            ims.append([im])
            self.step()
        
        self.anim = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
        
        plt.show()