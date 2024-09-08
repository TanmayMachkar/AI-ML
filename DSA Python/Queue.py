#using list
s = []
s.insert(0, 'Tanmay')
s.insert(0, 'Tejas')
s.insert(0, 'Macho')
print(s.pop())
print(s)

#using deque
from collections import deque
q = deque()
q.appendleft(5)
q.appendleft(78)
q.appendleft(23)
print(q)
print(q.pop())
print(q)