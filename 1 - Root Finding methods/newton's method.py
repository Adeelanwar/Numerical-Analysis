import math
from sympy import *
x = symbols('x')
f = exp(x) + sin(x) - 4
dfdx = lambdify(x, diff(f, x))
f = lambdify(x, f)

def Newton(f, dfdx, x, e):
    n = 0
    x = [x]
    error = 100000
    while abs(error) > e and n < 100:
        try:
            x.append(x[n] - float((f(x[n])/dfdx(x[n]))))
        except ZeroDivisionError:
            print ("Error! - derivative zero for xn = ", x[n])
            break
        error = (x[n + 1] - x[n]) / x[n + 1]
        n += 1
    if error < e and n >= 100:
        n = -1
    return x, n


solution, niter = Newton(f, dfdx, x=1, e=10**-8)

if niter > 0:    # Solution found
    print ("Number of iterations: %d" % (niter))
    print ("A solution is: %0.12f" % (solution[niter]))
else:
    print ("Solution not found!")


##def Newton(f, dfdx, x, e):
##    n = 0
##    x = [x]
##    error = 100000
##    while abs(error) > e and n < 100:
##        try:
##            x.append(x[n] - float((f(x[n])/dfdx(x[n]))))
##        except ZeroDivisionError:
##            print ("Error! - derivative zero for xn = ", x[n])
##            break
##        error = (x[n + 1] - x[n]) / x[n + 1]
##        n += 1
##    if error < e and n >= 100:
##        n = -1
##    return x, n
##
##def f(x):
##    return (math.e)**x + math.sin(x) - 4
##
##def dfdx(x):
##    return (math.e)**x + math.sin(x)
##
##solution, niter = Newton(f, dfdx, x=1, e=10**-4)
##
##if niter > 0:    # Solution found
##    print ("Number of iterations: %d" % (niter))
##    print ("A solution is: %0.12f" % (solution[niter]))
##else:
##    print ("Solution not found!")
