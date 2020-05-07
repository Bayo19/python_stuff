width = 20
height = 5 * 9

word = 'lexxical'
# for i in range(len(word)):
squares = [1,4,9,16,25]
new_squares = squares + [36,49,64,81,100]
print(new_squares)

# a sorting algorithm

def sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array.pop()
        left = []
        right = []
        for i in range(len(array)):
            if pivot < i:
                left.append(i)
            else:
                right.append(i)
        return sort(left) + [pivot] + sort(right)

print(sort(new_squares))



