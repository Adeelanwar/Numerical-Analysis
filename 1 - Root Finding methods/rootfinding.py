class root():
    def __init__(self, f, x0, x1, tol = 10**-4):
        self.f = f
        self.x0 = x0
        self.x1 = x1
        self.tol = tol
        self.root = 0
        self.method = {'bisection': self.bisection, 'fp': self.falseposition, 'secant': self.secant}
        self.iter = 0
        self.usedmethod = None
        
    
    def solve(self, method):
        if self.f(self.x0) * self.f(self.x1) > 0:
            print('root either doesnt exist or there are even number of roots in this interval')
        else:
            self.usedmethod = method
            self.method[method](self.f, self.x0, self.x1, self.tol)
            if self.root == None:
                print('%s method was not able to find the root in the interval [%g, %g] in 100 iterations')
            else:
                self.show()
                
    
    def show(self):
        if self.iter != None:
            print ("Method used: %s method" %(self.usedmethod))
            print ("Number of iterations: %d" % (self.iter))
            print ("A solution is: %0.9f" % (self.root))
        else:
            print ("Use the solve function to find the root first!")
    
    def bisection(self, f, xp, xn, e = 10**-4):
        n = 0
        error = 10000
        xm = 0
        while abs(error) > e and n < 100:
            if(f(xp) * f(xn) < 0):
                xm = (xp + xn) / 2
                if(f(xp) * f(xm) < 0):
                    xn = xm
                elif(f(xm) * f(xn) < 0):
                    xp = xm
                n += 1
                #print("n = %3d, interval = [%.9f,%.9f],f(xl) = %.9f,f(xr) = %.9f" % (n, xp,xn,f(xp),f(xn)))
            else:
                n = 1000
                break
            error = (xn - xp) / xn
        if error < e and n >= 100:
            self.root = None
            self.iterations = None
        else:
            self.iter = n
            self.root = xm
            
    def falseposition(self, f, xl, xr, e):
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
                self.root = xm
                #print("n = %3d, interval = [%.9f,%.9f],f(xl) = %.9f,f(xr) = %.9f" % (n, xl,xr,f(xl),f(xr)))
            else:
                break
            error = (f(xm))
        
        if error < e and n >= 100:
            self.root = None
            self.iter = None
        else:
            self.iter = n
            
    def secant(self, f, x0, x1, e):
        n = 1
        x = [x0, x1]
        error = 10000
        while abs(error) > e and n < 100:
            try:
                x.append(x[n] - float(f(x[n]) * (x[n] - x[n - 1])/ (f(x[n]) - f(x[n - 1]))))
            except ZeroDivisionError:
                print ("Error! - denominator zero for xn =", x[n],', xn - 1 =',x[n - 1])
                n = 100
                break
            error = (x[n + 1] - x[n]) / x[n + 1]
            n += 1
        
        if error < e and n >= 100:
            self.root = None
            self.iter = None
        else:
            self.iter = n
            self.root = x[n]

            
    

def f(x):
    return x**2 - 2
a = root(f, 1, 2)
a.solve('fp')
