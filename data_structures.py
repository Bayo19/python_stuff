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
#nested list comprehension

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

trans = [[row[i] for row in matrix] for i in range(4)]
print(trans)

# same as

# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])

# print(transposed)

# same as
transposed = []
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)

# in the real world we can use the zip function

# del statement

a = [-1, 1, 66.25, 250, 333, 1234.5]

def something(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            del a[i]
            return arr
print(something(a, 66.25))

# the del statement can be used to delete a whole variable

# tuples and sequences
t = 0, 1, 1, 2, 3, 5, 8, 13, 21
# otherwise as (0, 1, 1, 2, 3, 4, 8, 13, 21)
print(t)

#nested tuples
u = ((123, 456, 'hello'),(1, 2, 3, 4, 5))
print(u)

# dictionary

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
# dict constructor
mash = dict([('john', 444), ('stein', 000), ('hamm', 202020)])
#dict comprehension
print(sorted(mash.keys()))
print(mash)

# more comprehensions
new_list = [n*n for n in range(0, 15) if n%2 == 0]
print(new_list)
#letter number pair
letnum = [(letter, num) for letter in 'abcd' for num in range(4)]
print(letnum)

