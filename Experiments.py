#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 01:18:26 2018

@author: tao
"""
import time
import Project_2_main

Test_case = [[1000]*1000, [1000]*1500, [1000]*2000, [1000]*2500]
n = 1
for test in Test_case:
    begin_time = time.time()
    Array = Project_2_main.Solution(test)
    after_merging_list = Array.MergeSequence()
    #Array.PrintSequence()
    print('Test Case', n, ':')
    print('After Merging list:', after_merging_list)
    print(Array.PrintCost())
    end_time=time.time()
    print('Running time is', (end_time-begin_time)*1000, 'ms.')
    n += 1
    print('\n')