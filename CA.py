import numpy as np
from cell import Cell

class CA:
    def __init__(self, n, rules, neighbourhood, edge_type):        
        self.grid = np.array([Cell(0) for _ in range(n)])
        self.rules = rules
        self.neighbourhood = neighbourhood
        self.edge_type = edge_type
        
        self.init_neighbours()
        
        
    def init_neighbours(self):
        pass
    
    
    def step(self):
        for cell in self.grid:
            cell.old_state = cell.state
            
        for cell in self.grid:
            neighbours = ''.join([str(x.old_state) for x in cell.neighbourhood])
            if neighbours in self.rules:
                cell.state = self.rules[neighbours]
    
    
    def run(self, steps):
        for i in range(steps):
            self.step()
            