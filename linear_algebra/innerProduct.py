"""
@file:          innerProduct.py
@description:   answers to problems in exercises 6.8
                (Linear Algebra and its applications, David C. Lay 3ed)
@author:        Hiu-kong Dan
@date:          June 9, 2021
"""

from linearModel import delimeter, getLeastSquare
import numpy as np

def problem15():
    time = [x for x in range(13)]
    data = [0, 8.8, 29.9, 62.0, 104.7, 159.1, 222.0, 294.5, 380.4, 471.1, 571.7, 686.8, 809.2]
    X = np.array([[1 for x in range(len(time))],
                  [x for x in time],
                  [x*x for x in time],
                  [x*x*x for x in time]]).T
                  
    y = np.array(data)
    
    W = np.diag([1,1,1,.9,.9,.8,.7,.6,.5,.4,.3,.2,.1])
    
    res = getLeastSquare(np.matmul(W, X), np.matmul(W, y))
    
    b = res[0]
    func = lambda t: b[1] + 2 * b[2] * t + 3 * b[3] * t * t
    
    print("velocity of the plane at time 4.5 is ", func(4.5))
    
def problem16():
    # me using desmos.com
    pass
    
if __name__ == "__main__":
    problem15()