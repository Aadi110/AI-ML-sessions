#scope

x =50
# def test():
#     print(x)                            #global variable scope
    
# test()

# def demo():
#     z= 100
#     print(z)                            #local variable scope
# demo()

# print(x)

# def change():
#     global x
#     x=20
#     change()
#     print(x)









#modules


import math                                             #whole function import

from math import pi                                     #specific function import


    

#create shopping.py. Inside this file write following items
# 1. add_item
# 2. show_item
# 3. total_price

# now create another file main.py
# import the functions from shopping.py and run them to add item, display item and calculate price 


#Data Structures

# 1. list:      []
# fruits=["apple", "banana", "guava", "pineapple"]
# print(fruits)

# print(fruits[1:])
# list.append



# 2. tuple:     ()
# no update


# 3. set:       {}



# 4. dictionary:{:}

# key:Value

# key-unique


# students={
#     "BITM":{
#         "student1": {
#              "name":"Aaditya",
#              "class": "BIM",
#                 "marks":{
#                     "english":45, 
#                     "math":55, 
#                     "Nepali":65, 
#                     "Science":75
#                 },
        
#         },
        
#         "student2": {
#             "name":"Aman",
#             "class": "BIM",
#                 "marks":{
#                     "english":45, 
#                     "math":55, 
#                     "Nepali":65, 
#                     "Science":75
#                 },
#         }
#     }
    
# }
# print(students["student1"]["name"])

# Class BIM
# student1
# Marks in subjects

# print(students.get("student1").get("name"))




'''
write a python program to manage the records of 3 students using a nested dictionary 
each student should have the following information:
    -Name
    -Age
    -Faculty
    -Marks in Finance
    -Marks in computer
The program should perform the following tasks:
    1. create a nested dictionary for 3 students
    2. display the details of all student
    3. display the details of a specific student
    4. update the finance marks to 95
    5. calculate and display the total marks of each students
    6. find and display the student who has the highest total marks

'''



# create a nested dictionary for 3 students

students={
        "student1": {
             "name":"Aaditya",
             "age": 21,
             "faculty": "BIM",
             "finance":45, 
             "computer":55, 
        },
        
        "student2": {
            "name":"Anil",
            "age": 22,
            "faculty": "BIM",
            "finance":45, 
            "computer":55, 
        },
        
        "student3": {
            "name":"Amit",
            "age": 22,
            "faculty": "BIM",
            "finance":45, 
            "computer":55, 
                    
                
        }
    }
    


# display the details of all student
print("Details of all students:")
for student_id, details in students.items():
    print(student_id, details)


# display the details of a specific student
print("\nDetails of Student1:")
print(students["student1"])


# update the finance marks to 95 for student1
students["student1"]["finance"] = 95

print("\nAfter updating finance marks of S001:")
print(students["student1"])


# calculate and display total marks of each students
print("\nTotal marks of each student:")

for student_id, details in students.items():
    total = details["finance"] + details["computer"]
    print(details["name"], "=", total)


# find and display the student who has the highest total marks
highest_student = ""
highest_total = 0

for student_id, details in students.items():
    total = details["finance"] + details["computer"]

    if total > highest_total:
        highest_total = total
        highest_student = details["name"]

print("\nStudent with highest total marks:")
print(highest_student, "=", highest_total)