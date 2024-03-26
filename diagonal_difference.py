#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    
    diag_right = [] 
    diag_left = []
 
    [diag_left.append(arr[c][c]) for c in range(len(arr))]
    [diag_right.append(arr[c][-c -1]) for c in range(len(arr))]
    
    return abs(sum(diag_left) - sum(diag_right))

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)