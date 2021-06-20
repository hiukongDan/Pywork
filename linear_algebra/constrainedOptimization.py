"""
@file:          constrainedOptimization.py
@description:   answers to problems in exercises 7.3
                (Linear Algebra and its applications, David C. Lay 3ed)
@author:        Hiu-kong Dan
@date:          June 20, 2021
"""

import numpy as np
from numpy import linalg
from sympy import Matrix

def common(A):
    print(Matrix.eigenvects(Matrix(A)))
    print(Matrix.eigenvals(Matrix(A)))
    vecs = np.linalg.eig(A)
    print("unit eigenvectors:")
    for vec in vecs[1]:
        print(vec / np.linalg.norm(vec))
    print("eigenvalues: ", vecs[0])
    print("-"*20)
    
def problem14():
    A = np.array([[0, .5, 1.5, 15],
                  [.5, 0, 15, 1.5],
                  [1.5, 15, 0, .5],
                  [15, 1.5, .5, 0]])
    common(A)

def problem15():
    A = np.array([[0, 1.5, 2.5, 3.5],
                  [1.5, 0, 3.5, 2.5],
                  [2.5, 3.5, 0, 1.5],
                  [3.5, 2.5, 1.5, 0]])
    common(A)
   
def problem16():
    A = np.array([[4, -3, -5, -5],
                  [-3., 0, -3, -3],
                  [-5, -3, 0, -1],
                  [-5, -3, -1, 0]])
    common(A)
    
def problem17():
    A = np.array([[-6, -2, -2, -2],
                  [ -2, -10, 0, 0],
                  [ -2, 0, -13, 3],
                  [ -2, 0, 3, -13]])
    common(A)


if __name__ == '__main__':
    problem14()
    problem15()
    problem16()
    problem17()