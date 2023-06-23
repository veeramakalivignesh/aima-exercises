from queue import PriorityQueue

# frontier: [((state, path_cost, parent_state), eval)]
# expand_result: (to_state, edge_cost) 

class BestFirstSearch:

    def __init__(self):
        self.search_history = {}
        self.frontier = PriorityQueue()
        self.reached_goal_state = None
        self.nodes_expanded = 0

    def is_goal(self, state):
        raise Exception("Not Implemented")

    def expand(self, state):
        raise Exception("Not Implemented")

    def evaluate(self, current_state, to_state, edge_cost):
        raise Exception("Not Implemented")

    def perform_search(self, initial_state):
        self.frontier.put((0, (initial_state, 0, None)))

        while not self.frontier.empty():
            _, (current_state, path_cost, parent_state) = self.frontier.get()
            self.search_history[current_state] = (path_cost, parent_state)

            if(self.is_goal(current_state)):
                self.reached_goal_state = current_state
                break
            
            expand_result = self.expand(current_state)
            self.nodes_expanded += 1
            for (to_state, edge_cost) in expand_result:
                if(to_state in self.search_history):
                    old_path_cost, _ = self.search_history[to_state]
                    if(old_path_cost <= path_cost + edge_cost):
                        continue
                eval = self.evaluate(current_state, to_state, edge_cost)
                self.frontier.put((eval, (to_state, path_cost + edge_cost, current_state)))

    def get_solution(self):
        if(self.reached_goal_state is None):
            raise Exception("Goal not yet found")
        
        solution_path = [self.reached_goal_state]
        while True:
            _, parent_state = self.search_history[solution_path[0]]
            if(parent_state is None):
                break
            else:
                solution_path.insert(0, parent_state)
        
        path_cost, _ = self.search_history[self.reached_goal_state]

        return (path_cost, solution_path)

    def display_state(self, state):
        print(state)

    def display_solution(self):
        path_cost, solution_path = self.get_solution()
        print("cost = " + str(path_cost))
        for state in solution_path:
            self.display_state(state)
    
    def display_stats(self):
        path_cost, solution_path = self.get_solution()
        print("solution cost: " + str(path_cost))
        print("solution depth: " + str(len(solution_path) - 1))
        print("no. of states visited: " + str(len(self.search_history.keys())))
        print("no. of nodes expanded: " + str(self.nodes_expanded))