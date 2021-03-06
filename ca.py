import math
import random
from cell import Cell

def number_to_base(n, b):
    '''Takes a decimal integer number and a base, and returns a list of integers'''
    digits = []
    while n:
        digits.append(n % b)
        n //= b
    return digits[::-1]

def base_to_number(digits, b):
    '''Takes a list of integers and a base, and returns a decimal integer number'''
    n = 0
    for i, x in enumerate(digits[::-1]):
         n += x * (b ** i)
    return n


class CA:     
    def __init__(self, dimensions, rule, states, neighbourhood, edge_type):
        #Checks for valid inputs
        assert isinstance(dimensions, tuple) and all(x > 0 for x in dimensions), f'{dimensions} not valid input, must be positive integer'
        assert isinstance(rule, int) and rule >= -1, f'{rule} not valid input, must be non-negative integer (or -1 for a random rule)'
        assert isinstance(states, int) and states > 0, f'{states} not valid input, must be positive integer'
        assert isinstance(neighbourhood, list), f'{neighbourhood} not valid input, must be list'
        assert edge_type in ['mirror', 'wrap'] or edge_type.isdigit(), f'{edge_type} not valid input, must be "mirror", "wrap" or a non-negative integer as string'

        self.dimensions = dimensions
        self.grid = [Cell(0) for _ in range(math.prod(dimensions))]
        self.states = states
        self.neighbourhood = neighbourhood
        self.edge_type = edge_type
        
        #generate random rule if rule == -1
        if rule == -1: 
            self.randomise_rule()
        else: 
            self.rule = rule
            self.rule_base = number_to_base(rule, states)
            
        self.init_neighbours()
    
    
    def randomise_grid(self):
        '''Randomises the state of all cells in the grid'''
        for cell in self.grid:
            cell.state = random.randint(0, self.states - 1)
            
            
    def randomise_rule(self):
        '''Generates a random rule'''
        self.rule = random.randint(1, self.states ** (self.states ** len(self.neighbourhood)))
        self.rule_base = number_to_base(self.rule, self.states)
    
    
    def cyclic_totalistic_rule(self, lower, upper, birth):
        rule = []
        for n in range(self.states ** len(self.neighbourhood)):
            
            n_base = number_to_base(n, self.states)
            while len(n_base) < len(self.neighbourhood): n_base = [0] + n_base
            
            alive = len(self.neighbourhood) - 1 - n_base[1:].count(0)
            if n_base[0] == 0:
                if alive == birth:
                    rule += [1]
                else: rule += [0]
            elif alive < lower or alive > upper:
                rule += [0]
            else: rule += [n_base[0] % (self.states - 1) + 1]
        return base_to_number(rule[::-1], self.states)            
    
    
    def cyclic_rule(self, threshold = 1):
        rule = []
        for n in range(self.states ** len(self.neighbourhood)):
            n_base = number_to_base(n, self.states)
            while len(n_base) < len(self.neighbourhood): n_base = [0] + n_base
            
            if n_base.count((n_base[0] + 1) % self.states) >= threshold:
                rule.append((n_base[0] + 1) % self.states)
            else: rule.append(n_base[0])
        return base_to_number(rule[::-1], self.states)
    
    
    def cyclic_step(self, threshold = 1):
        for cell in self.grid:
            cell.old_state = cell.state
            
        for cell in self.grid:
            if [x.old_state for x in self.grid].count((cell.state + 1) % self.states) >= threshold:
                cell.state = (cell.state + 1) % self.states
    
    
    def step(self):
        '''Generates the next iteration of the CA'''
        for cell in self.grid:
            cell.old_state = cell.state
            
        for cell in self.grid:
            i = base_to_number([x.old_state for x in cell.neighbourhood], self.states)
            if i >= len(self.rule_base):
                cell.state = 0
            else:
                cell.state = self.rule_base[~i]
    
    
    def run(self, steps):
        '''Iterates the CA multiple times'''
        for _ in range(steps):
            self.step()      
            
            
    #not implemented:
            
    def init_neighbours(self):
        '''Initialises the neighbours of all cells in the grid'''
        pass
    
    def change_cell(self, pos, state):
        '''Change the state of a cell'''
        pass
            
    def graph(self):
        '''Graphs the current iteration of the CA'''
        pass