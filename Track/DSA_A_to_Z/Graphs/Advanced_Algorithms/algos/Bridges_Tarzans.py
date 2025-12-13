"""
https://leetcode.com/problems/critical-connections-in-a-network/
https://www.youtube.com/watch?v=qrAub5z8FeA

Bridges -> Edge which on removal increases number of connected components in graph

IDEAS:
1. ` vistime[node]` : The time when the node was first visited during DFS.
2. ` low[node]` : The lowest visit time of all nbrs of `node` (including itself) but EXCLUDING PARENT.
    - low[node] means the earliest visited vertex that can be reached from subtree starting at `NODE`.


MAIN LOGIC:
- You are at node and exploring its nbr `nbr`.
    if low[nbr] <=vistime[node]: -> then its a NOT A BRIDGE
    if low[nbr] > vistime[node]: -> then it IS A BRIDGE
- WHY? low[nbr] <= vistime[node]: -> then its a NOT A BRIDGE
    1. low[nbr] tells the earliest visited vertex that can be reached from subtree starting at `nbr`.
    2. Here we say that low[nbr]<vistime[node], means that you can visit an ancestor of `node` from `nbr` without going through `node`.
    3. This means that removing this edge `node - nbr` will not disconnect `nbr` from the rest of the graph, as there is an alternative path to reach the ancestor of `node`.

- WHY? low[nbr] > vistime[node]: -> then it IS A BRIDGE
    - The earliest time you can visit from `nbr` and its subtree is after/more than `node` was visited.
    - This means that removing this edge ( node -> nbr ) will disconnect `nbr` and its subtree from the rest of the graph, as there is no alternative path to reach any ancestor of `node`.

- Why low[nbr] <= vistime[node]:
    - If you can earlier than `node` or even at the same time as `node still its fine
    - Because you are removing the edge (node->nbr) and not the node itself.
    
CORE IMPLEMENTATION:
- Init a timer, low, vistime dicts
- For each unvisited node, run DFS
    - Set vistime[node] and low[node] to current timer value, increment timer
    - For each nbr of node:
        - If nbr is parent, continue
        - If nbr not seen:
            - DFS(nbr, node)
            - Update low[node] = min(low[node], low[nbr])
            - Check if low[nbr] >= vistime[node]: -> then edge (node,nbr) is a bridge
        - if nbr is already seen:
            - Update low[node] = min(low[node], vistime[nbr]) # use vistime here because nbr is already visited

"""
from typing import List
from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)

        def dfs_tarzans(node: int, parent: int):
            nonlocal timer, seen
            seen.add(node)
            vistime[node] = timer
            low[node] = timer

            timer +=  1

            for nbr in adj[node]:
                if nbr == parent:
                    continue
                if nbr not in seen: # update the low of nbrs
                    dfs_tarzans(nbr, node)
                    low[node] = min(low[node], low[nbr]) # update low of current node after dfs of nbr

                    # check if node -> nbr is a bridge
                    if low[nbr] > vistime[node]:
                        bridges.append([node, nbr])
                else: # nbr is already seen -> update low
                    low[node] = min(low[node], low[nbr])


        
        vistime, low = {}, {}
        seen = set()
        timer = 0
        bridges = []
        for node in range(n):
            if node not in seen:
                dfs_tarzans(node, -1)

        return bridges