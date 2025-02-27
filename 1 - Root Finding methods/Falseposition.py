import math
def falseposition(f, xl, xr, e):
    n = 0
    error = 10000
    xm = 0
    while abs(error) > e and n < 1000:
        if(f(xl) * f(xr) < 0):
            xm = xr - (f(xr) * (xr - xl))/ (f(xr) - f(xl))
            if(f(xl) * f(xm) < 0):
                xr = xm
            elif(f(xm) * f(xr) < 0):
                xl = xm
            n += 1
            print("n = %3d, interval = [%.9f,%.9f],f(xl) = %.9f,f(xr) = %.9f" % (n, xl,xr,f(xl),f(xr)))
        else:
            print('root either doesnt exist or there are even number of roots in this interval')
            break
        error = (f(xm))
    if error < e and n >= 100:
        n = -1
    return xm, n
def f(x):
    return (math.e)**x + math.sin(x) - 4

solution, niter = falseposition(f,1,2, e=10**-6)

if niter > 0:
    print ("Number of iterations: %d" % (niter))
    print ("A solution is: %0.9f" % (solution))
else:
    print ("Solution not found!")

