import numpy as np
from cell import Cell


def base_to_number(a, b):
    n = 0
    for i, x in enumerate(a):
         n += x * (b ** i)
    return n


def number_to_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits


class CA:
    def __init__(self, n, rule, states, neighbourhood, edge_type):        
        self.grid = np.array([Cell(0) for _ in range(n)])
        self.rule = rule
        self.states = states
        self.rule_base = number_to_base(rule, states)
        
        self.init_neighbours(neighbourhood, edge_type)
        
        
    def init_neighbours(self, neighbourhood, edge_type):
        pass
    
    
    def step(self):
        for cell in self.grid:
            cell.old_state = cell.state
            
        for cell in self.grid:
            i = base_to_number([x.old_state for x in cell.neighbourhood], self.states)
            if i >= len(self.rule_base):
                cell.state = 0
            else:
                cell.state = self.rule_base[i]
    
    
    def run(self, steps):
        for i in range(steps):
            self.step()        