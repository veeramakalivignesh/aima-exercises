class SearchProblem:

    def __init__(self):
        self.initial_state = None
    
    def get_random_state(self):
        raise Exception("Not Implemented")

    def is_goal(self, state):
        raise Exception("Not Implemented")

    def expand(self, state):
        raise Exception("Not Implemented")
    
    def heuristic(self, state):
        raise Exception("Not Implemented")
    
    def display_state(self, state):
        print(state)