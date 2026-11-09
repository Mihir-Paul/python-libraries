import pandas as pd

data = [100,102,104,200,202,204]

series = pd.Series(data,index=['a','b','c','d','e','f'])

print(series[series>=200])