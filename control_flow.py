# if STATEMENTS
# x = int(input('Please enter something: '))

# if x < 0:
#     x = 0
#     print('Negative changed to zero')
#     print(x)
# elif x == 0:
#     print('Zero')
#     print(x)
# elif x == 1:
#     print('Single')
#     print(x)
# else:
#     print('More ...')
#     print(x)

# for STATEMENTS

words = ['cat', 'window', 'inspiration']

# for word in words:
#     print(word, len(word))

# # range() FUNCTION

# for i in range(5, 12, 2):
#     print(i)

# for i in range(10):
#     print(i)

# for i in range(1,6):
#     print(i**i)

# print(list(range(1,6)))

# loops

for n in range(2,10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

# the above is some weird maths shit