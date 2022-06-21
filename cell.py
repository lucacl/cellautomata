class Cell:
    def __init__(self, state):
        self.state = state
        self.old_state = state
        self.neighbourhood = []