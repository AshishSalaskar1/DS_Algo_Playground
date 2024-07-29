"""
PROBLEM: https://leetcode.com/problems/ipo/description/

SOLUTION:
- https://leetcode.com/problems/ipo/solutions/5315041/easy-to-understand-fast-maxheap-sorting

LOGIC:
- IMP: You dont spend w/capital in doing, its considered as added
    Ex: w=1, you do job with 1 capital => now your w = w+profit(job_done)
    
> TLE LOGIC:
    - put all jobs having capital<=w into MaxHeap and pick best based on profit
    - mark that job as done => k-= 1
    - Do this until k>0, len(MaxHeap)>0 and jobs_done<njobs

> OPTIMIZED LOGIC
- Wkt if w is our base capital, we need max profit of all elements with capital<w
- Then for picking up next elements we need max profit of all elements remaining with capital<w+profit_from_last

1. Sort list<capital,profit> based on capital
2. keep pointer call job_idx indicating how many jobs are inserted into MaxHeap
3. For each k,
    - Put all nodes starting from job_idx until their capital <= current_w
    - Then pick top profit one among them (remaining will stay in the MaxHeap)
- In this way, you are always sure that elements < cur_w are already in the MaxHeap and you can only add new elements. Because of SORTING ON CAPITAL

=> Why cant you put (capital, -profit) in MaxHeap? (pick lowest capital and highest profit)
- Lets say w=3 | k=1, jobs = [(0,1), (3,999), (3,9999)]
In this case you will pickup (0,1) [lowest_index and highest profit] which is wrong since you have `k`=1
- Hence you can pick any element with capital <= current_w (NOT with lowest capital) 
"""
from queue import PriorityQueue

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capitals: List[int]) -> int:
        n = len(profits)
        
        jobs = sorted(list(zip(capitals, profits)))
        jobs_added_idx = 0
        jobs_done = 0
        max_heap = PriorityQueue()

        while k>0 and jobs_done<n:
            while jobs_added_idx<n and jobs[jobs_added_idx][0] <= w:
                max_heap.put( -jobs[jobs_added_idx][1] )
                jobs_added_idx += 1
            
            if max_heap.empty():
                return w
            
            w += -max_heap.get()
            jobs_done += 1
            k -= 1

        return w


        