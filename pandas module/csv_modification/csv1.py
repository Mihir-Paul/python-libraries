import pandas as pd 

df = pd.read_csv("pandas module/csv_modification/pokemon.csv",index_col="Name")

print(df.loc["Charizard":"Pikachu",["Type1","Height","Weight"]])

print(df.iloc[0:11,0:3])