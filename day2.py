#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 21:35:11 2018

@author: pamela
"""
from collections import Counter

with open('day2_input.txt', 'r') as in2:
    strings = in2.readlines()

clean_str = [(string.rstrip('\n')) for string in strings]

idx2 = 0
idx3 = 0
for clean in clean_str:
    str_count = Counter(clean)
    if 2 in str_count.values():
        idx2 += 1
    if 3 in str_count.values():
        idx3 +=1

#Part 2
for i in range(len(clean_str)-1):
    for j in range(i, len(clean_str)-1):
        clean_str[i]
        almost_match = 0
        for c in range(26):
            if not (clean_str[i][c] == clean_str[j][c]):
                almost_match +=1
        #print(almost_match)
        if almost_match == 1:
            print(i, clean_str[i], clean_str[j])
            break