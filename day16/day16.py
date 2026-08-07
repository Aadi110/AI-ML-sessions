# import pandas as pd
# from sklearn.model_selection import train_test_split
# #from sklearn.linear_model import LinearRegression
# from sklearn.ensemble import RandomForestRegressor
# data={
#     "Hours":[1,2,3,4,5,6,7,8,9,10],
#     "Marks":[35,40,45,50,55,60,65,70,80,90]
# }

# df= pd.DataFrame(data)
# X= df[["Hours"]]
# Y= df["Marks"]
# X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


# # print("Training Data:")
# # print(X_train)

# # print("Testing Data:")
# # print(X_test)

# # model = LinearRegression()
# model = RandomForestRegressor()              #to decide which algo to use to train this model
# model.fit(X_train, y_train)             #always needed

# predictions= model.predict(X_test)

# print("Actual:", y_test.values) 
# print("Predicted:", predictions)

# new_student = pd.DataFrame({
#     "Hours": [10]
# })
# print("Study Hours: ",new_student["Hours"].iloc[0] )
# print("Predicted Marks:", predictions[0])



'''
A school has collected data about students' study hours and their final marks. 
Your task is to build a ML Model that predicts the marks of a new student based on their study hours.
Given Data:
Study Hours         Marks
1                      35

12                     95


'''



import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# from sklearn.ensemble import RandomForestRegressor
data={
    "Hours":[1,2,3,4,5,6,7,8,9,10,11,12],
    "Marks":[35,40,45,50,55,60,65,70,75,80,85,90]
}

df= pd.DataFrame(data)
X= df[["Hours"]]
Y= df["Marks"]
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = LinearRegression()
# model = RandomForestRegressor()              #to decide which algo to use to train this model
model.fit(X_train, y_train)             #always needed

predictions= model.predict(X_test)

print("Actual:", y_test.values) 
print("Predicted:", predictions)

new_student = pd.DataFrame({
    "Hours": [10]
})
print("Study Hours: ",new_student["Hours"].iloc[0] )
print("Predicted Marks:", predictions[0])