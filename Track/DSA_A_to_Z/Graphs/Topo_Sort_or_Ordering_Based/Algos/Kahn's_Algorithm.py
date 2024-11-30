"""
USE BFS here for TOPOLOGICAL SORT

Indegree[node] : no of incoming edges to this node
LOGIC
- If indegree =0, means that node can come first in order (since no nodes come before this), add such to the Q
- When u visit nbrs, u do indegree[nbr] -= 1 (Because the parent node was already added to topo order n will come before this)
- Now when u visit nbrs n decrement them, u add them to Q in case its indegree = 0
  (Means parents of this node is added in order, so now consider this as psuedo-root)

SOLID ASSUMPTION:
- If after running Kahns algo on your graph if all nodes are not visited -> GRAPH HAS CYCLE
- Kahsn algo doesnt work with Cycles. It works only on DIRECTED-ACYCLIC-GRAPH
"""

# USING KAHNS
def topologicalSort(adj, v, e):
    vis = set()
    topo_sort = []
    indegs = [0 for _ in range(v)]

    q = []
    for node in range(v):
        for nbr in adj[node]:
                indegs[nbr] += 1

    for i in range(v):
        if indegs[i] == 0:
            q.append(i)
            vis.add(i)

    # BFS
    while len(q) != 0:
        curr = q.pop(0)
        # added cur node with nothing incoming to topological sorted order
        topo_sort.append(curr)

        for nbr in adj[curr]:
            if nbr not in vis:
                indegs[nbr] -= 1

                # in case this node doesnt have any incoming edges add to Q
                # since all nodes leading to this have been added in topo
                if indegs[nbr] == 0:
                    q.append(nbr)
                    vis.add(nbr) # here vis means -> this nodes parents were all added n this also got added in topo sort

    print(topo_sort)
    return topo_sort