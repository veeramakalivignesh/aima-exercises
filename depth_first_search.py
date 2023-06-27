from search_problem import SearchProblem
from time import time

class DepthFirstSearch:

    def __init__(self, search_problem: SearchProblem):
        self.search_problem = search_problem
        self.search_history = {}
        self.frontier_stack = []
        self.max_frontier_size = 0
        self.reached_goal_state = None
        self.nodes_visited = 0
        self.ils_iterations = 0
        self.ils_limit = None
        self.time_taken = None
        self.search_complete = False

    def reset(self, randomize_input=False):
        if(randomize_input):
            self.search_problem.initial_state = self.search_problem.get_random_state()
        self.search_history = {}
        self.frontier_stack = []
        self.max_frontier_size = 0
        self.reached_goal_state = None
        self.nodes_visited = 0
        self.ils_iterations = 0
        self.time_taken = None
        self.search_complete = False
    
    def is_parent(self, state, to_state):
        _, parent_state = self.search_history[state]
        while parent_state is not None:
            if(parent_state == to_state):
                return True
            _, parent_state = self.search_history[parent_state]
        return False

    def remove_explored_nodes(self, state, ancestor_state):
        _, parent_state = self.search_history[state]
        del self.search_history[state]
        while parent_state is not ancestor_state:
            state = parent_state
            _, parent_state = self.search_history[state]
            del self.search_history[state]

    def dfs(self, cost_limit):
        if(self.search_problem.initial_state is None):
            raise Exception("Initial state not set")
        
        self.frontier_stack.append((self.search_problem.initial_state, 0, None))
        while not len(self.frontier_stack) == 0:
            self.max_frontier_size = max(self.max_frontier_size, len(self.frontier_stack))
            current_state, path_cost, parent_state = self.frontier_stack.pop()
            self.search_history[current_state] = (path_cost, parent_state)

            if(self.search_problem.is_goal(current_state)):
                self.search_complete = True
                self.reached_goal_state = current_state
                break
            
            expand_result = self.search_problem.expand(current_state)
            is_leaf = True
            for (to_state, edge_cost) in expand_result:
                self.nodes_visited += 1
                if((cost_limit >= 0) and (path_cost + edge_cost > cost_limit)):
                    if self.ils_limit is None:
                        self.ils_limit = path_cost + edge_cost
                    else:
                        self.ils_limit = min(self.ils_limit, path_cost + edge_cost)
                    continue
                if(self.is_parent(current_state, to_state)):
                    continue
                is_leaf = False
                self.frontier_stack.append((to_state, path_cost + edge_cost, current_state))
            
            if (len(self.frontier_stack) > 0) and is_leaf:
                _, _, ancestor_state = self.frontier_stack[-1]
                self.remove_explored_nodes(current_state, ancestor_state)
    
    def perform_dfs(self, cost_limit=-1):
        start = time()

        self.dfs(cost_limit)
        if(cost_limit == -1):
            self.search_complete = True

        end = time()
        self.time_taken = end - start
    
    def perform_ils(self):
        start = time()

        while self.reached_goal_state is None:
            if(self.ils_iterations == 0):
                new_ils_limit = 0
            else:
                new_ils_limit = self.ils_limit
            self.search_history = {}
            self.ils_limit = None
            self.dfs(new_ils_limit)
            self.ils_iterations += 1
        self.search_complete = True

        end = time()
        self.time_taken = end - start
    
    def get_solution(self):
        if not self.search_complete:
            raise Exception("Goal not yet found")
        
        if(self.reached_goal_state is None):
            return (-1,[])

        solution_path = [self.reached_goal_state]
        while True:
            _, parent_state = self.search_history[solution_path[0]]
            if(parent_state is None):
                break
            else:
                solution_path.insert(0, parent_state)
        
        path_cost, _ = self.search_history[self.reached_goal_state]

        return (path_cost, solution_path)

    def display_solution(self):
        path_cost, solution_path = self.get_solution()
        if(len(solution_path) == 0):
            print("Solution does not exist")
            return
        print("cost = " + str(path_cost))
        for state in solution_path:
            self.search_problem.display_state(state)
    
    def display_stats(self):
        path_cost, solution_path = self.get_solution()
        print("memory usage:")
        print("     max frontier size: " + str(self.max_frontier_size))
        print("     max state history size: " + str(len(self.search_history)))
        print("time:")
        print("     time taken: " + str(round(self.time_taken, 2)) + " seconds")
        print("     no. of nodes visited: " + str(self.nodes_visited))
        print("")
        print("solution cost: " + str(path_cost))
        print("solution depth: " + str(len(solution_path) - 1))
        print("no. of ILS iterations: " + str(self.ils_iterations))
        if(self.reached_goal_state is None):
            print("goal found: None")
        else:
            print("goal found:\n")
            self.search_problem.display_state(self.reached_goal_state)
