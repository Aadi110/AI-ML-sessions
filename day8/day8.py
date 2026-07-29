 #array=list's replacement

 # 1D array
# a=[10,20,30,40,50]         encapsulate, 
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])


# #2D array
# b=[[1,2,3],[4,5,6],[7,8,9]]
# print(b[0][0])
# print(b[0][1])
# print(b[0][2])
# print(b[1][0])
# print(b[1][1])
# print(b[1][2])
# print(b[2][0])
# print(b[2][1])
# print(b[2][2])



#3D array
# c=[[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]]
# print(c[0][0][0])
# print(c[0][0][1])
# print(c[0][0][2])
# print(c[0][1][0])
# print(c[0][1][1])
# print(c[0][1][2])
# print(c[0][2][0])
# print(c[0][2][1])
# print(c[0][2][2])
# print(c[1][0][0])
# print(c[1][0][1])
# print(c[1][0][2])
# print(c[1][1][0])
# print(c[1][1][1])
# print(c[1][1][2])
# print(c[1][2][0])
# print(c[1][2][1])
# print(c[1][2][2])








# [matrix, linear algebra, statistics]-----Data Science=[ML, Data Analysis],   Big Data

# numpy/numeric python - arithmetic functions

 #axis shows 3d array
import numpy as np
'''
arr=np.array([10,20,30,40,50])

print(arr)
print("Demsion of 1d array: ",arr.ndim)
print("Size of 1d array: ",arr.size)
print("Shape of 1d array: ",arr.shape)
print("Datatype of 1d array: ",arr.dtype)
'''


'''
arr2=np.array([
    [10,2,3],[70,8,4]
    
])

print(arr2)
print("Dimension of 2d array: ",arr2.ndim)
print("Size of 2d array: ",arr2.size)
print("Shape of 2d array: ",arr2.shape)
print("Datatype of 2d array: ",arr2.dtype)

#indexing or accessing arrays

# print(arr2[0])
print("printing row 1: ",arr2[:,1])
'''




# arr3=np.array([
#     [[10,2,3],[70,8,4]],           #layer0              
#     [[1,2,3],[7,8,9]],             #layer1
#     [[1,2,3],[7,8,9]]              #layer2
# ])            


#indexing

# # print(arr3)
# # print("deminsion of 3d array: ",arr3.ndim)
# # print("size of 3d array: ",arr3.size)
# # print("shape of 3d array: ",arr3.shape)
# # print("Datatype of 3d array: ",arr3.dtype)

#slicing

# print("1. ",arr3[:,1,1])              #(layer,row,column)
# print("1.5. ",arr3[:2])
# print("2. ",arr3[1:])
# print("3. ",arr3[:,:2])
# print("4. ",arr3[:,1:])



#indexing or accessing arrays
# array.ndim-dimension
# array.size-size
# array.shape-shape
# array.dtype-datatype



'''
arr=np.array([
    [80,85,90],
    [75,88,92],
    [60,70,95]
])

#slicing
print("1. ",arr[:2])            #before 2
print("2. ",arr[1:])            #row after 1
print("3. ",arr[:,:2])          #column before 2
print("4. ",arr[:,1:])          #column after 1
'''






arr3=np.array([
    [[1,2,3],[4,5,6]],           #layer0              
    [[7,8,9],[10,11,12]],        #layer1
]) 

#slicing
print(arr3[0,:,:])              #layer 0 only row
print(arr3[1,:,:])              #layer 1 only row
print(arr3[:,0,:])              #layer 0 only column
print(arr3[1,0,2])


# print(arr3+10)
# print(arr3*10)



print(np.max(arr3))
print(np.min(arr3))
print(np.mean(arr3))
print(np.sum(arr3))
print(np.std(arr3))