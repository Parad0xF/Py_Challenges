#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    
    
    rounded_grades = [i + (5 - (i % 5)) if ((5 - (i % 5)) < 3) and (i > 35) else i for i in grades]
            
    return rounded_grades
    # Write your code here

if __name__ == '__main__':

    grades = [73, 67, 38, 33]
    
    print(gradingStudents(grades))
