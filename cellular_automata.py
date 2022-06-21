import numpy as np
import matplotlib.pyplot as plt

class cell:
    def __init__(self, state):
        self.state = state
        self.old_state = state
        self.neighbourhood = []
        
    
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
        
        
    def init_neighbours(self, neighbourhood, edge_type):
        pass
        
    
    def step(self):
        for cell in self.grid:
            neighbours = ''.join([str(x.old_state) for x in cell.neighbourhood])
            if neighbours in self.rules:
                cell.state = self.rules[neighbours]
                
        for cell in self.grid:
            cell.old_state = cell.state
    
#class 1d_CA(CA):
    
#class 2d_CA(CA):
'''
import numpy as np
import matplotlib.pyplot as plt

nrows = 10
ncols = 10

Cellid = [2, 4 ,5, 11 ,45 ,48 ,98]
Cellval = [2, 4 ,55, 77,45 ,30 ,15]

data = np.zeros(nrows*ncols)
data[Cellid] = Cellval
data = np.ma.array(data.reshape((nrows, ncols)), mask=data==0)

fig, ax = plt.subplots()
ax.imshow(data, cmap="Greens", origin="lower", vmin=0)

# optionally add grid
ax.set_xticks(np.arange(ncols+1)-0.5, minor=True)
ax.set_yticks(np.arange(nrows+1)-0.5, minor=True)
ax.grid(which="minor")
ax.tick_params(which="minor", size=0)

plt.show()
'''