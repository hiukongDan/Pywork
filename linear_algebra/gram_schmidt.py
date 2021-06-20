"""
@file           gram_schmidt.py
@description    Orthogonalize set using Gram-Schmidt Process
@author         Hiukong Dan
@version        1.0
@copyright      (c) Hiukong Dan 2021
@contact        ifsoboy9148@hotmail.com
"""

#!/bin/python
import numpy as np
from numpy import linalg
import random

def gram_schmidt(M):
    """
    @param M:
        A mxn matrix whose columns to be orthogonalized
    @return ret
        Matrix whose columns being orthogonalized
    """
    columns = M.T
    res = []
    res.append(columns[0])
    
    for x in range(1, columns.shape[0]):
        tmp = np.array([0 for x in range(M.shape[0])])
        for vec in res:
            y = (np.dot(vec, columns[x]) / np.dot(vec, vec)) * vec
            tmp = tmp + y
            
        res.append(columns[x] - tmp)

    return np.array(res).T
    
def orthonormalize(M):
    """
    @param M: 
        The matrix whose columns to be orthonormalized
    @return ret: 
        The outcome matrix
    """
    ret = M.T
    for x in range(ret.shape[0]):
        ret[x] = ret[x] / np.linalg.norm(ret[x])
    
    return ret.T

if __name__ == "__main__":
    """
    ret = gram_schmidt(np.arange(16).reshape(4,4))
    northonormal = orthonormalize(ret)
    """