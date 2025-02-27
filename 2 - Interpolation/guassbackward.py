import numpy as np 
xvals = [1940,1950,1960,1970,1980,1990]
yvals = [17,20,27,32,36,38]
x = 1976

##xvals = [10,11,12,13,14]
##yvals = [0.23967,0.28060,0.31788,0.35209,0.38368]
##x = 12.2


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

def guassback(xvals, yvals, x):
    ftable = table(xvals, yvals)
    n = len(xvals)
    h =  xvals[1] - xvals[0]
    mid = int(n / 2)
    u = (x - xvals[mid]) / h

    ulist = [1, u]
    num = 1
    for i in range(0,n - 2,2):
        ulist.append(ulist[-1] * (u + num) / (i + 2))
        ulist.append(ulist[-1] * (u - num) / (i + 3))
        num += 1

    y = yvals[mid]
    string = 'y(%g) = %g + ' %(x, ftable[1, mid])

    for j in range(1, n - 1, 2):
        string += '%g * %g + %g * %g + ' %(ulist[j], ftable[j + 1, mid - int((j + 1) / 2)], ulist[j + 1], ftable[j + 2, mid - int((j + 1) / 2)])
        y += ulist[j] * ftable[j + 1, mid - int((j + 1) / 2)] + ulist[j + 1] * ftable[j + 2, mid - int((j + 1) / 2)]
    if n % 2 == 0:
        y += ulist[-1] * ftable[-1, 0]
        string += '%g * %g + ' %(ulist[-1] , ftable[-1, 0])
        
    print(string[:-2], '= %g' %(y))
    return y

