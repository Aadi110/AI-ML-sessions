import numpy as np   #percentile
# arr= np.array([10,20,30,40,50,60,70,80,90,100])
# print(np.percentile(arr,90))                                          #np.percentile(variables,percentile value)
# print(np.mean(arr))

# print(np.quantile(arr,0.25))

 #variance- how much data are close to each others
 
# a= np.array([1,2,3,4,5,6,7,8,9,10])
# b= np.array([1,15,30,45,60,75,90,115,130,145])
# print(np.var(a))                                                      #smaller value the spread of the data is small
# print(np.var(b))                                                      #larger the value the spread of the data is large

#correlation- helps to measure impact,

# hours= np.array([1,2,3,4,5])
# marks1= np.array([30,40,50,60,70])
# marks2= np.array([70,60,50,40,30])
# print(np.corrcoef(hours,marks1))                                       #positive correlations
# print(np.corrcoef(hours,marks2))                                       #negative correlation





    #covariance
# temp=np.array([20,30,35])
# icecream=np.array([200,250,300])

# print(np.cov(temp,icecream)) #positive relation



# linear algebra

# vector
# 1d array is called vector
# vector database



# RAG = vectorization = embedding 1D array 
# LLM # likewise, similar search, semantic search after embedded

# a=np.array([[1,2],[3,4]])
# b=np.array([[5,6],[7,8]])
# print(a+b)
# print(a*b)
# print(a@b)
# print(np.dot(a,b))
# print(a.T)



c=np.array([[4,7],[2,6]])
print(np.linalg.inv(c))                 #inverse matrix to solve equation
print(np.linalg.det(c))                 #determinant to determine the inverse of matrix