# Graphs Cheatsheet

Basics
- Represent with adj list; BFS for unweighted shortest paths; DFS for components/ordering
- Detect cycles: directed (DFS colors), undirected (parent check)
- Topo sort: Kahn’s (BFS indegree) or DFS postorder

Multi-source BFS
- Push all sources initially into queue with dist=0; expands layers simultaneously
- Finds min distance to any of the sources

Shortest paths
- Unweighted: BFS
- Weighted non-negative: Dijkstra (heap)
- With negatives but no cycles: Bellman-Ford; with cycle detection
- All pairs small N: Floyd–Warshall

Components
- Connected components via DFS/BFS
- DSU for dynamic connectivity or Kruskal MST

Trees as graphs
- Root, compute depth/parent; use LCA/binary lifting; Euler Tour for subtree queries

Pitfalls
- 1-based vs 0-based nodes; directed vs undirected edges; self-loops/multiedges

# Graphs Cheatsheet (verbatim)

BFS traversal demo (from Graphs/Graph_and_Types.py)
```python
from typing import List

def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
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
```

Is Graph Bipartite (BFS coloring) (from Graphs/BFS_DFS/Bipartite_Graph.py)
```python
from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        V = len(graph)
        colors = [-1] * V

        for i in range(V):
            if colors[i] != -1:
                continue
            
            q = deque([i])
            colors[i] = 0  # Assign color 0

            while len(q) != 0:
                node = q.popleft()
                for nbr in graph[node]:
                    if colors[nbr] == colors[node]:
                        return False
                    elif colors[nbr] == -1:  # Fixed typo here
                        colors[nbr] = 1 if colors[node] == 0 else 0
                        q.append(nbr)
        
        return True
```

Detect cycle in undirected graph (BFS parent tracking) (from Graphs/BFS_DFS/Cycle_Detection_in_undirected_Graph….py)
```python
def detect_cycle(adj):
    V = len(adj)

    # iterate all nodes and do BFS on each
    for i in range(V):
        # (node, where did u visit this from)
        q = [(i, -1)]
        vis = set([i])

        while len(q) != 0:
            curr, parent = q.pop(0)
            for nbr in adj[curr]:
                if nbr not in vis:
                    q.append((nbr, curr))
                    vis.add(nbr)
                # 1 <-> 2 <-> 3
                # nbr is visited already, but u came from this node only
                elif parent != nbr:
                    return True

    return False
```

Topo sort with Kahn’s algorithm (from Graphs/Topo_Sort_or_Ordering_Based/Course_Schedule_-_II.py)
```python
def topologicalSort(adj, v):
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


    topo_sort = [x+1 for x in topo_sort]
    
    if len(topo_sort) == v:
        return topo_sort
    else: # cycle present
        return []
```

Prim’s Minimum Spanning Tree (from Graphs/MST/Prims_Algorithm_MST.py)
```python
from queue import PriorityQueue

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
```

---

## 🗺️ Quick map
- 🌿 BFS/DFS basics and when to use each
- 🔁 Cycle detection (directed vs undirected)
- 🧱 Topological ordering (Kahn vs DFS)
- 🌉 MST (Prim/Kruskal) and shortest paths (BFS/0–1/Dijkstra)

## ✅ Study checklist
- [ ] Can I model efficiently (adj list vs matrix)?
- [ ] Do I know which shortest-path flavor fits (BFS, 0–1, Dijkstra)?
- [ ] Can I detect cycles in both directed and undirected graphs?
- [ ] For topo: can I apply both Kahn and DFS+stack?
- [ ] For MST: can I justify Prim vs Kruskal choice?
