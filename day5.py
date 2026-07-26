#positional arguments [*args]

# def add(a,b,c):                            # we passed the position of c as a parameter
#     return a+b+c
# print(add(10,20,30) )


# def add(*numbers):
#     return sum(numbers)
# print(add(10,20,30) )





#all data types ( a, b, *args, **kwargs )




# def fruits(*items):
#     print(items)
# fruits("Apple", "Banana", "Guava", "Pineapple")            #arguments are the actual value that we pass during the function calling



# looping in a function

# def display(*args):
#     for value in args:
#         print(value)
        
# display(10,20,30,40,50)







#develop a function to add unlimited numbers

# def add(*numbers):
#     total=0
#     for a in numbers:
#         total+=a
#     return total

# print(add(10,20))


#real world example

# def shopping_cart(*items):
#     for item in items:
#         print(item)
        
# shopping_cart("Clothes","Shoes","Cap")                                #print only for numeric variables





#   *kwargs keyword arguments                       stores in dictionary value,  key value pairs


# def student(**kwargs):
#     print(kwargs)
# student(name="Aaditya", age=21, city="Sunwal")



# def students(**kwargs):
#     print(kwargs["name"])
#     print(kwargs["age"])
    
# students(name="Aadi", age=21)



# def student(**kwargs):
#     for key,value in kwargs.items():
#         print(key,"=", value)
# student(name="Aadi", age=21)



'''
for key, value in kwargs.items():
for key in kwargs:
for key,value in kwargs.items():
'''

#real world example

# def employee(**details):
#     for key, value in details.items():
#         print(key,"=", value)
# employee(Name="Aadi", Department="Developer", salary=500000, Country="Nepal")


# use *args when you need to accept an unknown number of positional value

#use **kwargs when you need to accept an unknown number of named values eg. detail user information



#lambda functions:
# is a one line of function without a name. Anonymous short function


# def square (x):           with function
#     return x*x
# print(square(5))



#using lambda
# square= lambda x:x*x
# print(square(5))



# multiply = lambda x,y:x*y
# print(multiply(4,3))                        #only for sorting,filtering the function ,for one line only


# def calculate_salary(hours, rate):              #can't use lambda here
#     salary = hours*rate
#     tax = salary*0.1
#     final_salary = salary - tax
#     return final_salary





#sorting data




# student= [
#     ("Ram", 78),
#     ("Hari", 92),
#     ("Sita", 85)
    
# ]
# student.sort(key= lambda student:student[1])
# print(student)









#lambda with map()              map-new iteration with same element | filter-conditional stmt

# marks = [ 50, 60, 70, 80 ]


#add bonus mark 5 to all

# new_marks =[]
# for mark in marks:
#     new_marks.append(mark+5)                #for function
# print (new_marks)



# new_marks=list(map(lambda x:x+5, marks))    #for lambda
# print(new_marks)




#lambda with filter

# passed= list(filter(lambda x:x>60, marks))
# print(passed)




from functools import reduce 
numbers=[10,20,30,40]
total = reduce(lambda x,y:x+y, numbers)
print (total)


# functools 
# reduce-takes 2 values and returns sum