import gym
import pandas as pd

class ra_env(gym.Env):
    def __init__(self):
        self.stock_price=pd.read_csv('data/all_stocks_5yr.csv')

    def step(self,action):

        return self.state,reward,done,{}

    def reset(self):
        return self.state

    def render(self):
        return None
    
    def close(self):
        return None
