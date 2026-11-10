import pandas as pd 

df = pd.read_csv("pandas module/csv_modification/pokemon.csv",index_col="Name")

pokemon = input("Enter a Pokemon:")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")