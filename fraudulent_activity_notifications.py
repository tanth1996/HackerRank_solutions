#!/bin/python3

import math
import os
import random
import re
import sys
from time import time
from bisect import bisect_left, insort_left

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    notifications_N = 0
    
    time_start = time()

    for idx in range(d, len(expenditure)):
        val_oldest = expenditure[idx-d]
        val_newest = expenditure[idx-1]
        val_current = expenditure[idx]

        if idx == d:
            expend_trail = expenditure[idx-d:idx]
            expend_trail.sort()
            
        if d % 2 == 0:
            median = (expend_trail[d//2 - 1] + expend_trail[d//2])/2
        else:
            median = expend_trail[(d-1)//2]

        if val_current >= 2*median:
            notifications_N += 1

        del expend_trail[bisect_left(expend_trail, val_oldest)]
        insort_left(expend_trail, val_current)
        
    
    # expend_trail = [0 for _ in range(d)]
    # expend_trail_init = expenditure[0:d-1]
    # expend_trail_counts = [0 for _ in range(201)]
    # for expense in expend_trail_init:
    #     expend_trail_counts[expense] += 1

    # for idx in range(d, len(expenditure)):
    #     val_oldest = expenditure[idx-d]
    #     val_newest = expenditure[idx-1]
    #     val_current = expenditure[idx]
    #     expend_trail_counts[val_newest] += 1

    #     idx_sort = 0
    #     for expense in range(len(expend_trail_counts)):
    #         for count in range(expend_trail_counts[expense]):
    #             expend_trail[idx_sort] = expense
    #             idx_sort += 1
                
    #             if idx_sort >= d//2 + 1:
    #                 break
    #         if idx_sort >= d//2 + 1:
    #             break

    #     if d % 2 == 0:
    #         median = (expend_trail[d//2 - 1] + expend_trail[d//2])/2
    #     else:
    #         median = expend_trail[(d-1)//2]

    #     if val_current >= 2*median:
    #         notifications_N += 1

    #     expend_trail_counts[val_oldest] -= 1
        


    # for idx in range(d, len(expenditure)):
    #     if not expend_trail:
    #         expend_trail = expenditure[idx-d:idx].copy()
    #         expend_trail.sort()
    #     else:
    #         idx_lo = 0
    #         idx_hi = len(expend_trail)-1
    #         idx_mid = (idx_hi - idx_lo)//2
    #         while True:
    #             if idx_mid == idx_lo or idx_mid == idx_hi:
    #                 if expenditure[idx-1] > expend_trail[idx_hi]:
    #                     idx_mid = idx_hi + 1
    #                 elif expenditure[idx-1] > expend_trail[idx_lo]:
    #                     idx_mid = idx_lo + 1
    #                 else:
    #                     idx_mid = idx_lo
    #                 break

    #             if expenditure[idx-1] > expend_trail[idx_mid]:
    #                 idx_lo = idx_mid
    #             elif expenditure[idx-1] < expend_trail[idx_mid]:
    #                 idx_hi = idx_mid
    #             else:
    #                 break

    #             idx_mid = (idx_hi - idx_lo)//2

    #         expend_trail.insert(idx_mid, expenditure[idx-1])
            
    #     print(expend_trail)

    #     if d % 2 == 0:
    #         median = (expend_trail[d//2 - 1] + expend_trail[d//2])/2
    #     else:
    #         median = expend_trail[(d-1)//2]
        
    #     if expenditure[idx] >= 2*median:
    #         notifications_N += 1

    #     expend_trail.remove(expenditure[idx-d])

    print(time() - time_start, ' s')

    return notifications_N


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
