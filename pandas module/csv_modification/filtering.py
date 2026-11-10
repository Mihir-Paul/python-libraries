import pandas as pd 

data = pd.read_csv("pandas module/csv_modification/pokemon.csv",index_col="Name")

tall_pokemon = data[data["Height"]>=2.0]
heavy_pokemon = data[data["Weight"]>=100]
legendary_pokemon = data[data["Legendary"]==True]
water_pokemon = data[(data["Type1"]=='Water') & (data["Type2"]=='Water')]

print(water_pokemon)