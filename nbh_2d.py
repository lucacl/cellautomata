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