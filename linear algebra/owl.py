import numpy as np
from matplotlib import pyplot as plt
from sympy import Matrix


if __name__ == "__main__":
    M = Matrix([[0,1.6],[.3,.8]])
    x = Matrix([15,10])
    
    years = np.arange(1, 100)
    num_juveniles, num_adults, num_total, ratio_juv2adult = [], [], [], []
    
    for year in years:
        x = M * x
        num_juveniles.append(x[0])
        num_adults.append(x[1])
        num_total.append(x[0] + x[1])
        ratio_juv2adult.append(x[0]/x[1])
        
    #plt.plot(years, num_juveniles)
    #plt.plot(years, num_adults)
    #plt.plot(years, num_total)
    plt.plot(years, ratio_juv2adult)
    
    plt.show()