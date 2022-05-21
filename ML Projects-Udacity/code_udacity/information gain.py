#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      extra
#
# Created:     16/02/2022
# Copyright:   (c) extra 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np
import math
#first is nb of + labels and tot is the total number of labels
def two_group_ent(first,tot):
    return -(first/tot*np.log2(first/tot) +
             (tot-first)/tot*np.log2((tot-first)/tot))

tot_ent = two_group_ent(29,64)
g17_ent = 26/64 * two_group_ent(21,26) + 38/64 * two_group_ent(8,38)

answer = tot_ent - g17_ent
print (answer)