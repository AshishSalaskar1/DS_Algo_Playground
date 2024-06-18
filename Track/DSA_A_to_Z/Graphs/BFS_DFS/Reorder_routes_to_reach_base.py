"""
PROBLEM: Reorder Routes to Make All Paths Lead to the City Zero
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

- You are given a graph of N nodes such that there is only one way to travel from one city to another (assumption can be no cycles)
- You need to flip any paths such that you can reach node `0` from all nodes
- Find min number of paths you need flip to achiece this


INTUITION
- Consider this as a UNDIRECTED GRAPH
- BUT Maintain a flag saying if its i->j or j->i
- Start doing a DFS from 0 -> to all nodes
    - When you visit nbrs of lets say node
    - Check flag if node->nbr or nbr->node
        1) if nbr->node (correct place, you want to COME TO 0 FROM OTHERS)
        2) if node-> nbr (consider this as FLIP ROAD)

Ref: https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/solutions/3334051/easy-solutions-with-exaplanation-in-java-python-and-c-look-at-once/?envType=study-plan-v2&envId=leetcode-75

"""
from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in connections:
            adj[u].append((v, 1)) # 1 indicates the edge needs to be reversed to reach city 0
            adj[v].append((u, 0)) # 0 indicates the edge is already correctly oriented

        stack = [0]
        visited = set([0])
        reverses = 0

        while stack:
            node = stack.pop()
            for neighbor, direction in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    if direction == 1: # node->nbr (you want nbr->node)
                        reverses += 1
                    stack.append(neighbor)

        return reverses
