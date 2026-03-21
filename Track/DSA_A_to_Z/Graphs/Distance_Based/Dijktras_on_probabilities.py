"""
https://leetcode.com/problems/path-with-maximum-probability/submissions/1955051123/


IDEA: 
- In Dijktras we minimize the path, here we maximize the Probability ( Hence we use maxheap instead of minheap )
- Greedy Approach:
  - Here we assume that at each `node` we find the nbr with `max_prob` and move there, we do this till we reach `end`
  

"""
from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = defaultdict(list)
        for i in range(len(edges)):
            src, dest, prob = edges[i][0], edges[i][1], succProb[i]
            adj[src].append((dest, prob))
            adj[dest].append((src, prob))
        
        reach_probs = [0.0 for _ in range(n)]
        reach_probs[start] = 1.0 # Prob of reaching start from start is 1 ( you are already there)

        pq = []
        heappush(pq,(-1, start)) # ( prob_to_reach_here_from_start, node)
        while pq:
            prob_to_reach_here, node = heappop(pq)
            prob_to_reach_here = -prob_to_reach_here

            for nbr, prob in adj[node]:
                new_prob = prob*prob_to_reach_here
                if new_prob > reach_probs[nbr]:
                    reach_probs[nbr] = new_prob 
                    heappush(pq, (-new_prob,nbr))
        
        return reach_probs[end]




        