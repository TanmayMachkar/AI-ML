#using list
s = ['Tanmay', 'Macho', 'Machkar', 'Tejas']
print(s)
s.pop()
print(s)

#using deque
from collections import deque
stack = deque()
stack.append('Tanmay')
stack.append('Tejas')
stack.append('Macho')
print(stack)
stack.pop()
print(stack)