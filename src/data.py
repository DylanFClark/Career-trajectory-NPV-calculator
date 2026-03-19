import pandas as pd

cli = pd.read_csv("../data/cpi_data.csv")

print(cli.columns)

#drop unessesairy columns
to_drop = ["DGUID", "SYMBOL", "DECIMALS", "TERMINATED"]
cli = cli.drop(columns=to_drop)


#remove GEO we don't want
provinces = ["Saskatchewan", "Manitoba", "British Columbia", "Alberta", "Prince Edward Island", "Ontario", "Quebec", "Newfoundland and Labrador"]
cli = cli[cli["GEO"].isin(provinces)]


#remove non-selected cost areas
cost_areas = ["Private transportation", "Natural gas", "Housing (1986 definition)", "Food", "Energy"]
cli = cli[cli["Products and product groups"].isin(cost_areas)]

print(cli)

#cli = cli[cli[""]]




