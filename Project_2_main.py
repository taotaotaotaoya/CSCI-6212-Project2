#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 22:56:00 2018

@author: tao
"""
import heapq as Heap

class Solution(object):
    def __init__(self, a=[]):
        self.a = a
        Heap.heapify(self.a) #transfer array to min heap
        self.sequence = []
        self.cost = 0
        
    def MergeSequence(self):
        if len(self.a) == 1 or len(self.a) == 0: #base case
            return self.a
        if len(self.a) > 1:
            list1 = Heap.heappop(self.a)
            list2 = Heap.heappop(self.a)
            self.sequence.append(list1)
            self.sequence.append(list2)
            new_list = list1+list2
            self.cost += new_list
            Heap.heappush(self.a, new_list)
            return self.MergeSequence()
        
    def PrintSequence(self):
        for i in range(len(self.sequence)):
            if i%2 == 1:
                times = i//2 + 1
                print(times, 'times merged lists:', self.sequence[i-1:i+1])
                
    def PrintCost(self):
        return 'Totoal Cost: ' + str(self.cost)
