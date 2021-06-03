#/bin/python
from sympy import Matrix

def GetCircuitMatrix1(r1, r2, c1, c2):
    return Matrix([[-(1/r1 + 1/r2)/c1, 1/(r2*c1)],[1/(r2*c2), -1/(r2*c2)]])
    
def GetCircuitMatrix3(r1, r2, c, l):
    return Matrix([[-r2/l, -1/l],[1/c,-1/(r1*c)]])
    
def GetCircuitMatrix22(r, c, l):
    return Matrix([[0,1/l],[-1/c,-1/(r*c)]])


if __name__ == "__main__":
    M = GetCircuitMatrix1(1/5,1/3,4,3)
    print(M)