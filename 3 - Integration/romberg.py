import numpy as np
import math

def f(x):
    return 1 / x

def drawtable(table):
    n = len(table[0,:])
    for i in range(n):   
        for j in range(i + 1):  
            print('%.9g'% (table[i , j]),  end ='\t')  
        print("")

def romberg(f, a, b, n):
    r = np.zeros([n + 1, n + 1])
    h = b - a
    r[0,0] = 0.5 * h * ( f( a ) + f( b ) )
    powerOf2 = 1
    
    for i in range(1, n + 1):
        h /= 2
        sumt = 0.
        powerOf2 = 2 * powerOf2
        for k in range( 1, powerOf2, 2 ):
            sumt += f( a + k * h )
        r[i,0] = 0.5 * r[i-1,0] + sumt * h
        
        powerOf4 = 1
        for j in range(1, i + 1):
            powerOf4 = 4 * powerOf4
            r[i,j] = r[i,j-1] + ( r[i,j-1] - r[i-1,j-1] ) / ( powerOf4 - 1 )
            
    drawtable(r)
    return(r[-1, -1])

print(romberg(f, 1, 2, 4) - math.log(2)) 
