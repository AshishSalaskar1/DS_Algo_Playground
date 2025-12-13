"""

EULERS_PATH:
- A path from `start` to `end` that visits every edge exactly once.
- No conditions on nodes -> you can visit nodes multiple times.

EULERS_CIRCUIT:
- Same logic as EULERS_PATH, but the start and end nodes are the same.

💡 Hamiltonion path/circuit vs Eulers?
- In Homiltonion path/circuit, you visit every NODE exactly once.
- There is no condition on edges.

FLOW:
1. Whether PATH or CIRCUIT -> Check degree conditions
2. If conditions met -> Use Hierholzer's algorithm to print the path/circuit

DIRECTED EULER CIRCUIT:
    - For EVERY vertex: indegree == outdegree
    - All vertices with edges belong to a single strongly connected component
      (weak connectivity is usually enough for Hierholzer usage)

DIRECTED EULER PATH (but NOT circuit):
    - Exactly ONE vertex satisfies: outdegree = indegree + 1   → START node
    - Exactly ONE vertex satisfies: indegree = outdegree + 1   → END node
    - All other vertices: indegree == outdegree
    - Graph must be connected in terms of edges (weakly)

NO EULER PATH:
    - Any vertex has |indegree - outdegree| > 1
    - More than 1 start or more than 1 end node


💡 Why cant you use DFS alone to find Euler Path/Circuit?
- In DFS we visit nodes only once, but in Euler Path/Circuit we can visit nodes multiple times.
- If we allow multiple, cant control loops

💡 DFS -> Heirholzer's Algorithm
- No seen set required
- When you reach a node -> visit all its edges (remove them as you go)
- Backtrack when no edges left

"""

from collections import defaultdict
import copy

class EulersDirected:

    # ------------- Hierholzer DFS -------------
    def heirholzers_dfs(self, u, adj):
        """
        Hierholzer's DFS to find Eulerian path/circuit.
        - While there are unused edges from u:
            - Pick an edge u->v
            - Remove edge u->v from graph
            - Recursively call DFS on v
        - After exploring all edges from u, add u to path
        """
        while adj[u]:
            v = adj[u].pop() # remove edge u->v | Consider you have taken it 
            self.heirholzers_dfs(v, adj)

        # forget abour edges from u-> everything
        self.path.append(u)

    # ------------- EULER CIRCUIT -------------
    def EulersCircuit(self, edges):
        adj = defaultdict(list)
        indeg = defaultdict(int)
        outdeg = defaultdict(int)

        for u, v in edges:
            adj[u].append(v)
            adj[v] # ensure v exists in defaultdict
            outdeg[u] += 1;indeg[v] += 1

        # Circuit condition: indeg == outdeg for all nodes
        for u in adj:
            if indeg[u] != outdeg[u]: return False

        # Pick a start node ( pick anyone )
        start = list(adj.keys())[0]

        # Copy adjacency for Hierholzer
        adj_copy = copy.deepcopy(adj)

        self.path = []
        self.heirholzers_dfs(start, adj_copy, self.path)
        return self.path[::-1]

    # ------------- EULER PATH -------------
    def EulersPath(self, edges):
        adj = defaultdict(list)
        indeg = defaultdict(int)
        outdeg = defaultdict(int)

        # Build adjacency + degrees
        for u, v in edges:
            adj[u].append(v)
            adj[v]               # ensure v exists
            outdeg[u] += 1;indeg[v] += 1

        start = None
        start_nodes = 0
        end_nodes = 0

        # Check Euler path degree conditions
        for u in adj:
            diff = outdeg[u] - indeg[u]
            if diff == 1:
                start = u
                start_nodes += 1
            elif diff == -1: end_nodes += 1
            elif diff != 0: return False

        # Allowed:
        # - 1 start and 1 end (true path)
        # - 0 start (circuit case)
        if not (start_nodes == 1 and end_nodes == 1 or start_nodes == 0):
            return False

        # If circuit-like, choose any start node
        if start is None: start = list(adj.keys())[0]

        # Copy adjacency for safe mutation
        adj_copy = copy.deepcopy(adj)

        self.path = []
        self.heirholzers_dfs(start, adj_copy)
        return self.path[::-1]
    

edges = [ (0, 1),(0, 2),(1, 3),(2, 3)]

ed = EulersDirected()
print("Circuit:", ed.EulersCircuit(edges))
print("Path:   ", ed.EulersPath(edges))