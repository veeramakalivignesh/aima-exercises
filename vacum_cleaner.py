from environment import Environment
from agent import Agent

class VacumEnvironment(Environment):
    agent_position = 0
    grid = [0,0]
    bump_sensor_activated = False

    def update_performance_measure(self):
        self.performance_measure += 2 - self.grid[0] - self.grid[1]
    
    def perform_action(self, action):
        if(action == 'LEFT'):
            if(self.agent_position > 0):
                self.agent_position -= 1
                self.performance_measure -= 1
                self.bump_sensor_activated = False
            else:
                self.bump_sensor_activated = True
        elif(action == 'RIGHT'):
            if(self.agent_position < 1):
                self.agent_position += 1
                self.performance_measure -= 1
                self.bump_sensor_activated = False
            else:
                self.bump_sensor_activated = True
        elif(action == 'SUCK'):
            self.grid[self.agent_position] = 0
            self.bump_sensor_activated = False
        elif(action == 'NOOP'):
            self.bump_sensor_activated = False
        else:
            raise Exception('Invalid Action: ' + action)
    
    def get_percept(self):
        if(self.grid[self.agent_position] == 0):
            return [self.bump_sensor_activated, 'CLEAN']
        else:
            return [self.bump_sensor_activated, 'DIRTY']
    
    def describe_environment(self):
        print('')
        print('time_step: ' + str(self.time_step))
        print('performance_measure: ' + str(self.performance_measure))
        print('agent_position: ' + str(self.agent_position))
        print('grid: ' + str(self.grid))
        print('')

class VacumAgent(Agent):
    initial_square_done = False
    prev_movement = ''

    def agent_program(self, percept):
        position = -1
        if(self.prev_movement == 'LEFT'):
            position = 0
        elif(self.prev_movement == 'RIGHT'):
            if(not percept[0]):
                self.initial_square_done = True
            position = 1

        if(percept[1] == 'DIRTY'):
            return 'SUCK'
        elif(position == -1):
            self.prev_movement = 'RIGHT'
            return 'RIGHT'
        elif(position == 0):
            if(self.initial_square_done):
                return 'NOOP'
            else:
                self.initial_square_done = True
                self.prev_movement = 'RIGHT'
                return 'RIGHT'
        else:
            if(self.initial_square_done):
                return 'NOOP'
            else:
                self.initial_square_done = True
                self.prev_movement = 'LEFT'
                return 'LEFT'


# from vacum_cleaner import *
# env = VacumEnvironment()
# env.agent_position = 0
# env.grid = [0,1]
# agent = VacumAgent()
# env.simulate(agent, 1000)