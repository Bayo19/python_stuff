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

# default argument values

def ask_ok(prompt, retries = 4, complaint = 'Yes or no, please!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries -1
        if retries < 0:
            raise IOError('uncooperative user')
        print (complaint)

xx = 5

def f(arg = xx):
    print(arg)
xx = 6

f()

def fun(a, L=[]):
    L.append(a)
    return L


print(fun(3))

# keyword argument
def parrot(voltage, state ='a stiff', action ='voom', type='Norwegian Blue'):
    print('-- This parrot wouldn\'t', action, end=' ')
    print('if you put', voltage, 'volts through it')
    print('Lovely plumage, the', type)
    print('-- It\'s', state, '!')

parrot(1000)
parrot(voltage=20000, action='VROOOOOOMYYY', state='sexy', type='Black Steiner' )

# final formal parameter **name

def cheeseshop(kind, *arguments, **keywords):
    print('--Do you have any', kind, '?')
    print('--I\'m sorry, we\'re all out of', kind)
    for arg in arguments:
        print(arg)
    print('-' * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ':', keywords[kw])

cheeseshop('Limburger', 'It\'s very runny, sir', shopkeeper='Michael Palin', client='John Cleese', sketch='Cheese Shop Sketch')

# arbitrary argument lists

def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

def concat(*args, sep='/'):
    return sep.join(args)
print(concat('stein', 'stein', 'stern', sep='$$'))

# Lmbda expressions
def increment(n):
    return lambda x: x + n

f= increment(20)
g = increment(7)
print(g(20))

