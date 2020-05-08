# using Lists as Stacks

stack = [2]
stack.append(6)
stack.append(7)
print(stack.pop())

# using Lists as Queues
from collections import deque
queue = deque(['Eric', 'John', 'Michael'])
queue.append('Terry')
queue.append('Stein')

print(queue.popleft())

# List comprehensions
squares = []
for x in range(11):
    squares.append(x**2)
print(squares[1:])

# same thing as above 
squares2 = [x**2 for x in range(11)]
print(squares2[1:])

#same thing as above 2
squares3 = list(map(lambda x: x**2, range(11)))
print(squares3[1:])

# more list  comprehension