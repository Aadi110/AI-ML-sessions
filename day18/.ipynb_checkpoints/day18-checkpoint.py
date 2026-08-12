import pandas as pd

data = {
    "Customers": ["A","B","C","D","E","F","G","H","I","J","K","L"],
    "Annual_Income": [25,28,30,32,45,48,50,52,70,75,78,80],
    "Spending_Score": [20,25,22,28,50,55,52,58,80,85,82,88]
}

df= pd.DataFrame(data)
print (df)
