''' The company wants to understand whether customer satisfaction is related to sales performance.
Management wants to know:
Do customers with higher satisfaction scores tend to generate higher-value purchases?
use the "business_data.csv" dataset.
Columns to use:
Customer_Satisfaction
Total_Amount
Category
Sales_Channel
Loyalty_Score

Task to do:
Load Data
Clean the data in category
Clean missing values as well
Create Satisfaction Groups (Satisfaction_level: 1-2=low, 3= Medium, 4-5=high)
Analyze sales by satisfaction level and category 
Plot the results '''







import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("day14/business_data.csv")
print(df.columns)

df["Category"]=df["Category"].astype("string")
df["Category"] = df["Category"].str.strip() 
df["Category"] = df["Category"].str.title()


# Convert numeric columns
df["Total_Amount"] = pd.to_numeric(df["Total_Amount"],errors="coerce") #coerce means ignore errors #convert to numeric, set errors to NaN
df["Customer_Satisfaction"] = pd.to_numeric(df["Customer_Satisfaction"],errors="coerce")
df["Total_Amount"] = df["Total_Amount"].fillna(df["Total_Amount"].median())
df["Loyalty_Score"] = df["Loyalty_Score"].fillna(df["Loyalty_Score"].median())
df["Category"]=df["Category"].fillna("unknown")
df["Sales_Channel"]=df["Sales_Channel"].fillna("unknown")
# print(df.isnull().sum())

df.dropna(inplace=True)  #drop rows where Category or Total_Amount is missing


def Satisfaction_Level(score):
    if score <= 2:
        return "low"
    elif score == 3:
        return "medium"
    else:
        return "high"


df["Satisfaction_Level"] = df["Customer_Satisfaction"].apply(Satisfaction_Level)

# -----------------------------
# Analyze Sales
# -----------------------------
sales_analysis = df.groupby(
    ["Satisfaction_Level", "Category"]
)["Total_Amount"].sum()

print("\nSales by Satisfaction Level and Category:")
print(sales_analysis)

# Convert to table format
sales_table = sales_analysis.unstack(fill_value=0)

print("\nPivot Table:")
print(sales_table)

# -----------------------------
# NumPy Analysis
# -----------------------------
sales_array = sales_table.to_numpy()

print("\nTotal Sales:", np.sum(sales_array))
print("Average Sales:", np.mean(sales_array))
print("Highest Sales:", np.max(sales_array))

# -----------------------------
# Plot
# -----------------------------
sales_table.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Sales by Satisfaction Level and Category")
plt.xlabel("Satisfaction Level")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.legend(title="Category")
plt.tight_layout()
plt.show()

