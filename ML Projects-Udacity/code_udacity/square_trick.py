#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      extra
#
# Created:     15/02/2022
# Copyright:   (c) extra 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def square_trick(w_1: float,
                 w_2: float,
                 point: tuple,
                 alpha: float = 0.01):
    p, q = point
    q_prime = w_1 * p + w_2
	# NO NEED to verify if q < q'
    w1 = w_1 + p * (q - q_prime) * alpha
    w2 = w_2 + (q - q_prime) * alpha
    return w1, w2

square_trick(w_1 = -0.6, w_2 = 4, point = (-5, 3), alpha = 0.01)
