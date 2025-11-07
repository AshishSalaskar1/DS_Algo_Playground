"""
Problem: https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/


SOLUTION IDEAS:

MAIN:
- To check if `k` tasks can be complete, you pick `k` STRONGEST PEOPLE and `k` EASIEST TASKS
- WHY? Seems to help me greedy and makes logical sense


CHECK:
- Pick hardest task, Strongest worker -> check if he can do it
- If he cant do, then you need to give ONE pill to any worker
    💡DOESNT MEAN U GIVE THE PILL TO THE STRONGEST ONE ALWAYS?
    - Because who knows a weaker worker with this skill might be able to do this task
    - Hence, use binary search -> pop that weakest worker who can do this with this one pill added
"""


from sortedcontainers import SortedList
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        nt, nw = len(tasks), len(workers)

        tasks = sorted(tasks)
        workers = sorted(workers)

        def isPossible(target: int):
            ws = SortedList(workers[nw-target:])
            p = pills
            for i in range(target-1,-1,-1):
                if ws[-1] >= tasks[i]:
                    ws.pop()
                else: # you are giving pill to worker 
                    if p == 0: return False
                    # which worker to give pill to? Weakest who can do it. Hence bisect_left
                    best_worker = ws.bisect_left(tasks[i]-strength)
                    if best_worker == len(ws): return False
                    else: ws.pop(best_worker)
                    p -= 1
            
            return True
        
        lo, hi = 1, min(nt,nw)
        res = 0
        while lo<=hi:
            mid = lo+(hi-lo)//2
            if isPossible(mid):
                res = max(res, mid)
                lo = mid+ 1
            else:
                hi = mid-1
        return res




        