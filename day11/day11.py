#data cleaning


import  pandas as pd
# df = pd.read_csv("day11/datacleaning.csv")
# # print(df.head(10))
# # print(df.shape)
# # print(df.info)
# # print(df.describe)

# df["Age"]=df["Age"].fillna(df["Age"].median)    #fillig null value in age, median is used to avoid outliars
# print(df.isnull().sum())



# df["Gender"]=df["Gender"].fillna("unknown")
# print(df.isnull().sum())



# missing=df["Customer_ID"].isna()
# df.loc[missing,"Customer_ID"]=[f"CUST{1000+i}" for i in range(missing.sum())]
# print(df.isnull().sum())


# df["Unit_Price"]=df["Unit_Price"].fillna(df["Unit_Price"].median)
# print(df.isnull().sum())


# df.to_csv("business_data.csv",index=False)                    #saves new data
df = pd.read_csv("day11/business_data.csv")
# print(df.info)

df["Total_Amount"]=df["Quantity"]*df["Unit_Price"]
print(df.head())
