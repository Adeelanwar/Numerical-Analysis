import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

class DE:
    def __init__(self, f, t, y, h, n):
        self.f = f
        self.y = y
        self.t = t
        self.h = h
        self.n = n + 1
        self.y = [0] * (n + 1)
        self.y[0] = y
        self.t = [0] * (n + 1)
        self.t[0] = t
        self.usedmethod = 'None'
        self.method = {'euler': self.Euler, 'rk2': self.RK2, 'rk4': self.RK4, 'modifiedeuler': self.ModifiedEuler, 'improvedeuler': self.ImprovedEuler, 'adam': self.Adamb, 'milne': self.MilneS}
        self.fig, self.ax = plt.subplots()

    def Solve(self, method, draw = False):
        self.method[method](draw)
    
    def cinput(self, f, t, y, h, n):
        self.f = f
        self.y = y
        self.t = t
        self.h = h
        self.n = n + 1
        self.y = [0] * (n + 1)
        self.y[0] = y
        self.t = [0] * (n + 1)
        self.t[0] = t

    def Euler(self, draw = True):
        self.usedmethod = 'Euler'
        for i in range(1, self.n):
            self.y[i] = self.y[i - 1] + self.h * self.f(self.t[i - 1], self.y[i - 1])       
            self.t[i] = self.t[i - 1] + self.h
        if draw == True:
            self.draw(self.t, self.y)
        return self.t, self.y

    def RK2(self, draw = True):
        self.usedmethod = 'RK2'
        for i in range(1, self.n):
            k1 = self.h * self.f(self.t[i - 1], self.y[i - 1])
            k2 = self.h * self.f(self.t[i - 1] + self.h * 0.5, self.y[i - 1] + k1 * 0.5)
            self.y[i] = self.y[i - 1] + k2      
            self.t[i] = self.t[i - 1] + self.h
        if draw == True:
            self.draw(self.t, self.y)
        return self.t, self.y

    def RK4(self, draw = True):
        self.usedmethod = 'RK4'
        for i in range(1, self.n):
            k1 = self.h * self.f(self.t[i - 1], self.y[i - 1])
            k2 = self.h * self.f(self.t[i - 1] + self.h * 0.5, self.y[i - 1] + k1 * 0.5)
            k3 = self.h * self.f(self.t[i - 1] + self.h * 0.5, self.y[i - 1] + k2 * 0.5)
            k4 = self.h * self.f(self.t[i - 1] + self.h, self.y[i - 1] + k3)
            self.y[i] = self.y[i - 1] + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)      
            self.t[i] = self.t[i - 1] + self.h
        if draw == True:
            self.draw(self.t, self.y)
        return self.t, self.y

    def ModifiedEuler(self, draw = True):
        self.usedmethod = 'Modified Euler'
        for i in range(1, self.n):
            k = self.f(self.t[i - 1], self.y[i - 1])
            self.y[i] = self.y[i - 1] + self.h * self.f(self.t[i - 1] + (0.5) * self.h ,self.y[i - 1] + (0.5) * self.h * k)    
            self.t[i] = self.t[i - 1] + self.h
        if draw == True:
            self.draw(self.t, self.y)
        return self.t, self.y
    
    def ImprovedEuler(self, draw = True):
        self.usedmethod = 'Improved Euler'
        for i in range(1, self.n):
            self.y[i] = self.y[i - 1] + (0.5) * self.h * (self.f(self.t[i - 1], self.y[i - 1]) + self.f(self.t[i - 1] + self.h, self.y[i - 1] + self.h * self.f(self.t[i - 1], self.y[i - 1])))    
            self.t[i] = self.t[i - 1] + self.h
        if draw == True:
            self.draw(self.t, self.y)
        return self.t, self.y

    def Adamb(self, draw = True): #not finished
        self.usedmethod = 'Adam-Bashford'
        if self.n >= 4:
            for i in range(1, 4): #Getting First Three values using RK4
                k1 = self.h * self.f(self.t[i - 1], self.y[i - 1])
                k2 = self.h * self.f(self.t[i - 1] + self.h * 0.5, self.y[i - 1] + k1 * 0.5)
                k3 = self.h * self.f(self.t[i - 1] + self.h * 0.5, self.y[i - 1] + k2 * 0.5)
                k4 = self.h * self.f(self.t[i - 1] + self.h, self.y[i - 1] + k3)
                self.y[i] = self.y[i - 1] + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)      
                self.t[i] = self.t[i - 1] + self.h
                
            for i in range(4, self.n):
                dy = list(self.f(np.array(self.t[i-4 :i]),np.array(self.y[i - 4:i])))
                yp = self.y[i - 1] + self.h * (1 / 24) * (55 * dy[-1] - 59 * dy[-2] + 37 * dy[-3] - 9 * dy[-4])
                self.t[i] = self.t[i - 1] + self.h
                dy.append(self.f(self.t[i],yp))
                self.y[i] = self.y[i - 1] + self.h * (1 / 24) * (9 * dy[-1] + 19 * dy[-2] - 5 * dy[-3] + 1 * dy[-4])
            if draw == True:
                self.draw(self.t, self.y)
            return self.t, self.y

    def MilneS(self, draw = True): #not finished
        self.usedmethod = 'Milne-Simpson'
        if self.n >= 4:
            for i in range(1, 4): #Getting First Three values using RK4
                k1 = self.h * self.f(self.t[i - 1], self.y[i - 1])
                k2 = self.h * self.f(self.t[i - 1] + self.h * 0.5, self.y[i - 1] + k1 * 0.5)
                k3 = self.h * self.f(self.t[i - 1] + self.h * 0.5, self.y[i - 1] + k2 * 0.5)
                k4 = self.h * self.f(self.t[i - 1] + self.h, self.y[i - 1] + k3)
                self.y[i] = self.y[i - 1] + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)      
                self.t[i] = self.t[i - 1] + self.h
                
            for i in range(4, self.n):
                dy = list(self.f(np.array(self.t[i-4 :i]),np.array(self.y[i - 4:i])))
                yp = self.y[i - 3] + self.h * (4 / 3) * (2 * dy[-1] - dy[-2] + 2 * dy[-3])
                self.t[i] = self.t[i - 1] + self.h
                dy.append(self.f(self.t[i],yp))
                self.y[i] = self.y[i - 2] + self.h * (1 / 3) * (dy[-1] + 4 * dy[-2] + dy[-3])
            if draw == True:
                self.draw(self.t, self.y)
            return self.t, self.y    
    
    def compare(self, method1, method2, draw = False):
        if draw == False:
            t, y2 = self.method[method2](draw = False)
            y2 = y2[:]
            t, y1 = self.method[method1](draw = False)
        else: 
            ax = self.ax
            t, y2 = self.method[method2](draw = False)
            y2 = y2[:]
            ax.plot(t, y2, color = 'green', label = self.usedmethod + " Approximation")
            t, y1 = self.method[method1](draw = True)
    
        
        print("t\t\t%s\t\t\t%s" %(method1, method2))
        for i in range(self.n):
            print("%g\t\t%.10f\t\t%.10f" %(t[i], y1[i], y2[i]))
    
    def draw(self, t,y):
        ax = self.ax
        ax.plot(t, y, color = 'red', label = self.usedmethod + " Approximation")
        sol = integrate.solve_ivp(self.f, (t[0], t[-1]), [y[0]],t_eval=np.linspace(t[0], t[-1], 1000))
        ax.plot(sol.t, sol.y[0], color = 'blue', label = 'Actual function')
        ax.set(xlabel='t', ylabel='y', title= self.usedmethod + ' Method')
        ax.legend()
        plt.show()
    
##def f(x, y):
##    return 2 - np.exp(-4 * x) - 2 * y
##Diff = DE(f, 0, 1, 1, 10)

def f(x, y):
    return (x + y) / 2 
Diff = DE(f, 0, 2, 0.5, 10)


##def f(x, y):
##    return x
##Diff = DE(f, 0, 1, 0.1, 10)
Diff.compare('adam', 'milne', draw = True)
    
