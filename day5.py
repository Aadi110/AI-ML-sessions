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

def employee(**details):
    for key, value in details.items():
        print(key,"=", value)
employee(Name="Aadi", Department="Developer", salary=500000, Country="Nepal")
