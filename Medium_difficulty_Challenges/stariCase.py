#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    lst = [[' ']*n]*n
    for r in range(n):
        lst[r][-r -1] = "#"
        lst[r] = lst[r]
        for c in range(n):
            print(lst[c][c], end='')
        print()         

    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
