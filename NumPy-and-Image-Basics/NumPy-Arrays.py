import numpy as np

my_list = [0,1,2,3,4]
print(type(my_list))
print(my_list)
arr = np.array(my_list)
print(type(arr))
print(arr)
arr1 = np.arange(0,10)
print(arr1)
arr2 = np.arange(0,10,2)
print(arr2)
mat = np.zeros((5,5))
print(mat)
mat1 = np.ones((2,4))
print(mat1)
np.random.seed(101) 
arr = np.random.randint(0,100,10)
arr2 = np.random.randint(0,100,10)
arr.max()
arr.min()
arr.mean()
arr.argmin()
arr.argmax()
arr.reshape(2,5)
mat = np.arange(0,100).reshape(10,10)
row = 0
col = 1
mat[row,col]
mat[:,col]
mat[row,:]
mat[0:3,0:3]
