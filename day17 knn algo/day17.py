# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt


# a=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
# b=np.array([21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40])
# df=pd.DataFrame(a,b)
# # print(df)

# print("Mean of Age: ",df.mean())
# print("Median of Age: ",df.median())
# print("Standard Deviation of Age: ",df.std())

# # plt.axline(df.mean(),df.median(),df.std())
# plt.plot(a,b,color='red',marker='o',linestyle='-')
# plt.show()










import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

from sklearn.tree import DecisionTreeClassifier,plot_tree

import matplotlib.pyplot as plt


data={
   "Hours":[1,2,2,3,3,4,4,5,5,6,6,7,9,9,10],
   "Attendance":[50,55,60,60,65,65,70,70,75,75,80,80,85,90,95],
   "Result":["Fail", "Fail", "Fail", "Fail", "Fail","Pass","Pass","Pass","Pass","Pass","Pass","Pass","Pass","Pass","Pass"]
}


df= pd.DataFrame(data)
# print(df)

#now split

X= df[["Hours", "Attendance"]]
y = df["Result"]

# print(x,y)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


#Selection Model
model= KNeighborsClassifier(n_neighbors=3)


#train
model.fit(X_train, y_train)


#Predict
y_pred = model.predict(X_test)
print(y_pred)

#Check Accuracy #StandardScaler
accuracy= accuracy_score(y_test, y_pred)
print("Accuracy: ", accuracy)


#Now give the new_student data and predict
new_student = pd.DataFrame([[5, 72]], columns=X.columns)
prediction = model.predict(new_student)
print("Prediction", prediction[0])


# Train a decision tree separately for visualization.
tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train, y_train)

# Plot the decision tree.
plt.figure(figsize=(12, 8))

plot_tree(tree_model, feature_names=X.columns, class_names=tree_model.classes_, filled=True)
plt.show()



# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import accuracy_score
# from sklearn.preprocessing import StandardScaler

# data = {
#     "Hours": [1,2,2,3,3,4,4,5,5,6,6,7,9,9,10],
#     "Attendance": [50,55,60,60,65,65,70,70,75,75,80,80,85,90,95],
#     "Result": [
#         "Fail", "Fail", "Fail", "Fail", "Fail",
#         "Pass", "Pass", "Pass", "Pass", "Pass",
#         "Pass", "Pass", "Pass", "Pass", "Pass"
#     ]
# }

# df = pd.DataFrame(data)

# # Split input and output
# X = df[["Hours", "Attendance"]]
# y = df["Result"]

# # Train-test split
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# # Standard Scaling
# scaler = StandardScaler()

# X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test)

# # Select KNN model
# model = KNeighborsClassifier(n_neighbors=3)

# # Train
# model.fit(X_train_scaled, y_train)

# # Predict
# y_pred = model.predict(X_test_scaled)

# print("Predicted:", y_pred)

# # Check accuracy
# accuracy = accuracy_score(y_test, y_pred)
# print("Accuracy:", accuracy)

# # New student data
# new_student = pd.DataFrame(
#     [[5, 72]],
#     columns=X.columns
# )

# # Scale new student using the SAME scaler
# new_student_scaled = scaler.transform(new_student)

# # Predict new student
# prediction = model.predict(new_student_scaled)

# print("Prediction:", prediction[0])