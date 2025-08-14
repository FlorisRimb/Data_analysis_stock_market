"""
This module is responsible for importing data in a database postgresql
"""

#import library
import pandas as pd

file = 'data/stock_market.csv'

data = pd.read_csv(file)

print(data)