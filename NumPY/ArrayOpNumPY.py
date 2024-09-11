import numpy as np
a = np.array([5, 6, 9])

#2d array
a = np.array([[1, 2], [3, 4], [5, 6]])
print(a.ndim) #print dimension of array
print(a.itemsize) #print size of data used. Here int64 is used therefore o/p will be 8
print(a.dtype) #data type of array here it is int64
a = np.array([[1, 2], [3, 4], [5, 6]], dtype = np.float64) #assign datatype as float64
print(a.itemsize)
print(a)
print(a.size) #size of array/total elements
print(a.shape) #(rows, col)
print(np.zeros((3, 4)))
print(np.ones((3, 4)))
print(np.arange(1, 5))
print(np.arange(1, 5, 2)) #2 is steps
print(np.linspace(1, 5, 10)) #generates 10 numbers btwn 1 and 5 that are linearly spaced
print(a.reshape(2, 3)) #reshape a with 2 rows and 3 cols
print(a.ravel()) #flattens i.e. makes 2d to 1d array
print(a.min())
print(a.max())
print(a.sum())
print(a.sum(axis = 0)) #peforms sum of vertical elements
print(np.sqrt(a))

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(a + b)
print(a * b)
print(a / b)
print(a.dot(b)) #matrix product