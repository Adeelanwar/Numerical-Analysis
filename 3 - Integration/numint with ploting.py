import numpy as np

import matplotlib
import matplotlib.pyplot as plt

from scipy import linalg

x = np.array([-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12])
def f(x):
    return np.sin(x)


class numint:
    def __init__(self, x, f):
        self.x = x
        self.y = f(x)
        self.n = len(x)
        self.h = x[1] - x[0]
        self.answer = 0
        self.method = {'trap': self.trap, 'simpson': self.simpson, '3/8': self.simpson38, 'boole': self.booles}
        
    def solve(self, method):
        return self.method[method](self.x, self.y)
        
        
    def trap(self, x, y):
        self.draw(x, y, 2)
        self.answer = 0
        string = 'integration of y from %g to %g = %g / %d * (' %(self.x[0], self.x[-1], self.h, 2)
        for i in range(1 , self.n):
            self.answer += y[i - 1] + y[i]
            string += '%g + %g + ' %(y[i - 1], y[i])
        self.answer *= self.h / 2
        string = string[:-3] + ') = %g' %(self.answer)
        print(string)
        return self.answer
        
    def simpson(self, x, y):
        self.draw(x, y, 3)
        if self.n % 2 == 1 and self.n >= 3:
            self.answer = 0
            string = 'integration of y from %g to %g = %g / %d * (' %(self.x[0], self.x[-1], self.h, 3)
            for i in range(2 , self.n, 2):
                self.answer += y[i - 2] + 4 * y[i - 1] + y[i]
                string += '%g + 4 * %g + %g + ' %(y[i - 2], y[i - 1], y[i])
            self.answer *= self.h / 3
            string = string[:-3] + ') = %g' %(self.answer)
            print(string)
        else:
            print('incorrect no of datapoints')
        return self.answer
        

    def simpson38(self, x, y):
        self.draw(x, y, 4)
        if self.n % 3 == 1 and self.n >= 4:
            self.answer = 0
            string = 'integration of y from %g to %g = %g / %d * (' %(self.x[0], self.x[-1], 3 * self.h, 8)
            for i in range(3, self.n, 3):
                self.answer += y[i - 3] + 3 * y[i - 2] + 3 * y[i - 1] + y[i]
                string += '%g + 3 * %g + 3 * %g + %g + ' %(y[i - 3], y[i - 2], y[i - 1], y[i])
            self.answer *= 3 * self.h / 8
            string = string[:-3] + ') = %g' %(self.answer)
            print(string)
        else:
            print('incorrect no of datapoints')
        return self.answer

    def booles(self, x, y):
        self.draw(x, y, 5)
        if self.n % 4 == 1 and self.n >= 5:
            self.answer = 0
            string = 'integration of y from %g to %g = %g / %d * (' %(self.x[0], self.x[-1], 2 * self.h, 45)
            for i in range(4, self.n, 4):
                self.answer += 7 * y[i - 4] + 32 * y[i - 3] + 12 * y[i - 2] + 32 * y[i - 1] + 7 * y[i]
                string += '7 * %g + 32 * %g + 12 * %g + 32 * %g + 7 * %g + ' %(y[i - 4], y[i - 3], y[i - 2], y[i - 1], y[i])
            self.answer *= 2 * self.h / 45
            string = string[:-3] + ') = %g' %(self.answer)
            print(string)
        else:
            print('incorrect no of datapoints')
        return self.answer
    
    def draw(self, x, y, n):
        fig, ax = plt.subplots()
        for i in range(n, self.n + 1, n - 1):
            print(i)
            xvals = np.linspace(x[1], x[n], num = 100,  ) + (i - n - 1) * self.h
            func = np.zeros(len(xvals))
            coef = self.Dmatrix(x[(i - n):i], y[(i - n):i])
            print(coef)
            index = 0
            for xval in xvals:
                for j in range(n):
                    func[index] += coef[j] * xval**(n - j - 1)

                index += 1
            
            ax.plot(xvals, f(xvals), color = 'red')
            ax.plot(xvals, func, color = 'green')
            ax.fill_between(xvals, func, color = 'grey')
        ax.set(xlabel='x', ylabel='y', title='Integration')
        
        for k in range(0, self.n, n - 1):
            ax.plot([x[k],x[k]], [0, y[k]], color = 'black')
        ax.plot(x,[0] * self.n, color = 'black')
        ax.plot(x, y, 'bo')
        plt.grid()
        fig.savefig("%d.png" %(n))
        plt.show()
    
    def Dmatrix(self, x, y):
        n = len(x)
        matrix = np.zeros([n, n])
        b = np.matrix(y).T
        for i in range(n):
            for j in range(n):
                matrix[i, n - j - 1] = x[i]**j
        return np.linalg.solve(matrix, b)

            
integration = numint(x , f)
integration.solve('trap')
integration.solve('simpson')
integration.solve('3/8')
integration.solve('boole')
