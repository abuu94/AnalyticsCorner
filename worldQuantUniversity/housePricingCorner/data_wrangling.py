import pandas as pd
df1=pd.read_csv("data/zanzibar_house_1.csv")
df3=pd.read_csv("data/zanzibar_house_2.csv")
df3=pd.read_csv("data/zanzibar_house_3.csv")

# attributes  (property_type, state, lat, lon, area_m2, price_usd )
# (property_type, state, lat, lon, area_m2, price_mxn )
# (property_type, place_with_parent_names, lat-lon, area_m2, price_usd)

# Print df1 shape
df1.shape
df1.info()
df1.head()

# missing values,  use str operators and recasting from object to float
df1.dropna(inplace=True)
df1["price_usd"].str.replace("$","",regex=False).str.replace(",","").astype(float).head()
df1["price_usd"] = (df1["price_usd"]
                    .str.replace("$","",regex=False)
                    .str.replace(",","")
                    .astype(float))


# df2  , drop null value and convert currency to usd dolla
df2.dropna(inplace=True)
df2["price_usd"] =( df2["price_mxn"]/19).round(2)
df2.drop(columns=["price_mxn"],inplace=True)
df2.head()


# df3
# Drop null values from df3
df3.dropna(inplace=True)

# Create "lat" and "lon" columns for df3
df3[["lat", "lon"]] = df3["lat-lon"].str.split(",",expand=True)

# Print object type, shape, and head
print("df3 type:", type(df3))
print("df3 shape:", df3.shape)
df3.head()


# Create "state" column for df3
df3["state"] = df3["place_with_parent_names"].str.split("|",expand=True)

# Drop "place_with_parent_names" and "lat-lon" from df3
df3.drop(columns=["place_with_parent_names","lat-lon"],inplace=True)


# Print object type, shape, and head
print("df3 type:", type(df3))
print("df3 shape:", df3.shape)
df3.head()


# Concatenate df1, df2, and df3
df = pd.concat([df1,df2,df3])

# Print object type, shape, and head
print("df type:", type(df))
print("df shape:", df.shape)
df.head()
