import gym
import pandas as pd
import numpy as np

class ra_env(gym.Env):
    def __init__(self):
        self.stock_price=pd.read_csv('data/all_stocks_5yr.csv')
        self.len=len(self.stock_price['name'].unique())
        self.pfo=np.array([0])*self.len
        self.state=self.price+self.pfo
        
    def step(self,action):

        return self.state,reward,done,{}

    def reset(self):
        return self.state

    def render(self):
        return None
    
    def close(self):
        return None
