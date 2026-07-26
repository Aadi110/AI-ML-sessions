#loops

# for i in range(6):
#     for j in range(i):
#         print('*', end=' ' )
#     print()#breaks line

# for i in range(7):
#     for j in range(i):
#         print('*', end=' ' )
#     print()#breaks line
# print("*")
# print("*")
# print("*")
# print("*")

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * * * 
# *
# *
# *
# *


# for i in range(6):
#     for j in range(6-i):
#         print("*", end=' ')
#     print()





# for i in range(6):
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print()




# for i in range(5):
#     for j in range(i):
#         print(" ", end=' ')
        
#     for j in range(5-i):
#             print("*", end=' ')
#     print()
    
    
    
    
# for i in range(5):
#     for j in range(i):
#         print(" ", end='')
        
#     for j in range(5-i):
#             print("*", end=' ')
#     print()

    # * * * * * 
    #  * * * * 
    #   * * * 
    #    * * 
    #     * 
    
    
    
# for i in range(6):
#     for j in range(6-i):
#         print(" ", end='')
        
#     for j in range(i):
#             print("*", end=' ')
#     print()
    
#      * 
#     * * 
#    * * * 
#   * * * * 
#  * * * * * 





# n=5 
# for i in range (n):           #i controls the row number
#     for j in range(n-i-1):    #j controls 
#         print(" ", end=" ")
#     for k in range(2*i+1):
#         print("*", end=" ")
#     print()
    
# for i in range (n-2, -1, -1):           
#     for j in range(n-i-1):    
#         print(" ", end=" ")
#     for k in range(2*i+1):
#         print("*", end=" ")
#     print()
    
    
    
    
    
    
    
    
    
    
    
    
    
n = 5

# for i in range(n):
#     # Print leading spaces
#     for j in range(n - i - 1):
#         print(" ", end=" ")

#     # Print hollow pyramid
#     for k in range(2 * i + 1):
#         if k == 0 or k == 2 * i or i == n - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
