import gym
import pandas as pd
import numpy as np


#数据预处理
stock_price=pd.read_csv('../data/all_stocks_5yr.csv')
stock_price_col=stock_price.pivot_table(index='date',columns='Name',values=['open','close'])
index_factor=pd.read_excel('../data/index_nav.xlsx')
index_factor_col=index_factor.pivot_table(index='nav_date',columns='bloomberg_ticker',values=['open','close','volume'])
print(index_factor_col.head())
print(index_factor_col['close']['SPX Index'])














class ra_env(gym.Env):
    def __init__(self):
        #env
        self.fee_buy=0.005

        #state
        self.stock_price=pd.read_csv('data/all_stocks_5yr.csv')
        self.stock=self.stock_price['Name'].unique()
        self.n=len(self.stock_price['Name'].unique())
        
        self.stock_price['trade_price']=self.stock_price['open']
        self.stock_price_col=self.stock_price.pivot_table(index='date',columns='Name',values='close')
        self.index_price=pd.read_csv('')

        self.len=len(self.stock_price['name'].unique())
        self.pfo=np.array([0])*self.len
        self.state=self.price+self.pfo
        #timeindex 2 int
        self.time_step=self.stock_price['date'].sort().unique()

        self.pfo=[0]*self.n
        self.asset=1000000
        #action
        self.action=[0]*self.n
        
        #reward
        self.reward=0


    def find_state(time_step):
        
        return 0

    def step(self,action):
        #action->switch portfolio; action to reward,state
        trade_list=action-self.pfo
        trade_fee=trade_list[trade_list>0].sum()*self.asset*self.fee_buy

        #change state
        self.time_step+=timedelta(day=1)

        reward=action*(self.state['close']/self.state['open']).sum()*self.asset-trade_fee
        done=True

        self.time_step+=1
        self.state=find_state(time_step)


        return self.state,reward,done,{}

    def reset(self):
        return self.state

    def render(self):
        return None
    
    def close(self):
        return None
