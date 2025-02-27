import math

def f(x):
    return x - math.cos(x)

# f(x)=0 coverted to x = g(x)
def g(x):
    return math.cos(x)

def fixedpoint(x0,f, g,e = 10**-4):
    n = 1
    is_convergent = True
    error = 10000
    while abs(error) > e:
        x1 = g(x0)
        error = abs((x1 - x0) / x0)
        print('Iteration = %2d, x%d = %0.16f and f(x%d) = %0.16f' % (n,n, x1, n, f(x1)))
        x0 = x1
        n += 1
        if n > 100:
            is_convergent = False
            break
    if is_convergent == True:
        print('Required root is: %0.8f' % x1)
    else:
        print('Not Convergent.')
fixedpoint(-1, f, g)
