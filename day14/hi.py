import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv("day14/business_data.csv")

# -----------------------------
# Data Cleaning
# -----------------------------

# Clean Category
df["Category"] = df["Category"].astype("string")
df["Category"] = df["Category"].str.strip()
df["Category"] = df["Category"].str.title()

# Convert numeric columns
df["Total_Amount"] = pd.to_numeric(df["Total_Amount"], errors="coerce")
df["Customer_Satisfaction"] = pd.to_numeric(df["Customer_Satisfaction"], errors="coerce")
df["Loyalty_Score"] = pd.to_numeric(df["Loyalty_Score"], errors="coerce")

# Fill missing values
df["Total_Amount"] = df["Total_Amount"].fillna(df["Total_Amount"].median())
df["Customer_Satisfaction"] = df["Customer_Satisfaction"].fillna(df["Customer_Satisfaction"].median())
df["Loyalty_Score"] = df["Loyalty_Score"].fillna(df["Loyalty_Score"].median())

df["Category"] = df["Category"].fillna("Unknown")
df["Sales_Channel"] = df["Sales_Channel"].fillna("Unknown")

# Remove remaining missing values
df = df.dropna()

# -----------------------------
# Create Satisfaction Groups
# -----------------------------
def Satisfaction_Level(score):
    if score <= 2:
        return "Low"
    elif score == 3:
        return "Medium"
    else:
        return "High"

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