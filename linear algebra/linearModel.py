"""
@file:          linearModel.py
@description:   answers to problems in exercises 6.6 
                (Linear Algebra and its applications, David C. Lay 3ed)
@author:        Hiu-kong Dan
@date:          June 3, 2021
"""

from sympy import Matrix
import numpy as np
from numpy import linalg
from matplotlib import pyplot as plt
import math

def delimeter():
    print("-"*20)
    
def printAnswerMsg(title, res):
    """
    @description:
        print answers
    @param:
        title: string
            the question title: string
        res: tuple
            tuple returned by getLeastSquare
    @return:
        none
    """
    print(title, ": ")
    print("b: ", res[0])
    print("e: ", res[1])
    delimeter()
    
def getLeastSquare(X, y):
    """
    @description:
        calculate the least square solution of Xb = y
    @param:
        X: design matrix
        y: observation vector
    @return:
        (b, e)
        b: parameter vector
        e: error vector
    """
    XTX = np.matmul(X.T, X)
    XTX_INV = np.linalg.inv(XTX)
    XTY = np.matmul(X.T, y)
    b = np.matmul(XTX_INV, XTY)
    XB = np.matmul(X, b)
    e = y - XB
    return (b, e)

def problem7():
    X = np.array([[1,1],
                  [2,4],
                  [3,9],
                  [4,16],
                  [5,25]])
    y = np.array([1.8,2.7,3.4,3.8,3.9])
    res = getLeastSquare(X, y)
    printAnswerMsg("problem7", res)

def problem8():
    X = np.array([[4, 4**2, 4**3],
                  [6, 6**2, 6**3],
                  [8, 8**2, 8**3],
                  [10, 10**2, 10**3],
                  [12, 12**2, 12**3],
                  [14, 14**2, 14**3],
                  [16, 16**2, 16**3],
                  [18, 18**2, 18**3]])
    y = np.array([1.58,2.08,2.5,2.8,3.1,3.4,3.8,4.32])
    res = getLeastSquare(X, y)
    b = res[0]
    
    func = lambda x: b[0]*x + b[1]*x**2 + b[2]*x**3;
    plt.plot([x for x in range(100)], [func(x) for x in range(100)])
    plt.show()
    
    
def problem10():
    X = np.array([[math.e**-.2, math.e**-.7],
                  [math.e**-.22, math.e**(-.07*11)],
                  [math.e**(-.02*12), math.e**(-.07*12)],
                  [math.e**(-.02*14), math.e**(-.07*14)],
                  [math.e**(-.02*15), math.e**(-.07*15)]])
    y = np.array([21.34, 20.68,20.05,18.87,18.30])
    
    res = getLeastSquare(X, y)
    
    printAnswerMsg("problem10", res)
    
def problem11():
    X = np.array([[1, 3.00*math.cos(.88)],
                  [1, 2.30*math.cos(1.10)],
                  [1, 1.65*math.cos(1.42)],
                  [1, 1.25*math.cos(1.77)],
                  [1, 1.01*math.cos(2.14)]])
    y = np.array([3.00, 2.30, 1.65, 1.25, 1.01])
    
    res = getLeastSquare(X, y)
    
    printAnswerMsg("problem11", res)
    
def problem12():
    X = np.array([[1, 1, 1, 1, 1],
                  [3.78, 4.11, 4.41, 4.73, 4.88]]).T
    y = np.array([91.0, 98, 103, 110, 112])
    
    res = getLeastSquare(X, y)
    
    func = lambda w: res[0][0] + res[0][1] * math.log(w)
    
    print("problem 12:", func(100))
    delimeter()
    
def problem13():
    time = [x for x in range(13)]
    data = [0, 8.8, 29.9, 62.0, 104.7, 159.1, 222.0, 294.5, 380.4, 471.1, 571.7, 686.8, 809.2]
    X = np.array([[1 for x in range(len(time))],
                  [x for x in time],
                  [x*x for x in time],
                  [x*x*x for x in time]]).T
                  
    y = np.array(data)
    
    res = getLeastSquare(X, y)
    
    print("b"
    
    b = res[0]
    func = lambda t: b[1] + 2 * b[2] * t + 3 * b[3] * t * t
    
    print("velocity of the plane at time 4.5 is ", func(4.5))

if __name__ == "__main__":
    problem13()