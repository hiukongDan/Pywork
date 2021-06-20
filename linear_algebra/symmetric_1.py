"""
@file:          symmetric_1.py
@description:   answers to problems in exercises 7.1
                (Linear Algebra and its applications, David C. Lay 3ed)
@author:        Hiu-kong Dan
@date:          June 12, 2021
"""

from sympy import *
import numpy as np
from numpy import linalg

def prob24():
    A = Matrix([[1/sqrt(2), 1/(3*sqrt(2)), -2/3],
                [1/sqrt(2), -1/(3*sqrt(2)), 2/3],
                [0,4/(3*sqrt(2)), 1/3]])
    p = diag(1,1,10)
    print(A * p * A.inv())
    
def normalize(vector):
    x = 0
    for i in vector:
        x += i*i
    sqrtx = sqrt(x)
    return [x/sqrtx for x in vector]

def _dot(x, y):
    res = 0
    for i in len(x):
        res += x[i] * y[i]
    return res
    
def _rref(M):
    """
    @param M: matrix
    """
    # scale each line with first non empty entry
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if(M[i,j] != 0):
                scale = M[i,j]
                for k in range(j, M.shape[1]):
                    M[i,k] /= scale
                break
    print(M)
    
def orthonormal_basis(vector_list):
    u = []
    u.append(Matrix(normalize(vector_list[0])))
    for i in range(1, len(vector_list)):
        vec = Matrix(vector_list[i])
        res = Matrix.zeros(vec.shape[0], 1)
        for uv in u:
            res += uv.dot(vec)/uv.dot(uv) * uv
        res = vec - res
        u.append(Matrix(normalize(res)))
    return u
    
def test_orthogonal(vectors, tolerence = 0.001):
    for i in range(len(vectors)-1):
        for j in range(i+1, len(vectors)):
           if vectors[i].dot(vectors[j]) > tolerence:
                print("orthogonal test fail: \n\t\tvec1:", vectors[i], "\n\t\tvec2:", vectors[j],
                        "\n\t\tdot product: ", vectors[i].dot(vectors[j]))
                return False
    return True
    
def common_calculation(A, title):
    print("problem ", title)
    print("vecs from sympy: ")
    print(A.eigenvects())
    for eigval in A.eigenvals():
        res = Matrix.rref(A - eigval * eye(A.shape[0]))
        print(eigval)
        print(res)
        
    print("-"*20)
    
def prob37():
    A = Matrix([[5.,2,9,-6],
                [2,5,-6,9],
                [9,-6,5,2],
                [-6,9,2,5]])
    common_calculation(A, "37")

def prob38():
    A = Matrix([[.38,-.18,-.06,-.04],
                [-.18,.59,-.04,.12],
                [-.06,-.04,.47,-.12],
                [-.04,.12,-.12,.41]])
    common_calculation(A, "38")
    
    
def prob39():
    A = Matrix([[.31,.58,.08,.44],
                [.58,-.56,.44,-.58],
                [.08,.44,.19,-.08],
                [.44,-.58,-.08,.31]])
    common_calculation(A, "39")

def prob40():
    A = Matrix([[10.,2,2,-6,9],
                [2,10,2,-6,9],
                [2,2,10,-6,9],
                [-6,-6,-6,26,9],
                [9,9,9,9,-19]])
    common_calculation(A, "40")

if __name__ == "__main__":
    prob37()
    prob38()
    prob39()
    prob40()