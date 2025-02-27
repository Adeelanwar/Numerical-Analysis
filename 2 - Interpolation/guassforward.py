import numpy as np 
##xvals = [ 1, 2, 3, 4, 5];
##yvals = [1, -1, 1, -1, 1]
##x = 3.5
##xvals = [310, 320, 330, 340, 350, 360]
##yvals = [2.4914, 2.5052, 2.5185, 2.5315, 2.5441, 2.5563]
##x = 337.5

xvals = [2,4,6,8,10]
yvals = [4,15,33,56,90]
x = 6.4

xvals = [10,11,12,13,14]
yvals = [0.23967,0.28060,0.31788,0.35209,0.38368]
x = 12.2

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

def guassfor(xvals, yvals, x):
    ftable = table(xvals, yvals)
    n = len(xvals)
    h =  xvals[1] - xvals[0]
    mid = int((n - 1)/ 2)
    u = (x - xvals[mid]) / h

    ulist = [1, u]
    num = 1
    for i in range(0,n - 2,2):
        ulist.append(ulist[-1] * (u - num) / (i + 2))
        ulist.append(ulist[-1] * (u + num) / (i + 3))
        num += 1
    y = yvals[mid] + u * ftable[2, mid]
    string = 'y(%g) = %g + %g * %g + ' %(x, ftable[1, mid], u, ftable[2, mid])

    for j in range(2, n - 1, 2):
        string += '%g * %g + %g * %g + ' %(ulist[j], ftable[j + 1, mid - int((j + 1) / 2)], ulist[j + 1], ftable[j + 2, mid - int((j + 1) / 2)])
        y += ulist[j] * ftable[j + 1, mid - int((j + 1) / 2)] + ulist[j + 1] * ftable[j + 2, mid - int((j + 1) / 2)]
    if n % 2 == 1:
        y += ulist[-2] * ftable[-1, 0]
        string += '%g * %g + ' %(ulist[-2] , ftable[-1, 0])
    print(string[:-2], '= %g' %(y))
    return y

