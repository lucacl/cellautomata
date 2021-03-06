import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from ca import CA
from cell import Cell


def game_of_life_rule(lower, upper, birth):
    rule = ""
    for n in range(2 ** 9):
        binary = bin(n)[2:].zfill(9)
        alive = binary[1:].count("1")
        if binary[0] == '0':
            if alive == birth:
                rule += "1"
            else: rule += "0"
        elif alive < lower or alive > upper:
            rule += "0"
        else: rule += "1"
    return int(rule[::-1], 2)


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