#!/bin/python3

"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.
Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
"""

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    
    ret = ''
    int_nr_convert = int(s[:2])
    int(int_nr_convert)

    if s[-2:] == "PM" and int(s[:2]) != 12:
        int_nr_convert +=12
        int_nr_convert = str(int_nr_convert)
        result = "".join(map(str, s[2:-2]))
        ret = int_nr_convert + result
        return ret
        
    elif s[-2:] == "AM" and int(s[:2]) == 12:
        result = "".join(map(str, s[2:-2]))
        ret = "00"+result
        return ret       
    else:
        ret = "".join(map(str, s[:-2]))
        return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
