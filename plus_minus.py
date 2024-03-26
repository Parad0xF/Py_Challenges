#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    nr_positive = 0 
    nr_negative = 0
    nr_zero = 0
 
    for i in arr:
        if i > 0:
            nr_positive += 1 
        elif i < 0:
            nr_negative += 1
        elif i == 0:
            nr_zero +=1
        
    # Write your code here
    
    print(format(float(nr_positive/len(arr)), ".6f"))
    print(format(float(nr_negative/len(arr)), ".6f"))
    print(format(float(nr_zero/len(arr)), ".6f"))

if __name__ == '__main__':


    arr = [1,1,0,-1,-1]

    plusMinus(arr)