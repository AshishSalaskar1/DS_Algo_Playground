"""
PROBLEM: https://leetcode.com/problems/minimum-cost-to-convert-string-i/
SOLUTION: Use Floyd-Warsall algo for all pairs shortest paths
- Djikstras gives TLE here

TC: O(26x26x26) + O(N)
"""
from typing import List, Tuple

class FW:
    def __init__(self, edges: List[Tuple[str, str, int]]):
        self.adj = [[float("inf") for _ in range(26)] for _ in range(26)]
        for i in range(26):
            self.adj[i][i] = 0

        for u, v, wt in edges:
            u,v = ord(u)-ord('a'), ord(v)-ord('a')
            self.adj[u][v] = min(self.adj[u][v], wt)

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if self.adj[i][k] != float("inf") and self.adj[k][j] != float("inf"):
                        self.adj[i][j] = min(self.adj[i][j], self.adj[i][k] + self.adj[k][j])

    def shortest_dist(self, src: str, dest: str) -> int:
        src, dest = ord(src)-ord('a'), ord(dest)-ord('a')
        return self.adj[src][dest] if self.adj[src][dest] != float("inf") else -1

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(source)
        fw = FW(list(zip(original, changed, cost)))
        seen_dist = {}

        total_cost = 0
        for i in range(n):
            src_char, dest_char = source[i], target[i]
            cur_cost = fw.shortest_dist(src_char, dest_char)

            if cur_cost == float("inf") or cur_cost == -1:
                return -1
            total_cost += cur_cost

        return total_cost

"""
DIJKSTRAS SOLUTION
https://leetcode.com/problems/minimum-cost-to-convert-string-i/?envType=daily-question&envId=2026-01-29

How to avoid TLE using Dijstras here?
- You can precompute the shortest distance from each character to every other character using Dijkstra's algorithm and store these distances in a dictionary.
"""
from collections import defaultdict
from heapq import heappush, heappop, heapify
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        def dijstras(nodes: list, adj: dict, source: str) -> int:
            pq = []
            dist = {  node:float("inf") for node in nodes}
            print(dist)
            heappush(pq, (source, 0))
            dist[source] = 0

            while pq:
                node, curdist = heappop(pq)
                
                for nbr, wt in adj[node]:
                    newdist = curdist + wt
                    if newdist < dist[nbr]:
                        dist[nbr] = newdist
                        heappush(pq, (nbr, newdist))
            return dist
        
        allnodes = set()
        adj = defaultdict(list)
        for i in range(len(original)):
            u,v = original[i], changed[i]
            adj[u].append((v, cost[i]))
            allnodes.add(u);allnodes.add(v)
        
        allnodes = list(allnodes)
        chardistmap = { chr:dijstras(allnodes, adj, chr) for chr in allnodes}

        cost = 0

        if len(source) != len(target):
            return -1

        for i in range(len(source)):
            src, dest = source[i], target[i]

            if src == dest: 
                continue
            elif src not in adj: 
                return -1
            else:
                mincost = chardistmap[src].get(dest, float('inf'))
                if mincost == float("inf"):
                    return -1
                else:
                    cost += mincost
        
        return cost

















