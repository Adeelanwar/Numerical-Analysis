import math

def bisection(f, xp, xn, e):
    n = 0
    error = 10000
    xm = 0
    while abs(error) > e and n < 1000:
        if(f(xp) * f(xn) < 0):
            xm = (xp + xn) / 2
            if(f(xp) * f(xm) < 0):
                xn = xm
            elif(f(xm) * f(xn) < 0):
                xp = xm
            n += 1
            print("n = %3d, interval = [%.9f,%.9f],f(xl) = %.9f,f(xr) = %.9f" % (n, xp,xn,f(xp),f(xn)))
        else:
            print('root either doesnt exist or there are even number of roots in this interval')
            break
        
        error = (xn - xp) / xn
        
    if error < e and n >= 100:
        n = -1
    return xm, n
def f(x):
    return (math.e)**x + math.sin(x) - 4

solution, niter = bisection(f,1,2, e=10**-4)

if niter > 0:
    print ("Number of iterations: %d" % (niter))
    print ("A solution is: %0.9f" % (solution))
else:
    print ("Solution not found!")
