import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/zanzibar-real-state.csv")
print("df type:", type(df))
print("df shape:", df.shape)
df.head()

# 3 categories of data: location, categorical, and numeric. Each of these require a different kind of exploration in our analysis.
# a good way to visualize Location data is to create a scatter plot on top of a map. A great tool for this is the scatter_mapbox from the plotly library.
# Use plotly express to create figure
fig = px.scatter_mapbox(
    df,  # Our DataFrame
    lat="lat",
    lon="lon",
    center={"lat": 19.43, "lon": -99.13},  # Map will be centered on Mexico City
    width=600,  # Width of map
    height=600,  # Height of map
    hover_data=["price_usd"],  # Display price when hovering mouse over house
)

# Add mapbox_style to figure layout
fig.update_layout(mapbox_style="open-street-map")

# Show figure
fig.show()

# categorical
df["state"].nunique()
df["state"].unique()
df["state"].value_counts()

# numerical , descriptive statistics
# Describe "area_m2", "price_usd" columns
df[["area_m2","price_usd"]].describe()
plt.hist(df["area_m2"]);

plt.xlabel("Area [sq meters]")
plt.ylabel("Frequency")
plt.title("Distribution of House Sizes");


# Use Matplotlib to create boxplot of "area_m2"

plt.boxplot(df["area_m2"],vert=False)
plt.xlabel("Area [sq meters]")
plt.title("Distribution of Home Sizes");


# Use Matplotlib to create histogram of "price_usd"
plt.hist(df["price_usd"])
plt.xlabel("Price [USD]")
plt.ylabel("Frequency")
plt.title("Distribution of Home Prices");


