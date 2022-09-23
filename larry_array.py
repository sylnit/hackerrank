#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#
# challenge URL = https://www.hackerrank.com/challenges/larrys-array/problem


def larrysArray(A):
    # Write your code here
    sum = 0

    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] > A[j]:
                sum += 1

    if sum % 2 == 0:
        return "YES"
    else:
        return "NO"
