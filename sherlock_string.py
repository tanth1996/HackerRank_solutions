#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    freq_lut = [0 for i in range(26)]

    for char in s:
        freq_lut[ord(char) - ord('a')] += 1
    
    print(freq_lut)

    freq_chk = []
    freq_freq_lut = {}
    idx = 0
    freq_allowed = None
    for freq in freq_lut:
        if freq == 0:
            continue

        if freq not in freq_freq_lut:
            if len(freq_freq_lut) == 2:
                return 'NO'
            else:
                freq_freq_lut[freq] = 1
        else:
            freq_freq_lut[freq] += 1

    print(freq_freq_lut)

    if len(freq_freq_lut) > 1:
        for freq, freq_freq in freq_freq_lut.items():
            if freq == 1 and freq_freq == 1:
                return 'YES'
        if max(freq_freq_lut.keys()) - min(freq_freq_lut.keys()) > 1:
            return 'NO'
        elif freq_freq_lut[max(freq_freq_lut.keys())] > 1:
            return 'NO'

    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
