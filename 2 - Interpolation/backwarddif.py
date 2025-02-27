import numpy as np

##xvals = [200 , 250, 300, 350, 400]
##yvals = [15.04, 16.81, 18.42, 19.90, 21.27]
xvals = [0,1,2,3,4,5]
yvals = [1,2,4,8,16,32]
x = 4.12


def table(x, y):
    n = len(x)
    ftable = np.zeros((n + 1, n))
    ftable[0, :] = x
    ftable[1, :] = y
    for i in range(n - 1,0, -1):
        for j in range(i):
            ftable[n + 1 - i,n - 1 - j] = ftable[n - i,n - j - 1] - ftable[n - i,n - j - 2]
    return ftable

def drawtable(table):
    n = len(table[0,:])
    for i in range(n):  
        print('%g' % (table[0, i]), end ='\t');  
        for j in range(i + 1):  
            print('%g'% (table[n - i, n - 1 - j]),  end ='\t');  
        print("");

def backwarddif(xvals, yvals, x):
    ftable = table(xvals, yvals)
    drawtable(ftable)
    n = len(xvals)
    h =  xvals[1] - xvals[0]
    u = (x - xvals[-1]) / h
    y = ftable[1, n - 1]
    string = 'y(%g) = %g + ' %(x, ftable[1, n - 1])
    cofu = [1]
    for i in range(n):
        cofu.append(cofu[i] * (u + i) / (i + 1))
    for i in range(1, n):
        string += '%g * %g + ' %(cofu[i], ftable[i + 1, n - 1])  
        y += ftable[i + 1, n - 1] * cofu[i]
    print(string[:-2], '= %g' %(y))
    return ftable
ftable = backwarddif(xvals, yvals, x)
