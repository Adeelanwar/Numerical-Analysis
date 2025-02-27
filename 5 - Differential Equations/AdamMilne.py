import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

usedmethod = "None"

def MilneS(f, t, y, n):
    usedmethod = "Milne-Simpson"
    h = t[1] - t[0]
    for i in range(4, n):
        dy = list(f(np.array(t[i-4 :i]),np.array(y[i - 4:i])))
        yp = y[i - 3] + h * (4 / 3) * (2 * dy[-1] - dy[-2] + 2 * dy[-3])
        t.append(t[i - 1] + h)
        dy.append(f(t[-1],yp))
        y.append(y[i - 2] + h * (1 / 3) * (dy[-1] + 4 * dy[-2] + dy[-3]))
    draw(t, y)
    return t, y

def Adamb(f, t, y, n):
    usedmethod = "Adam-Bashforth"
    h = t[1] - t[0]
    for i in range(4, n):
        dy = list(f(np.array(t[i-4 :i]),np.array(y[i - 4:i])))
        yp = y[i - 1] + h * (1 / 24) * (55 * dy[-1] - 59 * dy[-2] + 37 * dy[-3] - 9 * dy[-4])
        t.append(t[i - 1] + h)
        dy.append(f(t[-1],yp))
        y.append(y[i - 1] + h * (1 / 24) * (9 * dy[-1] + 19 * dy[-2] - 5 * dy[-3] + 1 * dy[-4]))
    draw(t, y)
    return t, y

def f(x, y):
    return (x + y) / 2

def draw(t ,y):
        fig, ax = plt.subplots()
        ax.plot(t, y, color = 'red', label = usedmethod + " Approximation")
        sol = integrate.solve_ivp(f, (t[0], t[-1]), [y[0]],t_eval=np.linspace(t[0], t[-1], 1000))
        ax.plot(sol.t, sol.y[0], color = 'blue', label = 'Actual function')
        ax.set(xlabel='t', ylabel='y', title= usedmethod + ' Method')
        ax.legend()
        plt.show()

t = [0, 0.5, 1, 1.5]
y = [2, 2.636, 3.595, 4.968]
Adamb(f, t, y, 10)[1]
