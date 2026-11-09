import pandas as pd 

data = [100,102,104]

series = pd.Series(data,index = [1,2,3] )
print(series)
series.loc[3]=200 

print(series)

print(series.loc[1])  