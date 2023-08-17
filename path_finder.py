from math import sqrt
from search_problem import SearchProblem

# obstacles: [vertiex_list]
class PathFinder(SearchProblem):

    def __init__(self, start, goal):
        super().__init__()
        self.initial_state = start
        self.goal_state = goal
        self.obstacles = [
            [(2.22,2.46), (4.62,1.8), (5.7,3.46), (4,6), (2.18,4.42)],
            [(6.56,2.24), (7.46,5.2), (8.06,2.22)],
            [(8.72,5.98), (10.5,5.8), (10.84,5.04), (8.76,4.18)],
            [(11.65,6.64), (13.34,6.7), (13.4,3.1), (11.65,3.11)],
            [(14,6), (14.51,6.86), (15.5,6.34), (14.74,3.03)],
            [(13.73,2.53), (14.62,1.65), (14.58,0.34), (13.64,-0.36), (12.57,0.45), (12.53,1.67)],
            [(11.76,1.72), (10.63,0.20), (9.97,2.7)],
            [(3,1), (9.48,1), (9.46,-1.37), (2.93,-1.39)]
        ]

    def is_goal(self, state):
        return state == self.goal_state
    
    def point_edge_parity(point, edge):
        x, y = point
        (x1, y1), (x2, y2) = edge
        return (y - y1) * (x2 - x1) - (x - x1) * (y2 - y1)
    
    def are_intersecting(edge1, edge2):
        if(PathFinder.point_edge_parity(edge1[0], edge2) * PathFinder.point_edge_parity(edge1[1], edge2) >= 0):
            return False
        if(PathFinder.point_edge_parity(edge2[0], edge1) * PathFinder.point_edge_parity(edge2[1], edge1) >= 0):
            return False
        return True
    
    def length(edge):
        (x1, y1), (x2, y2) = edge
        return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
    
    def generate_edge_set(obstacle):
        edge_set = set()
        for i in range(0, len(obstacle)):
            if(i < len(obstacle)-1):
                edge_set.add((obstacle[i], obstacle[i+1]))
            else:
                edge_set.add((obstacle[i], obstacle[0]))
        return edge_set
    
    def is_path_possible(self, point1, point2):
        for obstacle in self.obstacles:
            edge_set = PathFinder.generate_edge_set(obstacle)
            for edge in edge_set:
                if PathFinder.are_intersecting((point1, point2), edge):
                    return False
        return True

    def expand(self, state):
        expand_result = []
        for obstacle in self.obstacles:
            edge_set = PathFinder.generate_edge_set(obstacle)
            if state in obstacle:
                for vertex in obstacle:
                    if (state, vertex) in edge_set or (vertex, state) in edge_set:
                        expand_result.append((vertex, PathFinder.length((state, vertex))))
            else:
                for vertex in obstacle:
                    if self.is_path_possible(state, vertex):
                        expand_result.append((vertex, PathFinder.length((state, vertex))))
        
        if self.is_path_possible(state, self.goal_state):
            expand_result.append((self.goal_state, PathFinder.length((state, self.goal_state))))
        return expand_result
    
    def heuristic(self, state):
        return PathFinder.length((state, self.goal_state))
    
# from path_finder import PathFinder
# obj = PathFinder(1,1,(-6.75,12.24),(22.69,-4.4))
# obj.perform_search()
# obj.display_solution()