from environment import Environment
from agent import Agent

class VacumEnvironment(Environment):
    agent_position = 0
    grid = [0,0]

    def update_performance_measure(self):
        self.performance_measure += 2 - self.grid[0] - self.grid[1]
    
    def perform_action(self, action):
        if(action == 'LEFT'):
            if(self.agent_position > 0):
                self.agent_position -= 1
                self.performance_measure -= 1
        elif(action == 'RIGHT'):
            if(self.agent_position < 1):
                self.agent_position += 1
                self.performance_measure -= 1
        elif(action == 'SUCK'):
            self.grid[self.agent_position] = 0
        elif(action == 'NOOP'):
            pass
        else:
            raise Exception('Invalid Action: ' + action)
    
    def get_percept(self):
        if(self.grid[self.agent_position] == 0):
            return [self.agent_position, 'CLEAN']
        else:
            return [self.agent_position, 'DIRTY']
    
    def describe_environment(self):
        print('')
        print('time_step: ' + str(self.time_step))
        print('performance_measure: ' + str(self.performance_measure))
        print('agent_position: ' + str(self.agent_position))
        print('grid: ' + str(self.grid))
        print('')

class VacumAgent(Agent):
    initial_square_done = False

    def agent_program(self, percept):
        if(percept[1] == 'DIRTY'):
            return 'SUCK'
        elif(percept[0] == 0):
            if(self.initial_square_done):
                return 'NOOP'
            else:
                self.initial_square_done = True
                return 'RIGHT'
        else:
            if(self.initial_square_done):
                return 'NOOP'
            else:
                self.initial_square_done = True
                return 'LEFT'