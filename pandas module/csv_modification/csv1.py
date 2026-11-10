import pandas as pd 

df = pd.read_csv("pandas module/csv_modification/pokemon.csv")

print(df[["Name","Type1","Type2"]].to_string())