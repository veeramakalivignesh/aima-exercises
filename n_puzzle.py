from random import sample
from a_star_search import AStartSearch

class NPuzzle(AStartSearch):

    def __init__(self, cost_wight, heuristic_weight, n):
        super().__init__(cost_wight, heuristic_weight)
        self.n = n
        self.initial_state = ((7,2,4),(5,0,6),(8,3,1))

    def in_range(self, i, j):
        return i < self.n and i >= 0 and j < self.n and j >= 0

    def randomize_initial_state(self):
        self.reset()
        state_input = sample({0, 1, 2, 3, 4, 5, 6, 7, 8}, 9)
        state_config = []
        for i in range(0, self.n):
            state_config.append([])
            for j in range(0, self.n):
                state_config[i].append(state_input[3*i + j])
        self.initial_state = tuple([tuple(item) for item in state_config])


    def is_goal(self, state):
        return state == ((0,1,2),(3,4,5),(6,7,8))
    
    def expand(self, state):
        x = None
        y = None
        for i in range(0, len(state)):
            for j in range(0, len(state[0])):
                if(state[i][j] == 0):
                    x = i
                    y = j
                    break
            if (x is not None):
                break
        
        state_config = [list(item) for item in state]
        expand_result = []
        
        if(self.in_range(x, y+1)):
            num = state_config[x][y+1]
            state_config[x][y] = num
            state_config[x][y+1] = 0
            new_state = tuple([tuple(item) for item in state_config])
            expand_result.append((new_state,1))
            state_config[x][y+1] = num
            state_config[x][y] = 0
        
        if(self.in_range(x+1, y)):
            num = state_config[x+1][y]
            state_config[x][y] = num
            state_config[x+1][y] = 0
            new_state = tuple([tuple(item) for item in state_config])
            expand_result.append((new_state,1))
            state_config[x+1][y] = num
            state_config[x][y] = 0
        
        if(self.in_range(x, y-1)):
            num = state_config[x][y-1]
            state_config[x][y] = num
            state_config[x][y-1] = 0
            new_state = tuple([tuple(item) for item in state_config])
            expand_result.append((new_state,1))
            state_config[x][y-1] = num
            state_config[x][y] = 0

        if(self.in_range(x-1, y)):
            num = state_config[x-1][y]
            state_config[x][y] = num
            state_config[x-1][y] = 0
            new_state = tuple([tuple(item) for item in state_config])
            expand_result.append((new_state,1))
            state_config[x-1][y] = num
            state_config[x][y] = 0
        
        return expand_result
    
    def heuristic(self, state):
        result = 0
        for i in range(0,self.n):
            for j in range (0, self.n): 
                result += abs(state[i][j]//self.n - i) + abs(state[i][j]%self.n - j)
        return result

    def display_state(self, state):
        for row in state:
            for num in row:
                print(num, end=' ')
            print('')
        print('')

# from n_puzzle import NPuzzle
# obj = NPuzzle(1,1,3)
# obj.initial_state = ((0, 7, 2), (3, 8, 4), (6, 5, 1))
# obj.perform_search()
# obj.display_stats()