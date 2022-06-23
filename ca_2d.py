import numpy as np
import matplotlib.pyplot as plt
from ca import CA
from cell import Cell

def moore(r):
    '''Generates a list of tuples for a Moore neighbourhood with radius r'''
    neighbourhood = [(0, 0)]
    for i in range(1, r + 1):
        for j in range(r + 1):
            neighbourhood += [(i, j), (-j, i), (-i, -j), (j, -i)]
    return neighbourhood
        
def neumann(r):
    '''Generates a list of tuples for a Von Neumann neighbourhood with radius r.'''
    neighbourhood = [(0, 0)]
    for i in range(1, r + 1):
        for j in range(r):
            if i + j <= r:
                neighbourhood += [(i, j), (-j, i), (-i, -j), (j, -i)]
    return neighbourhood
                
def plus(r):
    '''Generates a list of tuples for a plus neighbourhood with radius r.'''
    neighbourhood = [(0, 0)]
    for i in range(1, r + 1):
        neighbourhood += [(-i, 0), (i, 0), (0, -i), (0, i)]
    return neighbourhood
    
def cross(r):
    '''Generates a list of tuples for a cross neighbourhood with radius r.'''
    neighbourhood = [(0, 0)]
    for i in range(1, r + 1):
        neighbourhood += [(-i, -i), (i, -i), (-i, i), (i, i)]
    return neighbourhood


class CA_2D(CA):
   
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
        
        
    def change_cell(self, pos, state):
        '''Change the state of a specified cell'''
        i, j = pos
        self.grid[i*self.dimensions[1] + j].state = state
        
        
    def game_of_life_step(self, lower = 2, upper = 3, birth = 3):
        '''Iterate the game by the rules of game of life in stead of self.rule.'''
        for cell in self.grid:
            cell.old_state = cell.state
    
        for cell in self.grid: 
            alive = [x for x in cell.neighbourhood if x.old_state != 0]
            if cell.state == 0:
                if len(alive) == birth:
                    cell.state = 1
            elif len(alive) - 1 < lower or len(alive) - 1> upper:
                cell.state = 0
                
                    
    
    def graph(self):
        '''Graphs the current iteration of the CA'''
        data = np.array([x.state for x in self.grid]).reshape(self.dimensions)
         
        fig, ax = plt.subplots()
        ax.imshow(data, cmap="viridis", vmin = 0, vmax = self.states - 1, interpolation = "none")
        
        plt.xticks([])
        plt.yticks([])
        plt.suptitle(f"Rule {self.rule}", fontsize = 10)
        plt.title(f"2D CA with states = {self.states},neighbourhood = {self.neighbourhood}, edge_type = {self.edge_type}", fontsize = 10)
        
        plt.show()