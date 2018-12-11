#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 23:12:05 2018

@author: pamela
"""
import itertools
with open('day1_input.txt', 'r') as in1:
    data = in1.readlines()
    
nums = [int(dat.rstrip('\n')) for dat in data]
sum(nums) 

#Part 2
freq = 0
seen = {0}

for dat in itertools.cycle(data):
    freq += int(dat)
    if freq in seen:
        print(freq); break
    seen.add(freq)