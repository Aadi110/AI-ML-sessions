#while loop


# count=2
# while count<=10:
#     print(count)
#     count+=2



# num=7
# a=0
# while num!=a:
    
#     a=int(input("guess the number"))
   
  
  
  
# i=0
# while i<10:
#       i+=1
#       if i==5:
#           continue
#       print(i)






'''functions'''


# def add(a,b):
#     return a+b
# print(add(5,3))
    
# def name(hello):
#     return hello
# print(name("hello"))




# def calculate_discount(price, discount_percent):
#     if discount_percent <0 or discount_percent>100:
#         raise ValueError("Invalid Discount")
#     return price * (1-discount_percent/100)
# print(calculate_discount(100,50))

    
    
# def c_to_f(c):
#     # pass         #future use
#  return c*1.8+32
# print(c_to_f(0))

# def f_to_c(f):
#     #pass
#  return (f-32)/1.8   
# print(f_to_c(32)) 

# #     args
# #     kwargs
# #     lambda
# #     recursion     --numpy and pandas










def student_marksheet():
    s_name = input("Enter student name: ")

    s1 = float(input("Enter marks in English: "))
    s2 = float(input("Enter marks in Mathematics: "))
    s3 = float(input("Enter marks in Science: "))
    s4 = float(input("Enter marks in Computer: "))

    total = s1 + s2 + s3 + s4
    percentage = total / 4

    print("\nSTUDENT MARKSHEET")
    print("Student Name:", s_name)
    print("English:", s1)
    print("Mathematics:", s2)
    print("Science:", s3)
    print("Computer:", s4)
    print("Total Marks:", total)
    print("Percentage:", percentage, "%")

student_marksheet()         # Calling the function

