"""
@file               gram_schmidt_test.py
@description        solutions for linear algebra textbook 6.4
@author             Hiukong Dan
@date               May 29, 2021
"""

from gram_schmidt import *
from qr_factorization import *
import numpy as np
from numpy import linalg

def gram_schmidt_modified(A):
    # Check if the matrix is linear independent
    assert np.linalg.matrix_rank(A) == A.shape[1]
    
    len = np.linalg.norm(A.T[0])
    Q = []
    Q.append(A.T[0] / len)
    #print(Q)
    
    for i in range(1, A.shape[1]):
        #print(Q.T)
        p = np.matmul(np.array(Q), A.T[i])
        p = np.matmul(np.array(Q).T, p)
        z = A.T[i] - p
        z = z / np.linalg.norm(z)
        Q.append(z)
    
    return np.array(Q).T

if __name__ == "__main__":
    # problem 24
    print("problem 24")
    A = np.array([[-10,13,7,-11],[2,1,-5,3],[-6,3,13,-3],[16,-16,-2,5],[2,1,-5,-7]])
    print(orthonormalize(gram_schmidt(A)))
    print("-" * 20)

    # problem 25
    print("problem 25")
    ret = qr_factorization(A)
    print("Q", ret[0])
    print("R", ret[1])
    print("-" * 20)
    
    # problem 26
    print("problem 26")
    ret = gram_schmidt_modified(A)
    print(ret)