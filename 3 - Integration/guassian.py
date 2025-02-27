import numpy as np
from math import *

import matplotlib
import matplotlib.pyplot as plt

from numpy import linalg



def gaussian(f, a, b, n = 1):
    
    if n == 1:
        x = np.array([0])
        t = ((b - a) * x + (b + a)) / 2
        w = [2]
    if n == 2:
        x = np.array([1 / sqrt(3), -1 / sqrt(3)])
        t = ((b - a) * x + (b + a)) / 2
        w = [1, 1]
    if n == 3:
        x = np.array([0, sqrt(3 / 5), -sqrt(3 / 5)])
        t = ((b - a) * x + (b + a)) / 2
        w = [8/9, 5/9, 5/9]
    if n == 4:
        x = np.array([sqrt((3 / 7) - (2 / 7) * sqrt(6 / 5)), -sqrt((3 / 7) - (2 / 7) * sqrt(6 / 5)), sqrt((3 / 7) + (2 / 7) * sqrt(6 / 5)), -sqrt((3 / 7) + (2 / 7) * sqrt(6 / 5))])
        t = ((b - a) * x + (b + a)) / 2
        w = [(18 + sqrt(30))/ 36, (18 + sqrt(30))/ 36, (18 - sqrt(30))/ 36, (18 - sqrt(30))/ 36]

    y = 0
    ylist = []
    for i in range(n):
        y += w[i] * f(t[i])
        ylist.append(w[i] * f(t[i]))


    #ploting the actual function and approximated function filling between the curves
    fig, ax = plt.subplots()
    func = draw(x, ylist, a, b)
    x = np.arange(a, b, (b - a) / 100)
    fx = f(x)
    ax.plot(x, fx, color = 'black', label = 'Actual function')
    ax.fill_between(x, fx, color = 'red', label = 'Area under the curve')
    ax.plot(x, func, color = 'Blue', label = 'Approximated Function')
    ax.fill_between(x, fx, func,color = 'green', label = 'Approximated area under the curve')
    ax.set(xlabel='x', ylabel='y', title='Guassian Quadrature Method')
    plt.legend()
    fig.savefig("%d.png" %(n))
    plt.show()
    
    return y
    
def draw(x, y, a, b):
    xvals = np.arange(a, b, (b - a) / 100)
    func = np.zeros(len(xvals))
    if len(x) == 1:
        for i in range(len(xvals)):
            func[i] = y[0]
    n = len(x)
    if len(x) >= 2:
        coef = Dmatrix(x, y)
        index = 0
        for xval in xvals:
            for i in range(n):
                func[index] += coef[i] * xval**(n - i - 1)
            index += 1
    return func
    
def Dmatrix(x, y):
    n = len(x)
    matrix = np.zeros([n, n])
    b = np.matrix(y).T
    for i in range(n):
        for j in range(n):
            matrix[i, n - j - 1] = x[i]**j
    return np.linalg.solve(matrix, b)

def f(x):
    return -x**2 - 1

gaussian(f, -1, 1,4)
        
    

