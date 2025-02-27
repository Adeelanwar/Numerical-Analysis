from sympy import *
import numpy as np

def picard(f, x0, y0, xn, n):
    val = [0] * n
    g = integrate(f.subs(y, y0),(x, x0, x))
    val[0] = y0 + g.subs(x, xn)
    #print("y{} = {} + {}, y{}({}) = {}".format(1, y0, g , 1, xn, val[0]))
    for i in range(1, n):
        g = integrate(f.subs(y, g),(x, x0, x))
        val[i] += y0 + g.subs(x, xn)
        #print("y{} = {} + {}, y{}({}) = {}".format(i + 1, y0, g , i + 1, xn, val[i]))
    return val

x, y = symbols('x y')
f = x + y**2
print(picard(f,0, 0, 0.3, 10))

