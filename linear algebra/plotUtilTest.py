#plotUtil test
from plotUtil import getList
from math import *
import matplotlib.pyplot as plt
from scipy import integrate as integrate

if __name__ == '__main__':
    init = -10
    terminate = 10
    delta = 0.01
    
    f = lambda t: integrate.quad(lambda t: cos(pi*t*t/2), 0, t)
    g = lambda t: integrate.quad(lambda t: sin(pi*t*t/2), 0, t)
    
    x = getList(lambda t: f(t)[0], init, terminate, delta)
    y = getList(lambda t: g(t)[0], init, terminate, delta)
    plt.plot(x, y)

    plt.show()