from best_first_search import BestFirstSearch

class AStartSearch(BestFirstSearch):

    def __init__(self, cost_wight, heuristic_weight, search_problem):
        super().__init__(search_problem)
        self.cost_weight = cost_wight
        self.heuristic_weight = heuristic_weight

    def evaluate(self, current_state, to_state, edge_cost):
        path_cost = self.search_history[current_state][0] + edge_cost
        return self.cost_weight * path_cost + self.heuristic_weight * self.search_problem.heuristic(to_state)