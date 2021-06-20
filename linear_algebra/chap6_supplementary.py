"""
@file:          chap6_supplementary.py
@description:   answers to problems in exercises chapter 6 supplementary exercises
                (Linear Algebra and its applications, David C. Lay 3ed)
@author:        Hiu-kong Dan
@date:          June 10, 2021
"""

import numpy as np
from numpy import linalg

def calculate_relative_change(A, b, db):
    """
    @description:
        calculate Ax = b, and A*dx = db  (delta x, delta b respectively)
    @params:
        A: nxn matrix
        b: right side of Ax = b
        db: change in b
    @return:
        tuple(x, dx)
    """
    x = np.matmul(np.linalg.inv(A), b)
    dx = np.matmul(np.linalg.inv(A), db)
    return (x, dx)
    
def compare_relative_change(A, b, db):
    """
    @description:
        calculate the relative change in b and relative change in x
        then determine if norm(dx)/norm(x) <= cond(A) * (norm(db)/norm(b))
    @param:
        A: nxn matrix
        b: right side of Ax = b
        db: change in b
    @return:
        none
    """
    x, dx = calculate_relative_change(A, b, db)
    right_side = np.linalg.cond(A) * (np.linalg.norm(db) / np.linalg.norm(b))
    left_side = np.linalg.norm(dx) / np.linalg.norm(x)
    print("left side: ", left_side, "\nright side: ", right_side)
    print("left side <= right side: ", left_side<=right_side)

def problem(title, A, b, db):
    print("problem ", title, ":")
    print("cond: ", np.linalg.cond(A))
    compare_relative_change(A, b, db)
    print("-"*20)

def problem17():
    A = np.array([[4.5,3.1],[1.6,1.1]])
    b = np.array([19.249,6.843])
    db = np.array([.001,-.003])
    problem("17", A, b, db)
    
def problem18():
    A = np.array([[4.5, 3.1],[1.6,1.1]])
    b = np.array([.500,-1.407])
    db = np.array([.001,-.003])
    problem("18", A, b, db)
    
def problem19():
    A = np.array([[7.,-6,-4,1],
                  [-5,1,0,-2],
                  [10,11,7,-3],
                  [19,9,7,1]])
    b = np.array([.100,2.888,-1.404,1.462])
    db = 10**-4 * np.array([.49, -1.28, 5.78,8.04])
    problem("19", A, b, db)
    
def problem20():
    A = np.array([[7.,-6,-4,1],
                  [-5,1,0,-2],
                  [10,11,7,-3],
                  [19,9,7,1]])
    b = np.array([4.230,-11.043,49.991,69.536])
    db = 10**-4 * np.array([.27,7.76,-3.77,3.93])
    problem("20", A, b, db)

if __name__ == "__main__":
    problem17()
    problem18()
    problem19()
    problem20()