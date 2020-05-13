# first class functions

def square(x):
    return x * x 

def my_map(func, array):
    result = []
    for i in array:
        result.append(func(i))
    return result

squares = my_map(square, [2,4,6,8])

print(squares)

#----------------------------------------------
def cube(x):
    return x * x * x 