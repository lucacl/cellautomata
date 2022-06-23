import random
from cell import Cell

def number_to_base(n, b):
    '''Neemt een decimaal getal en een grondtal, en geeft een lijst getallen terug.'''
    digits = []
    while n:
        digits.append(n % b)
        n //= b
    return digits

def base_to_number(digits, b):
    '''Neemt een lijst getallen en een grondtal, en geeft een decimaal getal terug.'''
    n = 0
    for i, x in enumerate(digits):
         n += x * (b ** i)
    return n


class CA:
    '''
    Een generieke klasse voor een cellulaire automaat
    
    ...
    
    Attributen
    ----------
    grid: list(Cell)
        lijst met cellen
    rule: int
        regel van de CA
    states: int
        aantal verschillende toestanden die een cel kan aannemen
    rule_base: list(int)
        rule met als grondtal states, gerepresenteerd als lijst
    neighbourhood: list
        de buren van een willekeurige cel, relatief aan de cel
    edge_type: str
        de regel die wordt toegepast voor randgevallen
        
    Methoden
    --------
    
    '''
    
    def __init__(self, n, rule, states, neighbourhood, edge_type): 
        assert isinstance(n, int) and n > 0, f'{n} not valid input, must be positive integer'
        assert isinstance(rule, int) and rule >= 0, f'{rule} not valid input, must be non negative integer'
        assert isinstance(states, int) and states > 0, f'{states} not valid input, must be positive integer'
        assert isinstance(neighbourhood, list), f'{neighbourhood} not valid input, must be list'
        assert edge_type in ['mirror', 'wrap'] or edge_type.isdigit(), f'{edge_type} not valid input, must be "mirror", "wrap" or a positive integer as string'
        
        self.grid = [Cell(0) for _ in range(n)]
        self.rule = rule
        self.states = states
        self.rule_base = number_to_base(rule, states)
        self.neighbourhood = neighbourhood        
        self.edge_type = edge_type
        self.init_neighbours(neighbourhood, edge_type)
        
        
    def init_neighbours(self, neighbourhood, edge_type):
        pass
    
    
    def randomise_grid(self):
        '''generates a rondom grid'''
        for cell in self.grid:
            cell.state = random.randint(0, self.states - 1)
            
            
    def randomise_rule(self):
        '''generates a random rule'''
        self.rule = random.randint(1, self.states ** (self.states ** len(self.neighbourhood)))
        self.rule_base = number_to_base(self.rule, self.states)
    
    
    def change_cell(self):
        pass
    
    
    def step(self):
        '''generates the next iteration of the CA'''
        for cell in self.grid:
            cell.old_state = cell.state
            
        for cell in self.grid:
            i = base_to_number([x.old_state for x in cell.neighbourhood], self.states)
            if i >= len(self.rule_base):
                cell.state = 0
            else:
                cell.state = self.rule_base[i]
    
    
    def run(self, steps):
        '''Genereert de CA na '''
        for _ in range(steps):
            self.step()        
            
    def graph(self):
        pass
