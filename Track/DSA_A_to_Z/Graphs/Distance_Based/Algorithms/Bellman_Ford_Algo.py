"""
STEPS:
- Works only on directed graph (even if undirected manually add two edges)
- Works on list of edges

Solution:
- dist[] -> dist[i] = dist from src->i
- For V-1 times run:
    - For each edge u->v: relax it
        - check if you can update path from src->v via u
- If dist[] arr still decreases after 1 more iter after (V-1) then there is a NEGATIVE CYCLE

Why (V-1 iterations)?
- Worst case: 1->2->3->4->5 (src=0, V=5)
Before starting dist[0] = 1
1st iter: dist[2] set
2nd iter: dist[3] set
...
4th iter: dist[5] set (SO IN WORST CASES YOU NEEDED V-1 Iterations)

"""


def build_adj(edges, V):
    """
    Returns: [
       0th index: [(2,10), (dest_node, wt)]
    ]
    """
    adj = [[] for _ in range(V)]
    for src, dest, wt in edges:
        adj[src].append((dest, wt))
    print(edges)
    print(adj)
    return adj 

# NOTE: nodes are 1 indexed
def bellmonFord(V, E, src, edges):
    # print(edges)
    dist = [10**8 for _ in range(V+1)]
    dist[src] = 0

    # relax all nodes V-1 times (why V-1? )
    for _ in range(len(dist) - 1):
        for u, v, wt in edges: # check if dist of "v" gets updated (u->v and wt)
            if dist[u] != 10**8 and dist[u]+wt < dist[v]:
                dist[v] = dist[u] + wt
    

    return dist[1:]