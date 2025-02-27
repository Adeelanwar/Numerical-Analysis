from guassforward import *
from guassbackward import *

##xvals = [20,25,30,35,40]
##yvals = [49225,48316,47236,45926,44306]
##x = 28

##xvals = [1931, 1941, 1951, 1961, 1971, 1981]
##yvals = [12, 15, 20, 27, 39, 52]
##x = 1966

xvals = [10, 11, 12, 13, 14]
yvals = [0.23967, 0.28060, 0.31788, 0.35209, 0.38368]
x = 12.2
##
##
##xvals = [0, 0.5, 1.0, 1.5, 2.0 ]
##yvals = [ 0, 0.191, 0.341, 0.433, 0.477];
##x = 1.22

##xvals = [25, 26, 27, 28, 29, 30]
##yvals = [4.0, 3.846, 3.704, 3.571, 3.448, 3.333]
##x = 27.4

##xvals = [20, 24, 28, 32]
##yvals = [2854, 3162, 3544, 3992]
##x = 25
##
##xvals = [2.5, 3, 3.5, 4.0, 4.5, 5.0]
##yvals = [24.145, 22.043, 20.225,18.644, 17.262, 16.047]
##x = 3.75

def Stirling(xvals, yvals, x):
    drawtable(table(xvals, yvals))
    print('guass forward:  ')
    gf = guassfor(xvals, yvals, x)
    print('guass backward: ')
    gb = guassback(xvals, yvals, x)
    y = (gf + gb) / 2
    print('Stirling: \ny = (%f + %f) / 2 = %.6g' % (gf, gb, y))
    return y
print(Stirling(xvals, yvals, x))
