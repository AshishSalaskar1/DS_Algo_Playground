from typing import List
from queue import PriorityQueue

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capitals: List[int]) -> int:
        n = len(profits)
        jobs_done = 0

        max_heap = PriorityQueue()
        for profit, capital in zip(profits, capitals):
            max_heap.put( (capital, -profit) )
        
        while k>0 and not max_heap.empty() and jobs_done<n:
            best_cap, best_profit = max_heap.get()
            if best_cap > w:
                return w
            print(f"Picked up job {(best_cap, -best_profit)}")
            w += -best_profit
            jobs_done += 1
            k -= 1

        return w





sol = Solution()

k,w = 1,2 # 5
profits, capital = [1,2,3], [1,1,2] 
print(sol.findMaximizedCapital(k, w, profits, capital))
print()

# k,w = 2,0 # 1
# profits, capital = [1,2,3], [0,9,10] 
# print(sol.findMaximizedCapital(k, w, profits, capital))
# print()

# k,w = 2,0 # 4
# profits, capital = [1,2,3], [0,1,1] 
# print(sol.findMaximizedCapital(k, w, profits, capital))
# print()

# k,w = 3,0 # 6
# profits, capital = [1,2,3], [0,1,2 ]
# print(sol.findMaximizedCapital(k, w, profits, capital))
# print()



"""
TLE SOLUTION
"""


class SolutionTLE:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        res = w
        jobs = list(zip(profits, capital, list(range(n))))
        remaining_jobs = set(list(range(n)))

        while k>0 and len(remaining_jobs)>0: 
            max_heap = PriorityQueue()
            for i in remaining_jobs:
                if jobs[i][1] <= w:
                    print(f"valid job: {jobs[i]}")
                    max_heap.put( (-jobs[i][0],jobs[i][1],jobs[i][2]) )
            
            if max_heap.empty():
                return res

            most_profit, most_capital, job_index = max_heap.get()
            most_profit = -most_profit
            w += most_profit
            remaining_jobs.remove(job_index)

            print(f"Did job {jobs[job_index]} and rem: {remaining_jobs}")
            k -= 1
            print(k>0 and len(remaining_jobs)>0)
        
        return w