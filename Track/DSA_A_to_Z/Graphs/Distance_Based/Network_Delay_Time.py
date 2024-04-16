"""
Question:
- You are given a network of n nodes, labeled from 1 to n.
- You are also given times, a list of travel times as directed edges
We will send a signal from a given node k. 
Return the minimum time it takes for all the n nodes to receive the signal. 
If it is impossible for all the n nodes to receive the signal, return -1.

 
Solution:
- Do normal Dijsktras from "src" node, this will give you least time to reach all nodes from "src"
- Min time to reach all nodes from "src": MAX(distances)
- Why max? since you need to reach all nodes, farthest node - least time is taken
"""

from queue import PriorityQueue

class Solution:
    def create_adj(self, V, edges):
        adj = [[] for _ in range(V)]
        for u,v,wt in edges:
            adj[u].append((v,wt))
        
        return adj

    def networkDelayTime(self, times: List[List[int]], n: int, src_node: int) -> int:

        pq = PriorityQueue()
        adj = self.create_adj(n+1, times)
        # nodes based on 1-based indexing
        dist = [float("inf") for _ in range(n+1)]

        pq.put((0,src_node))
        dist[src_node] = 0

        while pq.qsize() != 0:
            udist, u = pq.get()
            
            for v,wt in adj[u]:
                if udist + wt < dist[v]:
                    dist[v] = udist + wt
                    pq.put((udist+wt, v))
        

        # shortest time to reach all nodes
        shortest_time = max(dist[1:])

        if shortest_time == float("inf"):
            return -1
        else:
            return shortest_time