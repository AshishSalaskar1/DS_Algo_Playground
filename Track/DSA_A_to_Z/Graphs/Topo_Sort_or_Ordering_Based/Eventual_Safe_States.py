"""
Problem: https://leetcode.com/problems/find-eventual-safe-states/submissions/1740006052/
- You are given a directed graph
    1. Terminal node: has no outgoing edges = sink = (outdegree==0)
    2. Safe Nodes: Nodes where all outgoing edges lead to a Terminal
    Note: Each terminal node is also considered to be Safe node


SOLUTION:
1) REVERSE ALL edges
- After doing this, nodes with indegree==0 ==> TERMINAL+SAFE_NODES

2) Now do BFS from this, means all the nodes you will reach in this BFS are reachable from TERMINAL Nodes
- If you reverse this, all nodes that get visited in this BFS end their path at TERMINAL Nodes
IMP: Here since you want all nodes to end at TERMINAL then indegree[nodes] == 0 ( reverse means outdegree==0 since nodes reach terminals will get cancelled out)
"""



from queue import deque
from collections import defaultdict
class Solution:
    def eventualSafeNodes(self, adj: List[List[int]]) -> List[int]:
        V = len(adj)
        rev_adj = defaultdict(list)
        q = deque()
        indegree = [0]*V

        for u in range(V):
            for v in adj[u]:
                rev_adj[v].append(u)
                indegree[u] += 1
        

        res = []
        for node in range(V):
            if indegree[node] == 0:
                q.append(node)
        

        while q:
            node = q.popleft()
            res.append(node)

            for nbr in rev_adj[node]:
                indegree[nbr] -= 1

                if indegree[nbr] == 0:
                    q.append(nbr)
        
        return sorted(res)
        