import math
def secant(f, x0, x1, e):
    n = 1
    x = [x0, x1]
    error = 10000
    while abs(error) > e and n < 100:
        try:
            x.append(x[n] - float(f(x[n]) * (x[n] - x[n - 1])/ (f(x[n]) - f(x[n - 1]))))
        except ZeroDivisionError:
            print ("Error! - denominator zero for xn =", x[n],', xn - 1 =',x[n - 1])
            n = -1
            break
        error = (x[n + 1] - x[n]) / x[n + 1]
        n += 1
    if error < e and n >= 100:
        n = -1
    return x[n], n

def f(x):
    return (math.e)**x + math.sin(x) - 4

solution, niter = secant(f,x0 = 1,x1 = 2, e=10**-6)

if niter > 0:    # Solution found
    print ("Number of iterations: %d" % (niter))
    print ("A solution is: %0.12f" % (solution))
else:
    print ("Solution not found!")
