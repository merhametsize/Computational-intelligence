#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 16:56:24 2022

@author: gabri
"""

import random
import itertools
from collections import deque #for deque

def problem(N, seed=None):
    random.seed(seed)
    return [
        list(set(random.randint(0, N - 1) for n in range(random.randint(N // 5, N // 2))))
        for n in range(random.randint(N, N * 5))
    ]

#Determines whether possible_solution (deque of list) contains all of the numbers from 0 to N
def is_solution(N, possible_solution):
    solution_set = set(itertools.chain(*possible_solution)) #flattens the deque of lists into a set for fast retrieval
    numbers_1_N = set(range(0, N))
    return numbers_1_N.issubset(solution_set) #issubset() for maximum speed compared to for cycles

#Computes the number of elements inside a collection of lists (a deque of lists in this case)
def get_solution_length(solution): #flattens a deque of lists and gets its total number of elements
    flattened_list = list(itertools.chain(*solution))
    return len(flattened_list)

class Search:
    def __init__(self, N, lists):
        self.N = N
        self.lists = lists                #search space
        self.solution = lists.copy()      #dummy solution, worst case
        self.possible_solution = deque()  #efficient append() and pop() in the recursive search function
        self.nodes = 0

        print(f"N: {N}")
        print(f"Lists: {lists}")
        print(f"Number of lists: {len(lists)}")
        print("")

        self._search(0)

    def _search(self, index):
        self.nodes += 1

        #base case: possible solution found
        if is_solution(self.N, self.possible_solution):
            self.solution = self.possible_solution.copy()
            return

        #Recursive search
        for i in range(index, len(self.lists)):
            #PRUNING: if the accumulator length is greater than the insofar best solution's length, skip
            if get_solution_length(self.possible_solution) + len(self.lists[i]) > get_solution_length(self.solution):
                continue

            self.possible_solution.append(self.lists[i])
            self._search(i+1)
            self.possible_solution.pop()

def main():
    N = 50
    lists = problem(N, 42)       #search space
    
    s = Search(N, lists)
    print(f"Solution: {s.solution}")
    print(f"Nodes visited: {s.nodes}")

main()