#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr = sorted(arr)
    diff_min = arr[1] - arr[0]
    for idx in range(1, len(arr) - 1):
        diff = arr[idx+1] - arr[idx]
        if diff < diff_min:
            diff_min = diff
        if diff_min == 0:
            return diff_min
    return diff_min      


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
