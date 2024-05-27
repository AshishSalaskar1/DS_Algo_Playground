"""
PROBLEM: https://leetcode.com/problems/hand-of-straights/description/

SOLUTION:
- LC Discuss: https://leetcode.com/problems/hand-of-straights/solutions/135655/python-o-nlgn-simple-solution-with-intuition

INTUTION:
- Wkt if you know start of each group, then remaining elements are consecutive
- Also, if len(arr) = N, then you will have N//group+size starting element and groups

PQ: push everything and not count
CMAP: Used to hold frequency of numbers n how many of those are already used

"""

from queue import PriorityQueue
from collections import Counter
class Solution:
    def isNStraightHand(self, arr: List[int], group_size: int) -> bool:
        n = len(arr)
        cmap = Counter(arr)

        #  [1, 2, 2, 3, 3, 4, 6, 7, 8]
        if n%group_size != 0: # you cant divide equally into groups
            return False
        if group_size == 1:
            return True
        
        pq = PriorityQueue()
        for x in arr:
            pq.put(x)
        
        ngroups = n//group_size
        for _ in range(ngroups): # find if each group exists
            start = pq.get() # get lowest number -> start of this group
            while cmap[start] == 0: # in case the min number is already used before
                start = pq.get()
            
            for i in range(group_size):
                cmap[start] -= 1 # one number is used up
                if cmap[start] < 0: # you dont have start, start+1, start+2
                    return False 
                start += 1 # find next element in the groups
        

        return True
        

        