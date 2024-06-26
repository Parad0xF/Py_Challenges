#!/bin/python3
"""
Two friends like to pool their money and go to the ice cream parlor. They always choose two distinct flavors and they spend all of their money.
Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.
Example.  m = 6, cost = [1,3,4,5,6]
The two flavors that cost  and  meet the criteria. Using 1-based indexing, they are at indices 1 and 4.
Function Description
Complete the icecreamParlor function in the editor below.
icecreamParlor has the following parameter(s):
int m: the amount of money they have to spend
int cost[n]: the cost of each flavor of ice cream
Returns
int[2]: the indices of the prices of the two flavors they buy, sorted ascending
"""
import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.



# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == m:
                return[i+1, j+1]
    
    # Return an empty list if no solution is found (though per the problem's constraints, there should always be a solution)
    return []

if __name__ == '__main__':

    money = 5

    flavour = [1,2,3,4,5]

    result = icecreamParlor(money, flavour)

    print(result)