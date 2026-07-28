def student_marksheet():
    s_name = input("Enter student name: ")

    s1 = float(input("Enter marks in English: "))
    s2 = float(input("Enter marks in Mathematics: "))
    s3 = float(input("Enter marks in Science: "))
    s4 = float(input("Enter marks in Computer: "))

    sum = s1 + s2 + s3 + s4
    percentage = sum / 4

    print("\nSTUDENT MARKSHEET")
    print("Student Name:", s_name)
    print("English:", s1)
    print("Mathematics:", s2)
    print("Science:", s3)
    print("Computer:", s4)
    print("Total Marks:", sum)
    print("Percentage:", percentage, "%")

student_marksheet()
