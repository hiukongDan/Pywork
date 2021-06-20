#bezier
from plotUtil import getList
from math import *
import matplotlib.pyplot as plt

def plotLine(start, end):
    x = getList(lambda t: t, start[0], end[0], (end[0]-start[0])/100)
    y = getList(lambda t: t, start[1], end[1], (end[1]-start[1])/100)
    m = min(len(x), len(y))
    plt.plot(x[0:m],y[0:m])
    
def plotBezier(P0, P1, P2, P3):
    init = 0
    terminate = 1
    delta = 0.01
    
    fx = lambda t: P0[0]*(1-t)**3 + 3*P1[0]*t*(1-t)**2 + 3*P2[0]*t**2*(1-t) + P3[0]*t**3
    fy = lambda t: P0[1]*(1-t)**3 + 3*P1[1]*t*(1-t)**2 + 3*P2[1]*t**2*(1-t) + P3[1]*t**3
    
    x = getList(fx, init, terminate, delta)
    y = getList(fy, init, terminate, delta)
    plt.plot(x, y)

if __name__ == '__main__':
    init = 0
    terminate = 1
    delta = 0.01
    
    #fx = lambda t: x0*(1-t)**3 + 3*x1*t*(1-t)**2 + 3*x2*t**2*(1-t) + x3*t**3
    #fy = lambda t: y0*(1-t)**3 + 3*y1*t*(1-t)**2 + 3*y2*t**2*(1-t) + y3*t**3
    
    #x = getList(fx, init, terminate, delta)
    #y = getList(fy, init, terminate, delta)
    #plt.plot(x, y)
    
    #plotLine((x0, y0), (x1, y1))
    #plotLine((x1, y1), (x2, y2))
    #plotLine((x2, y2), (x3, y3))
    
    plotBezier((0, 0), (-10, 5), (0, 10), (5,5))
    plotBezier((0, 0), (10, -5), (0, -10), (-5, -5))

    plt.show()