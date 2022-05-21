#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      extra
#
# Created:     15/02/2022
# Copyright:   (c) extra 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#absolute trick

def absolute_trick(w_1: float,
		   w_2: float,
		   point: tuple,
		   alpha: float = 0.01):
    p, q = point
    # Change the signs if the line is above the point
    q_prime = w_1 * p + w_2 # compute q_p (or y)
    alpha = - alpha if q_prime > q else alpha
    w1 = w_1 + p * alpha
    w2 = w_2 + alpha
    return w1, w2


# test for y = -0.6 + 4
absolute_trick(w_1 = -0.6, w_2 = 4,
			   point = (-5, 3), alpha = 0.1)
