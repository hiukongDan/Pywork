"""
@file orthogonal_3.py
@description solutions to linear algebra textbook 6.3
@author Hiukong Dan
@version 1.0 May 28, 2021
"""
#!/bin/python
from sympy import Matrix
import numpy as np
import random

def problem25():
    """
    Find neareast point in Col A to vector p in R^n
    """
    print("broblem 25")
    
    A = np.array([[-6,-3,6,1],[-1,2,1,-6],[3,6,3,-2],[6,-3,6,-1],[2,-1,2,3],[-3,6,3,2],[-2,-1,2,-3],[1,2,1,6]])
    p = np.array([1,1,1,1,1,1,1,1])
    
    pp = np.array([0,0,0,0,0,0,0,0])
    for x in A.T:
        pp = pp + np.dot(x, p) / np.dot(x, x) * x
    
    print(pp)
    
    print("-"*20)
    
def problem26():
    """
    Find distance from p to A
    """
    print("broblem 26")
    
    A = np.array([[-6,-3,6,1],[-1,2,1,-6],[3,6,3,-2],[6,-3,6,-1],[2,-1,2,3],[-3,6,3,2],[-2,-1,2,-3],[1,2,1,6]])
    p = np.array([1,1,1,1,-1,-1,-1,-1])
    
    pp = np.array([0,0,0,0,0,0,0,0])
    for x in A.T:
        pp =pp + np.dot(x, p) / np.dot(x, x) * x
    
    dis = np.linalg.norm(p - pp)
    print(dis)
    
    print("-"*20)
    
    
if __name__ == "__main__":
    problem25()
    problem26()