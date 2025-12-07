"""
BFS - USE QUEUE or FIFO

- Here we are using adjacency list for representing a graph which is a BiDirectional graph
- Also keep track of visited nodes since Graph may have cycle


V = 5, E = 4
adj = {{1,2,3},{},{4},{},{}}
OUTPUT: 0 1 2 3 4

V = 3, E = 2
adj = {{1,2},{},{}}
OUTPUT: 0 1 2

"""

from typing import List

def bfsOfGraph(V: int, adj: List[List[int]]) -> List[int]:
    bfs = []
    n_nodes = len(adj)
    root_node = 0
    
    q = [root_node]
    vis = set()
    vis.add(root_node)
    
    while len(q) != 0:
        # get first element of queue: FIFO
        cur_node = q.pop(0)
        bfs.append(cur_node)
        
        for nbr in adj[cur_node]:
            if nbr not in vis:
                # mark node as visited
                vis.add(nbr)
                q.append(nbr)
    
    return bfs


V = 5; E = 4
adj = {0: [1,2,3],1:[],2:[4],3:[],4:[]}
bfsOfGraph(V, adj)