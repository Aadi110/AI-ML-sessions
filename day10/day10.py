import pandas as pd


#pandas helps in data cleaning and data framing

# marks=pd.Series([80,75,90,85,95])
# print(marks)


# series=pd.Series([100,200,300,400,500])
# print(series)

# student = {
#     "name": ["Aaditya", "Ram", "Shyam", "Hari", "Sita"],
#     "age": [21,22,23,24,25],
#     "maths":[80,75,90,85,95]
# }

# df=pd.DataFrame(student)
# print(df)

# print(df.head(2)) #first 2 rows from 0 to 2     ,    default prints 5 rows from 0
# print(df.tail(2)) #last 2 rows                  ,    default prints 5 rows from last

# print(df[['name','maths']]) #to print specific columns


# print(df.loc[1]) #to print specific row
# print(df.loc[1:3]) #to print specific row from this to that
# print(df.iloc[1:3]) #to print specific row from this to that n-1






# employee = {
#     "name": ["Aaditya", "Ram", "Shyam", "Hari", "Sita", "Gita", "Rita", "Misti", "Aadi", "Ravi" ],
#     "Department": ["Developer", "Manager", "Developer", "Tester", "Designer", "Manager", "UI/UX", "Developer", "Designer", "Manager"],
#     "salary":[10000,20000,30000,40000,None,60000,70000,80000,90000,100000]
# }

# df=pd.DataFrame(employee)
# print(df)


# print(df.columns)
# print(df.shape)
# print(df.dtypes)
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.isnull())
# print(df.describe())
# print(df.fillna(0, inplace=True))               # fill 0 for none data filtering
# print(df.dropna())                              #removed row with none data cleaning

df=pd.read_csv("day10/employee.csv")
print(df)
