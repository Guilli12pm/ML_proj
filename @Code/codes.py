import numpy as np
import math

def check_closer(dict,numb):
    which = None
    dist = math.inf
    for key,value in dict.items():
        diff = abs(value - numb)
        if diff < dist:
            dist = diff
            which = key
    
    return which
