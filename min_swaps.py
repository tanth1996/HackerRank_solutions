#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    unsortedEle = {}
    sorted_flag = False

    while not(sorted_flag):
        for idx, ele in enumerate(arr):
            correctVal = idx + 1
            correctIdx = ele - 1
            
            if ele != correctVal:
                arr[idx] = arr[correctIdx]
                arr[correctIdx] = ele
                swaps += 1
       
        if arr == sorted(arr):
            sorted_flag = True
        
    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
