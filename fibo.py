# modules
def fibo(n):
    res = []

    if n == 0:
        res.append(n)
    elif n == 1:
        res.extend([0,1])
    else:
        res.extend([0,1])
        for i in range(n):
            res.append(res[-1] + res[-2])
    return res
        
print(fibo(10))