#file handling

# file= open("fruits.txt" , "r")
# # content = file.read()
# # print(content)

# for line in file:
#     print(line.strip())             #line by line
# file.close()


# file= open("students.txt" , "w")
# file.write("Ram")
# file.write("\nShyam")
# file.write("\nHari")
# file.write("\nSita")
# file.close

# print("file created")




# file= open("students.txt" , "a")
# file.write("Ramayana")

# file.close

# print("file updated")


#with open is used for closing in new python updated programming 

import csv
with open("students.csv" , "r") as file:
    # reader = csv.reader(file)
    # for row in reader:
    #     print(row)
        
        
        

    reader=csv.reader(file)
    next(reader)
    for row in reader:
        name = row[0]
        math=int(row[1])                    #typecasting for int because csv has string value
        science=int(row[2])
        english=int(row[3])
        average=(math+science+english)/3
        print(name , average)