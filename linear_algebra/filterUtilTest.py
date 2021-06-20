import numpy as np
import matplotlib.pyplot as plt
from math import *

def movingAverage(data):
    ret = [(data[i] + data[i+1] + data[i+2])/3 for i in range(len(data)-2)]
    return np.array(ret)
    
def filter(generator, count=100):
    return np.array([.35*(generator(x) + .5*generator(x+1) + .35*generator(x+2)) for x in range(count)])

if __name__ == "__main__":
    #data = np.array([9,5,7,3,2,4,6,5,7,6,8,10,9,5,7])
    #plt.plot([x for x in range(len(data))], data)
    #avg = movingAverage(data)
    #plt.plot([x for x in range(len(avg))], avg)
    #print(avg)
    
    gen = lambda t: 2*cos(pi*t/4) + cos(3*pi*t/4)
    filtered = filter(gen)
    
    #plt.plot([x for x in range(len(filtered))], [gen(x) for x in range(len(filtered))])
    plt.plot([x for x in range(len(filtered))], filtered)
    
    print(filtered)
    
    
    plt.show()