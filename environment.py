from agent import Agent
class Environment:
    performance_measure = 0
    time_step = 0

    def update_performance_measure(self):
        raise Exception("Not Implemented")
    
    def perform_action(self, action):
        raise Exception("Not Implemented")
    
    def get_percept(self):
        raise Exception("Not Implemented")
    
    def describe_environment(self):
        raise Exception("Not Implemented")
    
    def simulate(self, agent: Agent, num_time_steps):
        for i in range(0,num_time_steps):
            self.update_performance_measure()
            percept = self.get_percept()
            action = agent.agent_program(percept)
            # print(action)
            self.perform_action(action)
            self.time_step += 1
        self.describe_environment()