"""
@file orthogonal.py
@description solutions to linear algebra textbook 6.2
@author Hiukong Dan
@version 1.0 May 26, 2021
"""
#!/bin/python
from sympy import Matrix
import numpy as np
import random

def problem35():
    A = np.array([[-6,-3,6,1],[-1,2,1,-6],[3,6,3,-2],[6,-3,6,-1],[2,-1,2,3],[-3,6,3,2],[-2,-1,2,-3],[1,2,1,6]])
    for x in range(0, A.shape[1]-1):
        for y in range(x+1, A.shape[1]):
            print(Matrix(np.dot(A.T[x], A.T[y])))

def problem36():
    A = np.array([[-6,-3,6,1],[-1,2,1,-6],[3,6,3,-2],[6,-3,6,-1],[2,-1,2,3],[-3,6,3,2],[-2,-1,2,-3],[1,2,1,6]])
    U = np.array([A.T[x] / np.linalg.norm(A.T[x]) for x in range(A.shape[1])]).T
    # (a)
    # print("U^T * U", np.matmul(U.T, U))
    # print("U * U^T", np.matmul(U, U.T))
    
    # (b)
    y = np.array([random.random() * 18 - 9 for x in range(8)])
    print("y", y)
    
    p = np.matmul(U, np.matmul(U.T, y))
    print("p", p)
    
    z = y - p
    print("z", z)
    
    print("dot(z, p)", np.dot(z, p))
    
    # (c)
    for x in range(U.shape[1]):
        print(np.dot(U.T[x], z))


if __name__ == "__main__":
    problem36();