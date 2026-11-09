import pandas as pd 

calories ={"Day1":1700,"Day2":2300,"Day3":1900}

series = pd.Series(calories)

series.loc['Day3']+=500

print(series)