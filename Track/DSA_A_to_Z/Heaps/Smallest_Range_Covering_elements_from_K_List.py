"""
Problem: https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists
[(0, 1), (4, 0), (5, 2), (9, 1), (10, 0), (12, 1), (15, 0), (18, 2), (20, 1), (22, 2), (24, 0), (26, 0), (30, 2)]

QUESTION:
- You need to find min diff range [start,end] such that this range contains atleast 1 element from each list

SOLUTION:
- Flatten list with (num, array_index) -> sort it

- NEW QUESTION: Find the window with atleast 1 element from each list -> and its range is lowest
"""

from collections import defaultdict
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        arr = []

        for i in range(len(nums)):
            for x in nums[i]:
                arr.append((x,i))

        arr = sorted(arr, key=lambda x:x[0])

        k = len(nums)        
        n = len(arr)
        rstart, rend = 0, (10**5)+1
        l,r = 0,0
        takenmap = defaultdict(int)
        while r<n:
            takenmap[arr[r][1]] += 1

            if len(takenmap)<k: # doesnt have elements from every list
                r += 1
            else:
                while len(takenmap) == k: # SHRINK RANGE TILL VALID
                    if (arr[r][0]-arr[l][0]) < (rend-rstart):
                        rstart, rend = arr[l][0], arr[r][0]
                    
                    takenmap[arr[l][1]] -= 1
                    if takenmap[arr[l][1]] == 0: takenmap.pop(arr[l][1])
                    l += 1
                
                r += 1
            # print("TURN DONE\n")
        
        return [rstart,rend]
            

                