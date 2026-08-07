import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data={
    "Hours":[1,2,3,4,5,6,7,8,9,10],
    "Marks":[35,40,45,50,55,60,65,70,80,90]
}

df= pd.DataFrame(data)
X= df[["Hours"]]
Y= df["Marks"]
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


# print("Training Data:")
# print(X_train)

# print("Testing Data:")
# print(X_test)


model = LinearRegression()
model.fit(X_train, y_train)

predictions= model.predict(X_test)

print("Actual:", y_test.values)
print("Predicted:", predictions)

