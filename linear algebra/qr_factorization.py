"""
@file           qr_factorization.py
@description    QR facorization using Gram-Schmidt process
@author         Hiukong Dan
@version        1.0
@copyright      (c) Hiukong Dan 2021
@contact        ifsoboy9148@hotmail.com
"""

#!/bin/python
import numpy as np
from numpy import linalg
from gram_schmidt import *
from sympy import Matrix

def qr_factorization(A):
    """
    @description:
        QR Factorize a matrix A using gram schmidt process
    @param A:
        Matrix to be factored
    @return (Q, R):
        Q, R tuple of the result
    """
    # linear independence check
    assert np.linalg.matrix_rank(A) == A.shape[1], "The columns are not linear independent"
    
    Q = orthonormalize(gram_schmidt(A))
    R = np.matmul(Q.T, A)
    return (Q, R)

if __name__ == "__main__":
    """
    A = np.array([[-10,13,7,-11],[2,1,-5,3],[-6,3,13,-3],[16,-16,-2,5],[2,1,-5,-7]])
    print(A)
    print(Matrix.rref(Matrix(A)))
    ret = qr_factorization(A)
    print(ret)
    print(np.matmul(ret[0], ret[1]))
    """