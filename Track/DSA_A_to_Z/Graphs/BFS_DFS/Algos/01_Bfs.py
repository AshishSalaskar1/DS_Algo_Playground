"""
BFS - USE QUEUE or FIFO

LOGIC OF USING 0-1 BFS
- Lets say you are given a graph with only 0/1 weights and asked to find shortest path from some Node
- You just use DJIKSTRAS -> but this is said to be faster [DONT BOTHER MUCH]


- Here we are using adjacency list for representing a graph which is a BiDirectional graph
- Also keep track of visited nodes since Graph may have cycle

01 BFS
- In BFS you consider each level to increase the depth by 1
- If you follow this, your Queue at any point satisifies this condition
    1. There is certain point below which all nodes stored have depth = i
    2. All nodes in Queue above that point will have depth = i+1
    3. Ideally lower depth will lie at bottom n increase on top (Later you add the more the depth)

- NOW here, you have some nodes whose edge weight = 0, this needs to be at the bottom of the Q and not on top

V = 5, E = 4
adj = {{1,2,3},{},{4},{},{}}
OUTPUT: 0 1 2 3 4

V = 3, E = 2
adj = {{1,2},{},{}}
OUTPUT: 0 1 2


"""

from typing import List
from collections import deque

def bfsOfGraph(src: int, adj: List[List[(int,int)]]) -> List[int]:
    vis = set()
    q = deque([(src,0)])

    while len(q) != 0:
        node, dist = q.popleft()
        vis.add(node)
        for nbr, wt in adj[node]:
            if nbr not in  vis:
                if wt==1:
                    q.append((node, 1+dist)) # add to right (TOP)
                elif wt==0:
                    q.appendleft((node, 1+dist))
                    
