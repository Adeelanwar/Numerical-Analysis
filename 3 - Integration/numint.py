from numpy import *
x = array([0,1,2,3,4,5,6,7,8,9,10,11,12])
y = (x)**4 - 4 * (x)**3 + 2 * x + 5
l = x[-1]
print((l**5 / 5) - (l**4) + l**2 + 5 * l)


class numint:
    def __init__(self , x, y):
        self.x = x
        self.y = y
        self.n = len(x)
        self.h = x[1] - x[0]
        self.answer = 0
        self.method = {'trap': self.trap, 'simpson': self.simpson, '3/8': self.simpson38, 'boole': self.booles}
        fig, ax = plt.subplots()
        
    def solve(self, method):
        self.method[method](self.x, self.y)
        
        
    def trap(self, x, y):
        self.answer = 0
        string = 'integration of y from %g to %g = %g / %d * (' %(self.x[0], self.x[-1], self.h, 2)
        for i in range(1 , self.n):
            self.answer += y[i] + y[i - 1]
            string += '%g + %g + ' %(y[i - 1], y[i])
        self.answer *= self.h / 2
        string = string[:-3] + ') = %g' %(self.answer)
        print(string)
        
    def simpson(self, x, y):
        if self.n %2 == 1 and self.n >= 3:
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

    def simpson38(self, x, y):
        self.answer = 0
        string = 'integration of y from %g to %g = %g / %d * (' %(self.x[0], self.x[-1], 3 * self.h, 8)
        for i in range(3, self.n, 3):
            self.answer += y[i - 3] + 3 * y[i - 2] + 3 * y[i - 1] + y[i]
            string += '%g + 3 * %g + 3 * %g + %g + ' %(y[i - 3], y[i - 2], y[i - 1], y[i])
        self.answer *= 3 * self.h / 8
        string = string[:-3] + ') = %g' %(self.answer)
        print(string)

    def booles(self, x, y):
        self.answer = 0
        string = 'integration of y from %g to %g = %g / %d * (' %(self.x[0], self.x[-1], 2 * self.h, 45)
        for i in range(4, self.n, 4):
            self.answer += 7 * y[i - 4] + 32 * y[i - 3] + 12 * y[i - 2] + 32 * y[i - 1] + 7 * y[i]
            string += '7 * %g + 32 * %g + 12 * %g + 32 * %g + 7 * %g + ' %(y[i - 4], y[i - 3], y[i - 2], y[i - 1], y[i])
        self.answer *= 2 * self.h / 45
        string = string[:-3] + ') = %g' %(self.answer)
        print(string)

            
integration = numint(x , y)
integration.solve('trap')
integration.solve('simpson')
integration.solve('3/8')
integration.solve('boole')
