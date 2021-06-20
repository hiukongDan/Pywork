# calculation for linear algebra textboox, 6.1
#!/bin/python3

import numpy as np
from numpy import linalg
import random
import sympy as sp

def randVec(n):
    """
    @param n: dimension of vector space the generated vector in
    @return: numpy array of n-dimension vector ranging from [-1, 1)
    """
    return np.array([random.random() * 2 - 1 for x in range(n)])
    
def randIntVec(n):
    """
    @param n: dimension of vector space the generated vector in
    @return: numpy array of n-dimension vector ranging from [-9, 9)
    """
    return np.array([random.randint(-9, 9) for x in range(n)])
    
def vecCos(a, b):
    """
    @param
        a, b: two vectors this function calculates cosine from
            using dot(a, b) / (||a|| * ||b||)
    @return: the cosine calculated by above algorithm
    """
    return np.dot(a, b) / np.linalg.norm(a) / np.linalg.norm(b)
    
def print_delimeter():
    print("-" * 20)
    
def problem32():
    A = np.array([[.5,.5,.5,.5],[.5,.5,-.5,-.5],[.5,-.5,.5,-.5],[.5,-.5,-.5,.5]])
    vecs = [np.array(x) for x in [[.5,.5,.5,.5],[.5,.5,-.5,-.5],[.5,-.5,.5,-.5],[.5,-.5,-.5,.5]]]
    
    for i in range(len(vecs)-1):
        for j in range(i+1, len(vecs)):
            print("%d x %d" % (i, j))
            print(np.dot(vecs[i], vecs[j]))
            
    print("-" * 20)
    
    u,v = randVec(4), randVec(4)
    
    print("norm u")
    print(np.linalg.norm(u))
    
    print("norm Au")
    print(np.linalg.norm(np.matmul(A, u)))
    
    print("norm v")
    print(np.linalg.norm(v))
    
    print("norm Av")
    print(np.linalg.norm(np.matmul(A, v)))
    
    print("-" * 20)
    print("u")
    print(u)
    
    print("Au")
    print(np.matmul(A, u))
    
    print("v")
    print(v)
    
    print("Av")
    print(np.matmul(A, v))
    
    
    print("-" * 20)
    
    print("cosine between v and u: %f" % (vecCos(u, v)))
    print("cosine between Av and Au: %f" % (vecCos(np.matmul(A, u), np.matmul(A, v))))
    
    print("-" * 20)
    print(sp.Matrix.rref(sp.Matrix(A)))

def problem33():
    x, y, v = randIntVec(4), randIntVec(4), randIntVec(4)
    print("x \n", x)
    print("y \n", y)
    print("v \n", v)
    
    print_delimeter();
    
    print("(dot(x, v) / dot(v, v)) v\n",np.dot(x, v) / np.dot(v, v) * v)
    print("(dot(y, v) / dot(v, v)) v\n",np.dot(y, v) / np.dot(v, v) * v)
    print("(dot(x+y, v) / dot(v, v)) v\n",np.dot(x+y, v) / np.dot(v, v) * v)
    print("(dot(10x, v) / dot(v, v)) v\n",np.dot(10*x, v) / np.dot(v, v) * v)


def problem34():
    A = sp.Matrix([[-6,3,-27,-33,13],[6,-5,25,28,14],[8,-6,34,38,18],
        [12,-10,50,41,23],[14,-21,49,29,33]])
    print("reduced echelon form of A\n", sp.Matrix.rref(A))
    
    N = sp.Matrix([-5,-1,1,0,0])
    R = sp.Matrix([[1,0,5,0,0],[0,1,1,0,0],[0,0,0,1,0],[0,0,0,0,1]])
    
    print("NR \n", R * N)

if __name__ == "__main__":
    problem34()