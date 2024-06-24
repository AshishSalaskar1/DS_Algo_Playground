"""
PROBLEM: https://leetcode.com/problems/total-cost-to-hire-k-workers/
- You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.
- You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:

- You will run k sessions and hire exactly one worker in each session.
In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. Break the tie by the smallest index.
For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.
A worker can only be chosen once.
Return the total cost to hire exactly k workers.


=> Example 1:

Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
Output: 11
Explanation: We hire 3 workers in total. The total cost is initially 0.
- In the first hiring round we choose the worker from [17,12,10,2,7,2,11,20,8]. The lowest cost is 2, and we break the tie by the smallest index, which is 3. The total cost = 0 + 2 = 2.
- In the second hiring round we choose the worker from [17,12,10,7,2,11,20,8]. The lowest cost is 2 (index 4). The total cost = 2 + 2 = 4.
- In the third hiring round we choose the worker from [17,12,10,7,11,20,8]. The lowest cost is 7 (index 3). The total cost = 4 + 7 = 11. Notice that the worker with index 3 was common in the first and last four workers.
The total hiring cost is 11.

SOLUTION:
- Maintain 2 PQ (one stores first `candidate` eles and another stores last `candidate` eles)
- Initially, start_ptr=0 (start_pq) and end_ptr=n-1 (last_pq)

- Iterate until k>0
    - Put elements in start_pq till you have `candidate` elements and start_ptr<=end_ptr (you dont want to include elements in both - put in either)
    - Put elements in end_pq till you have `candidate` elements and start_ptr<=end_ptr (you dont want to include elements in both - put in either)
    - Pick min of both (and then put back the one not choses in respective PQ)
"""
from queue import PriorityQueue
class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        n = len(costs)
        start_pq = PriorityQueue()
        end_pq = PriorityQueue()
        total_cost = 0

        start_ptr, end_ptr = 0,n-1


        while k>0:
            while start_pq.qsize()<candidates and start_ptr<=end_ptr:
                start_pq.put((costs[start_ptr], start_ptr))
                start_ptr += 1

            while end_pq.qsize()<candidates and start_ptr<=end_ptr:
                end_pq.put((costs[end_ptr], end_ptr))
                end_ptr -= 1
            # print(start_pq.queue,end_pq.queue)
            min1 = start_pq.get() if not start_pq.empty() else (float("inf"), -1)
            min2 = end_pq.get() if not end_pq.empty() else (float("inf"), -1)

            # in case both are same, pick from start (lesser index)
            if min1[0] <= min2[0]: # pick from start candidates
                total_cost += min1[0]
                end_pq.put(min2) # put back last min candidate
            else: # pick from end candidates
                total_cost += min2[0]
                start_pq.put(min1) # put back first min candidate

            k -= 1

        return total_cost


# sol = Solution()
# sol.totalCost(costs=[17,12,10,2,7,2,11,20,8], k=3, candidates=4)
# sol.totalCost(costs=[1,2,4,1], k=3, candidates=3)
# sol.totalCost(costs=[10,1,11,10], k=2, candidates=1) # 11
# sol.totalCost(costs=[31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58], k=11, candidates=2) # 423