"""
@file:          least_square.py
@description:   answer to problems in exercises 6.5
@author:        Hiu-kong Dan
@date:          June 1, 2021
"""

from sympy import Matrix

def problem26():
    A = Matrix([[0, .7, 1],
                [-.7,0,.7],
                [-1,-.7,0],
                [-.7,-1,-.7],
                [0,-.7,-1],
                [.7,0,-.7],
                [1,.7,0],
                [.7,1,.7],
                [0,-.7,1],
                [.7,0,-.7],
                [-1,.7,0],
                [.7,-1,.7],
                [0,.7,-1],
                [-.7,0,.7],
                [1,-.7,0],
                [-.7,1,-.7]])
    b = Matrix([.7,
                0,
                -.7,
                -1,
                -.7,
                0,
                .7,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0])
    
    assert A.shape == (16,3)
    assert b.shape == (16,1)
    
    M = (A.T * A).col_insert(4, A.T * b)
    
    assert M.shape == (3, 4)
    
    x = Matrix.rref(M)[0].col(3)
    
    print("Using row reduction:")
    print(x)
    print("-"*20)
    
    # using another mathod
    print("Using inverse matrix:")
    x = (A.T * A).inv() * A.T * b
    print(x)
    

if __name__ == "__main__":
    problem26()