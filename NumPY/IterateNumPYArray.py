import numpy as np

a = np.arange(12).reshape(3, 4)
print(a)

for cell in a.flatten():
    print(cell)

#C order
for x in np.nditer(a, order = 'C'):
    print(x)

#Fortran order
for x in np.nditer(a, order = 'F'):
    print(x)

for x in np.nditer(a, order = 'F', flags = ['external_loop']):
    print(x)  

for x in np.nditer(a, op_flags = ['readwrite']):
    x[...] = x * x
    print(x)
    
b = np.arange(3, 15, 4).reshape(3, 1)
print(b)

#iterating two arrays at the same time
for x, y in np.nditer([a, b]):
    print(x, y)