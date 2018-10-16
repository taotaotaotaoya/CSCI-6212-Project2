#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 01:13:37 2018

@author: tao
"""

import Project_2_main

test_case = [1000]*20
Array = Project_2_main.Solution(test_case)
after_merging_list = Array.MergeSequence()
print('After Merging list:', after_merging_list)
Array.PrintSequence()