#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(costs, money):
    cost_lut = {}
    for idx, cost in enumerate(costs, 1):
        if cost not in cost_lut:
            cost_lut[cost] = []
        cost_lut[cost].append(idx)

    for idx, cost in enumerate(costs, 1):
        cost_tgt = money - cost
        if cost_tgt in cost_lut:
            for idx_chk in cost_lut[cost_tgt]:
                if idx_chk != idx:
                    print(idx, idx_chk)
                    return


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
