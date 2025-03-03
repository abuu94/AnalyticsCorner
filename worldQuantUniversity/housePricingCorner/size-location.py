# Location or Size: What Influences House Prices in Zanzibar?
# Import 
df = pd.read_csv("data/zanzibar-real-state.csv")
print("df type:", type(df))
print("df shape:", df.shape)
df.head()

# Reaserch Question 1:Which state has the most expensive real estate market?
"""
Je bei inatofautiana baina ya State?
State gani ina bei kubwa ya nyumba?

Now,The next step is to divide our dataset into groups (one per state) and
calculate the mean house price for each group.
"""

mean_price_by_state=df.groupby("state")["pricee_usd"].mean().sort_values(ascending=False)
# Create bar chart from `mean_price_by_state` using pandas
mean_price_by_state.plot(
  kind="bar",
  xlabel="State",
  ylabel="Price [USD]",
  title="Mean House Price by State"
);
# Add new column to the dataset
df["price_per_m2"]=df["price_usd"] /df["area_m2"]
print("df type:", type(df))
print("df shape:", df.shape)
df.head()

# Method chaining
# Group `df` by "state", create bar chart of "price_per_m2"

(
  df
  .groupby("state")
  ["price_per_m2"].mean()
  .sort_values(ascending=False)
  .plot(
    kind="bar",
    xlabel="State",
    ylabel="Mean Price per M^2[USD]",
    title="Mean House Price per M^2 by State"
  )
);

# Research Question 2: Is there a relationship between home size and price?
# Tumeona kuwa location inaathiri bei ya House ktk sehemu ilopita.
# Now let's see if home size can also affect the price ?

"""
A scatter plot forb two columns because itaonesha correlation — in this case, 
if an increase in home size is associated with an increase in price.
"""
plt.scatter(x=df["area_m2"],y=df["price_usd"])
plt.xlabel("Area [sq meters]")
plt.ylabel("Price [USD]")
plt.title("Price vs Area");

"""
 The bigger the house, the higher the price. 
 But how can we quantify this correlation( using numerals)?
 Yes, by using Correlation Co-efficient -1 <= r <= 1
 1 means strong + correlation: As area increase also price increase .
 -1 means area increases price decreases
 0 means no correlation at all.

 Sometime kuna moderate corellation.
"""

p_correlation=df["area_m2"].corr(df["price_usd"])
"""
The correlation coefficient is over 0.5, 
so there's a moderate relationship house size and price. 
But does this relationship hold true in every state?
Let's look at a couple of states.
""
df_morelos=df[df["state"]=="Morelos"]
df_morelos.head()
df_morelos.shape

# Create scatter plot of "price_usd" vs "area_m2" in Morelos
plt.scatter(x=df_morelos["area_m2"],y=df_morelos["price_usd"])
plt.xlabel("Area [sq meters]")
plt.ylabel("Price [USD]")
plt.title("Morelos: price vs. Area");

p_correlation=df_morelos["area_m2"].corr(df_morelos["price_usd"])

# Mexico City
# Create scatter plot of "price_usd" vs "area_m2" in Mexico
df_mexico_city=df[df["state"]=="Distrito Federal"]
plt.scatter(x=df_mexico_city["area_m2"],y=df_mexico_city["price_usd"])
plt.xlabel("Area [sq meters]")
plt.ylabel("Price [USD]")
plt.title("Mexico City: price vs. Area");

p_correlation=df_mexico_city["area_m2"].corr(df_mexico_city["price_usd"])

"""
here's see a weak relationship between size and price
How should we interpret this ? The relationship  haiko sawa kwa states zote 
because there are other factors that have a larger influence on price.
"""
# Tutanya kwaa Latin America city Buenos Aires, Argentina — and build a model that predicts housing price by taking much more than size into account.

