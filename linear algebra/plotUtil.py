import matplotlib.pyplot as plt
import numpy as np
from math import *

        
def getList(func, init, termi, delta):
    """
    Retunrs: a list contains values mapped by func from init to termi with increament
    delta.
    Parameters:
    func: single parameter function which returns one real number
    init: init value
    termi: terminate value
    delta: increment value
    """
    x = []
    n = init
    if(delta > 0):
        while(n < termi):
            x.append(func(n))
            n += delta
    elif(delta < 0):
        while(n > termi):
            x.append(func(n))
            n += delta
    return x
    
 