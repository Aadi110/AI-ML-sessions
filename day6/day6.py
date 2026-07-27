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


students={
    "student1": {
        "name":"Aaditya",
        "class": "BIM",
        
        "english":45, 
        "math":55, 
        "Nepali":65, 
        "Science":75
        }
    
    
}
# print(students["student1"]["name"])

# Class BIM
# student1
# Marks in subjects

print(students.get("student1").get("name"))




