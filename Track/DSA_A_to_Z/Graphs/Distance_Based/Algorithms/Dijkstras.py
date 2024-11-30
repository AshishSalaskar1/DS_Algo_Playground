"""
ALGORITHM
-> dist array: dist[i] stores distance src->i (we want to minimize this)
    All set to INF except src=0 (src->src takes 0 distance)
-> min_heap -> elements are (dist_from_src_to_this_node, node)

- Why PriorityQueue:    
    - Acts like greedy method, you pick nearest length (assuming nbrs of this will be nearest -> DOESNT ALWAYS NEED TO BE TRUE)
    - N since we add only to PQ if better dist is met, we reduce lot of unecessary (dist_to_node,node) pairs that we would have inserted
- TC: V* (ELogV )

while min_heap is not empty:
        d, node <- heap.peek()
        visit all nbrs of node:
            dist_to_reach_nbr = min_dist_to_reach_node (saved in heap) + weight(node -> nbr)
            if dist_to_reach_nbr < dist[nbr] and min_dist_to_reach_node!=INF:
                update dist[nbr] and update same in heap to pick up next iteration

PriorityQueue Doc
 length = pq.qsize()
- You can any comparable types in PQ (tuples, list..)
- But you cant mix up element types (Ex: one int n rest tuples)
1. MIN_HEAP
    pq = PriorityQueue()
    - insert: pq.put()
    - peek: 
        pq.queue[0] <- smallest 
        pq.queue[-1] <- largest (but you cant pop this one)
    - pop: pq.get() <- POPS SMALLEST ELE

2 . MAX_HEAP
   - No default implementation of max heap (workaround: negate numbers while put and get)
    pq = PriorityQueue()
    pq.put(-x) -> popped_ele = -pq.get()

"""

from typing import List
from queue import PriorityQueue


def build_adj(edges, V):
    """
    Returns: [
       0th index: [(2,10), (dest_node, wt)]
    ]
    """
    adj = [[] for _ in range(V)]
    for src, dest, wt in edges:
        adj[src].append((dest, wt))
        adj[dest].append((src, wt))

    return adj 


def dijkstra(edges: List[List[int]], V: int, E: int, src: int):
    adj = build_adj(edges, V)
    pq = PriorityQueue()

    # add src node to PQ
    pq.put((0,src))

    # dist[i] -> dist of node "i" from "src"
    dist = [float("inf") for _ in range(V)]
    dist[src] = 0

    while pq.qsize() != 0:
        udist, u = pq.get() # pick node at least distance in PQ from src

        # visit all nbrs of node and update
        for v, wt in adj[u]:
            if udist + wt < dist[v]: # shorter path found  from src->nbr
                dist[v] = udist+wt
                pq.put((udist+wt, v))

    return dist


