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

EULERS_PATH:
- A path from `start` to `end` that visits every edge exactly once.
- No conditions on nodes -> you can visit nodes multiple times.

EULERS_CIRCUIT:
- Same logic as EULERS_PATH, but the start and end nodes are the same.

FLOW:
1. Whether PATH or CIRCUIT -> Check degree conditions
2. If conditions met -> Use Hierholzer's algorithm to print the path/circuit


UNDIRECTED EULER CIRCUIT:
    - Every vertex has EVEN degree
    - Graph is connected (ignoring isolated vertices)

UNDIRECTED EULER PATH (but NOT circuit):
    - Exactly TWO vertices have ODD degree
    - All other vertices have EVEN degree
    - Graph is connected (ignoring isolated vertices)

NOTHING EXISTS:
    - More than 2 odd-degree vertices → NO Euler path or circuit

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

class EulersUndirected:

    # ------------- Hierholzer DFS for UNDIRECTED -------------
    def heirholzers_dfs(self, u, adj):
        """
        For undirected Euler:
        - When you take edge u--v, you must remove BOTH:
              adj[u].remove(v)
              adj[v].remove(u)
        """
        while adj[u]:
            v = adj[u].pop()        # take edge u--v
            adj[v].remove(u)        # remove reverse edge
            self.heirholzers_dfs(v, adj)
        self.path.append(u)

    # ------------- EULER CIRCUIT -------------
    def EulersCircuit(self, edges):
        adj = defaultdict(list)
        degree = defaultdict(int)

        # Build adj + degree
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1

        # Circuit condition: ALL vertices must have even degree
        for u in degree:
            if degree[u] % 2 != 0:
                return False

        # Pick any starting node
        start = list(adj.keys())[0]

        # Deep copy adjacency (because Hierholzer deletes edges)
        adj_copy = copy.deepcopy(adj)

        self.path = []
        self.heirholzers_dfs(start, adj_copy)
        return self.path[::-1]

    # ------------- EULER PATH -------------
    def EulersPath(self, edges):
        adj = defaultdict(list)
        degree = defaultdict(int)

        # Build adj + degree
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1

        odd = [u for u in degree if degree[u] % 2 == 1]

        # Euler path requires exactly 0 or 2 odd vertices
        if len(odd) not in (0, 2):
            return False

        # Start node:
        # - If 2 odd nodes: start at one of them
        # - If 0 odd nodes: start anywhere
        start = odd[0] if len(odd) == 2 else list(adj.keys())[0]

        adj_copy = copy.deepcopy(adj)

        self.path = []
        self.heirholzers_dfs(start, adj_copy)
        return self.path[::-1]
