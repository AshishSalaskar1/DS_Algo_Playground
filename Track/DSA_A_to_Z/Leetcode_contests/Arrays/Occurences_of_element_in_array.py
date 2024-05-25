from typing import List

"""
PROBLEM
LINK: https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/description/\

- You are given an integer array nums, an integer array queries, and an integer x.
- For each queries[i], you need to find the index of the queries[i]th occurrence of x in the nums array. If there are fewer than queries[i] occurrences of x, the answer should be -1 for that query.
- Return an integer array answer containing the answers to all queries

"""

class Solution:
    def occurrencesOfElement(self, arr: List[int], queries: List[int], element: int) -> List[int]:
        res = []
        cmap = {}
        
        for idx, x in enumerate(arr):
            if x != element: # you need to find occurences of one element only
                continue
            if x in cmap:
                cmap[x].append(idx)
            else:
                cmap[x] = [idx]
        
        for k_occurence in queries: # You need to find the `k_occurence` of `element`
            if element in cmap:
                occurences = cmap[element]
                if k_occurence-1 < len(occurences):
                    res.append(occurences[k_occurence-1])
                else:
                    res.append(-1)
            else:
                res.append(-1) 
        
        return res