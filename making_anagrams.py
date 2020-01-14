#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    del_N = 0
    a_lut = {}
    for char in a:
        if char not in a_lut:
            a_lut[char] = 1
        else:
            a_lut[char] += 1
    
    for char in b:
        if char not in a_lut or a_lut[char] == 0:
            del_N += 1
        else:
            a_lut[char] -= 1

    del_N += sum(a_lut.values())

    return del_N

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
