"""
Given five positive integers, find the minimum and maximum values that can be 
calculated by summing exactly four of the five integers. Then print the respective
minimum and maximum values as a single line of two space-separated long integers.

Example

The minimum sum is 1+3+5+7 = 16  and the maximum sum is 3+5+7+9 = 24. The function prints 16, 24
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    lst_check = []
    lst_hold = []
    for i in range(len(arr)):
       data =  arr.pop(-i -1)
       lst_check = arr
       lst_hold.append(sum(lst_check))
       lst_check.append(data)
    print(min(lst_hold), max(lst_hold))
    # Write your code here
if __name__ == '__main__':

    #arr = list(map(int, input().rstrip().split()))

    arr = [396285104,573261094, 759641832, 819230764, 364801279]

"""
    print(sum([396285104,573261094, 759641832, 819230764]))
    print(sum([396285104,573261094, 759641832, 364801279]))
    print(sum([396285104,573261094, 819230764, 364801279]))
    print(sum([396285104, 759641832, 819230764, 364801279]))
    print(sum([573261094, 759641832, 819230764, 364801279]))
"""

#miniMaxSum(arr)


test(arr)