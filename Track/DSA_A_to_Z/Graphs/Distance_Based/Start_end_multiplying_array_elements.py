"""
SOLUTION 1: Pure BFS
Why bfs works? First time you reach the end will be best/shortest way 
(since its shortest path in length and not in terms of weights
, if it was weighted then longer path may also be better/minimal in terms on weights)

SOLUTION 2: Use Dijstras (not needed)
- In this case dist[] will be of size 10^3 (since you do mod with this, it can never exceed this)

"""

from typing import *
from queue import PriorityQueue

def minimumOperations(n: int, start: int, end: int, arr: List[int]):
    q = []
    q.append((0, start))
    vis = set()
    vis.add(start)

    if start == end:
        return 0

    while len(q) != 0:
        dist, u = q.pop(0)

        for x in arr:
            v = u*x % (10**3)
            if v == end:
                return dist+1
            elif v not in vis:
                q.append((dist+1, v))
                vis.add(v)

    
    return -1


# def minimumOperations(n: int, start: int, end: int, arr: List[int]):
#     pq = PriorityQueue()
#     pq.put((0, start))
#     dist  = [float("inf") for _ in range(10**3+1)]
#     dist[start] = 0 

#     while pq.qsize() != 0:
#         udist, u = pq.get()
#         for x in arr:
#             v = (u*x)%(10**3)
#             if (udist+1) < dist[v]:
#                 dist[v] = udist+1 
#                 pq.put((udist+1, v))

    
#     return dist[end] if dist[end] != float("inf") else -1




