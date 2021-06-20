from sympy import Matrix
import numpy as np
import random

def GenerateMatrixWithRank(row, column, rank, lowerBound=-9, upperBound=9):
    """
    Generate Matrix with Rank=rank
    Res = A(row x rank) X B(rank x column)
    lowerBound: lower bound for generated entry
    upperBound: upper bound for generated entry
    """
    A = np.array([random.randint(lowerBound, upperBound) for x in range(row*rank)]).reshape(row, rank)
    B = np.array([random.randint(lowerBound, upperBound) for x in range(column*rank)]).reshape(rank, column)
    
    return np.matmul(A, B)

if __name__ == "__main__":
    rank = 1
    row = 5
    column = 7
    M = GenerateMatrixWithRank(row, column, rank, lowerBound=-3, upperBound=3)
    print(M)
    RREF, cols = Matrix.rref(Matrix(M))
    C = np.array(M)[:,[x for x in cols]]
    R = np.array(RREF)[[x for x in cols],:]
    
    print("C:")
    print(C)
    print("R:")
    print(R)
    print("C x R:")
    print(np.matmul(C, R))