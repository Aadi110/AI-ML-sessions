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