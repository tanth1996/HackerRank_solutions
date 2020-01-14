#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2): 
    lcs_lut = [[None]*(len(s2)+1) for i in range(len(s1)+1)] 
  
    for i in range(len(s1) + 1): 
        for j in range(len(s2) + 1): 
            if i == 0 or j == 0 : 
                lcs_lut[i][j] = 0
            elif s1[i-1] == s2[j-1]: 
                lcs_lut[i][j] = lcs_lut[i-1][j-1] + 1
            else: 
                if lcs_lut[i-1][j] > lcs_lut[i][j-1]:
                    lcs_lut[i][j] = lcs_lut[i-1][j]
                else:
                    lcs_lut[i][j] = lcs_lut[i][j-1]
  
    return lcs_lut[-1][-1] 

# Works but raises runtime error on large cases
def commonChild_recursion(s1, s2):
    lcs_lut = {}

    def lcs(s1, s2, end_s1, end_s2):
        if (end_s1, end_s2) in lcs_lut:
            return lcs_lut[(end_s1, end_s2)]
        elif end_s1 == 0 or end_s2 == 0:
            lcs_len = 0
        elif s1[end_s1-1] == s2[end_s2-1]:
            lcs_len = lcs(s1, s2, end_s1-1, end_s2-1) + 1
        else:
            lcs1 = lcs(s1, s2, end_s1-1, end_s2)
            lcs2 = lcs(s1, s2, end_s1, end_s2-1)
            lcs_len = lcs1 if lcs1 > lcs2 else lcs2

        lcs_lut[(end_s1, end_s2)] = lcs_len
        return lcs_len

    lcs_len = lcs(s1, s2, len(s1), len(s2))

    
    return lcs_len

def commonChild_attempt(s1, s2, recurse_reverse=True):
    s2_lut = {}
    for idx, char in enumerate(s2):
        if char not in s2_lut:
            s2_lut[char] = []
        s2_lut[char].append(idx)

    max_str_len = 0
    max_str_chars = []

    for idx_s1_start, char in enumerate(s1):
        max_str_chars_chk = []
        if char not in s2_lut:
            continue
        
        idx_s2 = s2_lut[char][0]
        max_str_chars_chk.append(char)

        for char in s1[idx_s1_start+1:]:
            if char in s2_lut:
                for idx_char_tgt in s2_lut[char]:
                    if idx_char_tgt > idx_s2:
                        max_str_chars_chk.append(char)
                        idx_s2 = idx_char_tgt
                        break
        
        if len(max_str_chars_chk) > max_str_len:
            max_str_len = len(max_str_chars_chk)
            max_str_chars = max_str_chars_chk

    print(max_str_chars, max_str_len)
    if recurse_reverse:
        max_str_len_reverse = commonChild(s2, s1, recurse_reverse=False)
        if max_str_len_reverse > max_str_len:
            return max_str_len_reverse
    return max_str_len


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
