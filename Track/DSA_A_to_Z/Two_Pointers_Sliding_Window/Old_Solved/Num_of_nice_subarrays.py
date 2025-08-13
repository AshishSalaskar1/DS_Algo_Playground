"""
PROBLEM:
Link: https://leetcode.com/problems/count-number-of-nice-subarrays/
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

SOLUTION:
- Nice subarray -> subarray which should contain exactly "k" odd numbers (it can contain any number of even numbers also)
- Question Change: replace odd numbers = 1 and even=0
- Now your question becomes find num of subarrays giving sum=k

- Normal sum=k using prefix sum
- REMEMBBER: You need count and not longest, so for each csum store number of times it was seen
"""

class Solution:
    def numberOfSubarrays(self, arr: List[int], k: int) -> int:
        n = len(arr)
        arr = [1 if x%2==1 else 0 for x in arr] # odd=1, even=0

        hmap = {}
        csum = 0
        rescount = 0
        for i,x in enumerate(arr):
            csum += x
            if csum == k:
                rescount += 1
            
            target = csum - k
            if target in hmap:
                rescount += hmap.get(target)

            hmap[csum] = hmap.get(csum,0) + 1 # keep track of how many times csum was seen

        return rescount 

