"""
https://leetcode.com/problems/maximum-number-of-k-divisible-components/?envType=daily-question&envId=2025-11-28


SIMPLE LOGIC:
- Start PRUNING from the leaf nodes
- Starting from the leaf nodes and moving up, whenver u see that a subtree-sum is mulitple of k -> cut that off
"""
from collections import defaultdict
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:

        
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        res = 0

        def dfs(node: int, parent: int):
            nonlocal res
            if node is None:
                return 0
            
            csum = values[node] # sub tree sum ( cur_node + all other sub nodes)
            for nbr in adj[node]:
                if nbr != parent:
                    csum += dfs(nbr, node)
            
            if csum%k == 0: # is this subtree sum multiple of K?
                res += 1 # if yes -> separate it into island
                return 0
            
            return csum%k # in case you can cut this tree
        
        dfs(0,-1)
        return res
                    