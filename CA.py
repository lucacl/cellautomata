import numpy as np
from cell import cell

class CA:
    '''
    edge_type = ['state x', 'mirror', 'wrap']
    '''
    def __init__(self, grid, rules, neighbourhood, edge_type = 0):
        self.grid = np.array([cell(x) for x in grid])
        self.rules = rules
        self.neighbourhood = neighbourhood
        self.edge_type = edge_type
        
        self.init_neighbours()
        
        
    def init_neighbours(self):
        pass
    
    
    def step(self):
        for cell in self.grid:
            neighbours = ''.join([str(x.old_state) for x in cell.neighbourhood])
            if neighbours in self.rules:
                cell.state = self.rules[neighbours]
                
        for cell in self.grid:
            cell.old_state = cell.state
    
