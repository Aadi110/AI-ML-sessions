import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Load the dataset

df= pd.read_csv('day14/business_data.csv')
print ("Original Shape:", df.shape)

# Clean Category Column
df["Category"] = df["Category"].astype("string")

df["Category"] = df["Category"].str.strip()  # Remove leading/trailing whitespace

df["Category"] = df["Category"].str.title()

df["Category"] = df["Category"].replace({"I.T.": "IT","It":"IT", "Information Technology": "IT"})

#Clean Total_Amount Column
df["Total_Amount"] = pd.to_numeric(df["Total_Amount"], errors='coerce')  # Convert to numeric, set errors to NaN

#Remove missing values:
df=df.dropna(subset=["Total_Amount", "Category"])  # Drop rows where Total_Amount or Category is NaN

#Check cleaned categories values:
print("\nCleaned Category Values:")
print(df["Category"].value_counts())

#Group Sales by Categories:
category_sales = df.groupby("Category")["Total_Amount"].sum()
print("\nSales by Category:")
print(category_sales)

#Convert pandas data to numpy arrays:
categories = category_sales.index.to_numpy()
sales = category_sales.to_numpy()

#Numpy Analysis:
total_sales = np.sum(sales)
average_sales = np.mean(sales)
highest_sales = np.max(sales)
lowest_sales = np.min(sales)
highest_index = np.argmax(sales)
highest_category = categories[highest_index]

#Display Results:
print("\nTotal Sales: ${:,.2f}".format(total_sales))
print("Average Sales per Category: ${:,.2f}".format(average_sales))
print("Highest Sales: ${:,.2f} in Category: {}".format(highest_sales, highest_category))
print("Lowest Sales: ${:,.2f} in Category: {}".format(lowest_sales, categories[np.argmin(sales)]))
print("Top Selling Category: {}".format(highest_category))

#Visualize using Matplotlib:
plt.figure(figsize=(10, 6))
plt.bar(categories, sales)
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.title("Sales by Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()