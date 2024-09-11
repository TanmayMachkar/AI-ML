import numpy as np

n = np.array([6, 7, 8])
print(n[0:2])
print(n[-1])
a = np.array([[6, 7, 8], [1, 2, 3], [9, 3, 2]])
print(a[1, 2])
print(a[0:2, 2])
print(a[-1])
print(a[-1, 0:2])
print(a[:, 1:3]) # : -> all rows

for cell in a.flat:
    print(cell)
    
a = np.arange(6).reshape(3, 2)
b = np.arange(6, 12).reshape(3, 2)
print(a)
print(b)
print(np.vstack((a,b)))
print(np.hstack((a, b)))
c = a > 2
print(c)
print(a[c]) #returned only those values where condition is true