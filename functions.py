def fibonacci(n):
    a = 0
    b = 1
    while a < n:
        print(a, end=' ')
        c = a + b
        a = b
        b = c
        
# fibonacci(70000)

# my version

def fibo(n):
    res = []
    if n == 0:
        res.append(0)
    elif n == 1:
        res.extend([0,1])
    else:
        res.extend([0,1])
        for i in range(0, n - 2):
            res.append(res[-1]+res[-2])
    return res

print(fibo(10))