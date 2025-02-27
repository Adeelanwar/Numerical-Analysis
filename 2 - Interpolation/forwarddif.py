import numpy as np

##xvals = [200 , 250, 300, 350, 400]
##yvals = [15.04, 16.81, 18.42, 19.90, 21.27]
xvals = [2,4,6,8,10]
yvals = [4,15,33,56,90]
x = 2.5


def table(x, y):
    n = len(x)
    ftable = np.zeros((n + 1, n))
    ftable[0, :] = x
    ftable[1, :] = y
    for i in range(n - 1,0, -1):
        for j in range(i):
            ftable[n + 1 - i,j] = ftable[n - i,j + 1] - ftable[n - i,j]
    return ftable

def drawtable(table):
    n = len(table[0,:])
    for i in range(n):
        for j in range(n - i + 1):  
            print('%g' % (table[j, i]), end = "\t");  
        print("");  

def forwarddif(xvals, yvals, x):
    ftable = table(xvals, yvals)
    drawtable(ftable)
    n = len(xvals)
    h =  xvals[1] - xvals[0]
    u = (x - xvals[0]) / h
    y = ftable[1, 0]
    string = 'y(%g) = %g + ' %(x, ftable[1, 0])
    cofu = [1]
    for i in range(n):
        cofu.append(cofu[i] * (u - i) / (i + 1))
    for i in range(1, n):
        string += '%g * %g + ' %(cofu[i], ftable[i + 1, 0])  
        y += ftable[i + 1, 0] * cofu[i]
    print(string[:-2], '= %g' %(y))
    return y
forwarddif(xvals, yvals, x)


    
