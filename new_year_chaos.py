#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    q_len = len(q)
    swaps = [0 for i in range(q_len)]
    swaps_N = 0

    sorted_flag = False
    while not(sorted_flag):
        sorted_flag = True
        for idx, ele in enumerate(q, 1):
            if idx == q_len:
                break
            if ele > q[idx]:
                sorted_flag = False
                swaps[q[idx-1]-1] += 1
                if swaps[q[idx-1]-1] > 2:
                    print('Too chaotic')
                    return
                
                q[idx-1] = q[idx]
                q[idx] = ele
                swaps_N += 1

    print(swaps_N)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
