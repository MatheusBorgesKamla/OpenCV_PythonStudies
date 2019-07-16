import numpy as np

my_list = [0,1,2,3,4]
print type(my_list)
print my_list 
arr = np.array(my_list)
print type(arr)
print arr
arr1 = np.arange(0,10)
print arr1
arr2 = np.arange(0,10,2)
print arr2
mat = np.zeros((5,5))
print mat
mat1 = np.ones((2,4))
print mat1
np.random.seed(101) 
arr3 = np.random.randint(0,100,10)
print(arr3)
arr4 = np.random.randint(0,100,10)
print arr4
print "Max = ", arr4.max(), "\nMin = ", arr4.min(), "\nMedia = ", arr4.mean(), "\nPos_min = ", arr4.argmin(), "\nPos_max = ", arr4.argmax()
arr4 = arr4.reshape(2,5)
print arr4
mat = np.arange(0,100).reshape(10,10)
print mat
row = 0
col = 1
print mat[row,col]
print mat[:,col]
print mat[row,:]
print mat[0:3,0:3]
