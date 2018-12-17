import pandas as pd
import numpy as np

import torch
import torch.utils.data as dataf


#数据预处理
stock_price=pd.read_csv('../data/all_stocks_5yr.csv')
stock_price_col=stock_price.pivot_table(index='date',columns='Name',values=['open','close'])
index_factor=pd.read_excel('../data/index_nav.xlsx')
index_factor_col=index_factor.pivot_table(index='nav_date',columns='bloomberg_ticker',values=['open','close','volume'])
print(index_factor_col.head())
print(index_factor_col['close']['SPX Index'])