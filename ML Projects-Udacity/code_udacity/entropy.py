#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      extra
#
# Created:     16/02/2022
# Copyright:   (c) extra 2022
# Licence:     <your licence>
#-----------------------------------------------------------------------------
import numpy as np
import math
def get_entropy(probs: np.array):
    entropy = - np.array([p * math.log2(p) for p in probs]).sum()
    return entropy

def get_probabilities(array: np.array):
    values, counts = np.unique(array, return_counts = True)
    n = len(array)
    probs = counts / n
    return probs

# Solution
a = ['R']*4 + ['B']*10
# Compute the probabilities
probs = get_probabilities(a)
# Get the entropy
print (get_entropy(probs))
print (a)