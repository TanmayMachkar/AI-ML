import numpy as np
import time
import sys

l = range(1000)
print(sys.getsizeof(5) * len(l))

array = np.arange(1000) #range from 0 to 999
print(array.size * array.itemsize) # size - total size of array and itemsize - sizeof one item

size = 1000000

l1 = range(size)
l2 = range(size)

a1 = np.arange(size)
a2 = np.arange(size)

#python list
start = time.time()
result = [(x + y) for x, y in zip(l1, l2)]
print("Python list took ", (time.time() - start) * 1000)

#numpy array
start = time.time()
result = a1 + a2
print("Numpy array took ", (time.time() - start) * 1000)
