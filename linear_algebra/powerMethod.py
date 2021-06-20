# Power method
# Estimate significant eigenvalue using power method
from sympy import Matrix
import numpy as np

class PowerMethodEntity:
    def __init__(self, A):
        """
        self.A is the matrix we estimate eigenvalue from
            type: sympy.Matrix
        """
        self.A = A
        
    def estimate(self, x0, n):
        """
        x0 is the initial vector
        n is the iteration times
        """
        val = []
        vec = []
        for i in range(n):
            x0 = A * x0
            tmp = max([abs(x) for x in x0])
            val.append(tmp)
            x0 = x0/tmp
            vec.append(x0)
        
        return (val, vec)
        
class InversePowerMethodEntity:
    def __init__(self, A):
        """
        self.A is the matrix we estimate eigenvalue from
            type: sympy.Matrix
        """
        self.A = A
        
    def estimate(self, a, x0, n):
        """
        a is the approximate eigenvalue
        x0 is the initial vector
        n is the iteration times
        """
        B = (self.A - a * Matrix.eye(self.A.shape[0])) ** -1
        val = []
        vec = []
        for i in range(n):
            x0 = B * x0
            tmp = max([abs(x) for x in x0])
            val.append(a + 1/tmp)
            x0 = x0/tmp
            vec.append(x0)
        
        return (val, vec)
    
def rayleigh_quotient(M, x):
    """"
    compute rayleigh quotient of vector x from matrix M
    """
    return (x.T * M * x)[0] / (x.T * x)[0]
    
    
def calculate_multiple(M, x, n):
    res = []
    for i in range(n):
        x = M * x
        res.append(x)
        
    return res

if __name__ == "__main__":
    A = Matrix([[.8,0],[0,.2]])
    #p = PowerMethodEntity(A)
    #res = p.estimate(Matrix([.5,.5]), 10)
    #vecs = res[1]
    #rays = [rayleigh_quotient(A, vec) for vec in vecs]
    #print(res)
    #print(rays)
    
    res = calculate_multiple(A, Matrix([.5,.5]), 10)
    print(res)