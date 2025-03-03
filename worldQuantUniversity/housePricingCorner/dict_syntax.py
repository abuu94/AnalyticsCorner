house_0_dict = {
    "price_approx_usd": 115910.26,
    "surface_covered_in_m2": 128,
    "rooms": 4,
}

# add price per m2 in dictionary
house_0_dict["price_per_m2"]=house_0_dict[price_approx_usd]/house_0_dict[surface_covered_in_m2]
house_0_dict

# list of dictionary : it does well for rowwise calculation , but complicated for columnwise eg to get mean price of all house ..!!
houses_rowwise = [
    {
        "price_approx_usd": 115910.26,
        "surface_covered_in_m2": 128,
        "rooms": 4,
    },
    {
        "price_approx_usd": 48718.17,
        "surface_covered_in_m2": 210,
        "rooms": 3,
    },
    {
        "price_approx_usd": 28977.56,
        "surface_covered_in_m2": 58,
        "rooms": 2,
    },
    {
        "price_approx_usd": 36932.27,
        "surface_covered_in_m2": 79,
        "rooms": 3,
    },
    {
        "price_approx_usd": 83903.51,
        "surface_covered_in_m2": 111,
        "rooms": 3,
    },
]
for house in houses_rowwise:
  house["price_per_m2"]=house[price_approx_usd]/house[surface_covered_in_m2]

# calculate mean price   Method No 1
house_prices = []
for house in houses_rowwise:
    house_prices.append(house["price_approx_usd"])
mean_house_price = sum(house_prices) / len(house_prices)
mean_house_price


# calculate mean price   Method No 2
houses_columnwise = {
    "price_approx_usd": [115910.26, 48718.17, 28977.56, 36932.27, 83903.51],
    "surface_covered_in_m2": [128.0, 210.0, 58.0, 79.0, 111.0],
    "rooms": [4.0, 3.0, 2.0, 3.0, 3.0],
}
mean_house_price =sum(houses_columnwise["price_approx_usd"])/len(houses_columnwise["price_approx_usd"])


# price and area
price = houses_columnwise["price_approx_usd"]
area=houses_columnwise["surface_covered_in_m2"]
# list(zip(price,area))
price_per_m2=[]
for p,a in zip(price,area):
  price_m2=p/a
  price_per_m2.append(price)
houses_columnwise["price_per_m2"]=price_per_m2
houses_columnwise

# pandas dataframes
import pandas as pd
df_houses = pd.DataFrame(houses_columnwise)
df_houses
