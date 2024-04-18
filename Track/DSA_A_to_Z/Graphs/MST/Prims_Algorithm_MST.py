
"""

MST -> Tree/graph having N nodes and exactly N-1 edges such that all nodes are reachable from any node (1-single connected island)

GREEDY WAY 
- For each node visit all nodes adj to it and store the dist -> MARK CUR AS VISITED
- if pq.get() node is visited -> ignore (You might have this node since it was reachable via more than 1 previous nodes, 
and out of those min path has been already popped and added to MST)
- min_heap will automatically return the nearest node which you can now visit (U only mark as vis when you get it out from PQ)
"""

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)


from queue import PriorityQueue


# Edge class for storing the Edges of thee graph
class Edge:
    
    def __init__(self, start, end, weight) :

        self.start = start
        self.end = end
        self.weigth = weight


def minimumSpanningTree(edges, V, E):
    edges = [(x.start, x.end, x.weigth) for x in edges]
    adj = [[] for _ in range(V)]

    for u,v,wt in edges:
        adj[u].append((v,wt))
        adj[v].append((u,wt))


    pq = PriorityQueue()
    vis = set()
    total_wt = 0

    pq.put((0,0,0)) #start from node 0

    while pq.qsize() != 0:
        udist, node, parent  = pq.get()
        if node in vis:
            continue

        total_wt += udist
        vis.add(node)

        # nbrs of u which are not yet added to MST
        for v,wt in adj[node]:
            if v not in vis:
                pq.put((wt, v, node))
        

    
    return total_wt











