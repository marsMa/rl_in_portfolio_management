import gym

class ra_env(gym.Env):
    def __init__(self):

    def step(self,action):
        return self.state,reward,done,{}

    def reset(self):
        return self.state

    def render(self):
        return None
    
    def close(self):
        return None
