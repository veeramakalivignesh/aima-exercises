from math import sqrt
from search_problem import SearchProblem

# self.cities = [(i,x,y)]
# state = (visited_cities)
class TravellingSalesman(SearchProblem):

   def __init__(self, cities=None):
      super().__init__()
      self.cities = cities
      if cities is None:
         self.initial_state = None
      else:
         self.initial_state = tuple([cities[0]])

   def process_input(self, file):
      self.cities = []
      with open(file, 'r') as f: 
         line = f.readline()
         while line:
            input = line.split()
            self.cities.append((int(input[0]), float(input[1]), float(input[2])))
            line = f.readline()

      self.initial_state = tuple([self.cities[0]])
         

   def is_goal(self, state):
         return len(state) == len(self.cities) + 1
   
   def length(from_city, to_city):
      (_, x1, y1), (_, x2, y2) = from_city, to_city
      return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
   
   def expand(self, state):
      if len(state) == len(self.cities):
         start_city = self.cities[0]
         visited_cities_list = list(state)
         visited_cities_list.append(start_city)
         to_state = tuple(visited_cities_list)
         current_city = state[-1]
         return [(to_state, TravellingSalesman.length(current_city, start_city))]
      
      expand_result = []
      for city in self.cities:
         if city not in state:
            visited_cities_list = list(state)
            visited_cities_list.append(city)
            to_state = tuple(visited_cities_list)
            current_city = state[-1]
            expand_result.append((to_state, TravellingSalesman.length(current_city, city)))
      return expand_result
   
   def heuristic(self, state):
      return 1

   def display_state(self, state):
      for city in state:
         print(city[0])
