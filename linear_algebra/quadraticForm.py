"""
@file:          quadraticForm.py
@description:   answers to problems in exercises 7.2
                (Linear Algebra and its applications, David C. Lay 3ed)
@author:        Hiu-kong Dan
@date:          June 20, 2021
"""

import numpy as np
from numpy import linalg
from sympy import Matrix

def common(A):
    vecs = np.linalg.eig(A)
    for vec in vecs[1]:
        print(vec / np.linalg.norm(vec))
    print(vecs[0])
    print("-"*20)

def problem15():
    A = np.array([[-2, 2, 2, 2],
                [ 2, -6, 0, 0],
                [ 2, 0, -9, 3],
                [ 2, 0, 3, -9]])
    common(A)
   
def problem16():
    A = np.array([[ 4, 1.5, 0, -2],
                [ 1.5, 4, 2, 0],
                [ 0, 2, 4, 1.5],
                [ -2, 0, 1.5, 4]])
    common(A)
    
def problem17():
    A = np.array([[ 1, 4.5, 0, -6],
                [ 4.5, 1, 6, 0],
                [ 0, 6, 1, 4.5],
                [ -6, 0, 4.5, 1]])
    common(A)
    
def problem18():
    A = np.array([[ 11, -6, -6, -6],
                [ -6, -1, 0, 0],
                [ -6, 0, 0, -1],
                [ -6, 0, -1, 0]])
    common(A)

if __name__ == '__main__':
    problem15()
    problem16()
    problem17()
    problem18()