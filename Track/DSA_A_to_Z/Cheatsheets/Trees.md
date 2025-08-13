# Trees Cheatsheet (Graph-style trees)

Setup
- Nodes are 1..N; adj[u] holds neighbors; parent, depth via DFS/BFS
- Precompute metadata: parent, depth, subtree size/sum, leaf flags

Binary Lifting
- lift[u][i] = 2^i-th ancestor of u; lift[u][0]=parent[u]
- Build: lift[u][i] = lift[lift[u][i-1]][i-1]
- LCA(u,v): raise deeper node up, then jump both down from high to low bits until parents match; answer is parent

Path queries
- Aggregate over path with lifting (max/min/sum/gcd) by storing aggregates along jumps
- Use prefix-on-tree for sums if applicable (Euler Tour + Fenwick/Segment Tree)

Edge cases
- Rooting choice; 1-based vs 0-based sentinel
- Disconnected input (ensure it’s a tree)

Refs
- Repo Trees README, Binary Lifting notes

---

## At a glance
- Binary lifting: up[v][k] = 2^k-th ancestor. Preprocess in O(n log n); LCA queries O(log n).
- Depth align: Lift deeper node up by depth diff before jumping both.
- Kth ancestor: Jump via bits of k using up table; guard when k exceeds depth.

## Pitfalls
- Root parent: Commonly set up[root][0] = root (or -1) consistently across table to avoid index errors.
- 0/1-based indexing consistency between input and storage.
- Ensure LOG is large enough: ceil(log2(n))+1.

# Trees Cheatsheet (verbatim)

Binary Lifting LCA (from Trees/Binary_Lifting/LCA.py)
```python
from math import log2

# Ref: https://www.youtube.com/watch?v=U3FDz6raLKQ
# https://www.youtube.com/watch?v=oibXaioMRiM
# Spoj: https://www.spoj.com/problems/LCA/

# The first link is the fastest, second is the most comprehensive

class Tree:
    def __init__(self, N, root=1):
        self.N=N
        self.LOGN = int(log2(self.N)) + 1

        # 1 based indexing is used here
        self.root=root
        self.graph = [[] for i in range(N + 1)]
        self.up = [[0] * self.LOGN for i in range(N + 1)]
        self.depth = [0] * (N + 1)

    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def dfs(self, node, parent, d):
        self.depth[node] = d
        self.up[node][0] = parent
        for k in range(1, self.LOGN):
            self.up[node][k] = self.up[self.up[node][k-1]][k-1]

        for child in self.graph[node]:
            if child != parent:
                self.dfs(child, node, d + 1)

    def lca(self, a, b):
        if self.depth[a] < self.depth[b]:
            a, b = b, a

        dist = self.depth[a] - self.depth[b]

        # level up from a
        for k in range(0, self.LOGN):
            if (dist >> k) & 1:
                a = self.up[a][k]

        if a == b: return a

        # now both are on same level
        # try to go above the lca
        for k in range(self.LOGN - 1, -1, -1):
            if self.up[a][k] != self.up[b][k]:
                a = self.up[a][k]
                b = self.up[b][k]

        return self.up[a][0]


if __name__ == '__main__':
    t = Tree(6, 1)
    t.add_edge(1, 2)
    t.add_edge(1, 3)
    t.add_edge(2, 4)
    t.add_edge(2, 5)
    t.add_edge(3, 6)

    # run the dfs once
    t.dfs(1, 1, 0)
    print(t.lca(4, 5)) #2
    print(t.lca(2, 6)) #1
```

Kth Ancestor (from Trees/Binary_Lifting/Kth_Ancestor_of_node.py)
```python
# https://leetcode.com/problems/kth-ancestor-of-a-tree-node/

from math import log2

class TreeAncestor:

    def __init__(self, n, parent):
        LOGN= int(log2(n+1)) + 1

        up = [[-1]*(LOGN) for _ in range(n)]
        depth = [0]*n
        graph = [[] for _ in range(n)]
        for i in range(1,n):
            graph[parent[i]].append(i)

        def dfs(node, par):
            for k in range(1, LOGN):
                up[node][k] = up[up[node][k-1]][k-1]
            for v in graph[node]:
                if v != par:
                    depth[v] = depth[node] + 1
                    up[v][0] = node
                    dfs(v, node)

        up[0][0]=0
        dfs(0,0)
        self.up = up
        self.depth = depth
        self.LOGN = LOGN

    def getKthAncestor(self, node: int, k: int) -> int:
        if k > self.depth[node]:
            return -1
        i=0
        while k>0:
            if (k >> i) & 1:
                node = self.up[node][i]
                k -= (1<<i)
            i += 1
        return node
```

---

## 🗺️ Quick map
- 🌳 Traversals and classic ops
- 🧭 LCA (BST and general), Binary Lifting, K-th ancestor
- 🧷 Depth/parent tables and preprocessing

## ✅ Study checklist
- [ ] Preprocess once (depth/up tables) and reuse
- [ ] Align depths before jumping for LCA
- [ ] Root conventions consistent (parent of root)
