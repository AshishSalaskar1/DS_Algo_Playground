
from collections import deque

class Tree:
    def __init__(self, n) -> None:
        self.adj = [list() for _ in range(n+1)] # DONT DO [list()]*n
        self.lift = [[0 for _ in range(20)] for _ in range(n+1)]
        self.val = [0]*(n+1)
        self.depth = [0]*(n+1)

    def dfs(self, node, parent, depth):
        self.depth[node] = depth
        self.lift[node][0] = parent

        # lift from 1->19 : 2^0 -> 2^19 (2^19 is approx equal to 10^6)
        for i in range(1,20): # VVVVVVIMP (1->20)
            self.lift[node][i] = self.lift[self.lift[node][i-1]][i-1]

        for child in self.adj[node]:
            if child!=parent:
                self.dfs(child, node, depth+1)

    def lca(self, u, v):
        print(u,v)
        # make sure depth of u>v =>
        if self.depth[u]<self.depth[v]: u,v= v,u
        print(u,v)

        # bring both nodes to same level/depth = Lift U (since its longer)
        diff_depth = self.depth[u] - self.depth[v]
        for i in range(19,-1,-1):
            # check if ith bit is set in diff_depth
            if diff_depth & (1<<i):
                u = self.lift[u][i] # lift by i, i=bit set

        print("AFTER LEVEL",u,v)
        # in case after reducing level you see both co-incide
        if u==v:    return u

        # lift both by 2^19->2^0 and stop when u!=v
        for i in range(19,-1,-1):
            # if both vals are same, means this loc is before the LCA
            if self.lift[u][i] != self.lift[v][i]:
                u = self.lift[u][i]
                v = self.lift[v][i]

        print("FINAL child of LCA",u,v)
        # now both u,v will be one node below the LCA (at LCA lift[u]==lift[v], so you will be one level below that )
        return self.lift[u][0] # lift(u,0) = parent(u)


tree = Tree(10)
tree_edges = [(1,2),(1,8),(2,3),(2,4),(4,5),(4,6),(4,7),(8,9)]

for u,v in tree_edges:
    tree.adj[u].append(v)
    tree.adj[v].append(u)

tree.dfs(1,0,1)


print(tree.lca(3,7)) # 2
print(tree.lca(3,9)) # 1
print(tree.lca(3,4)) # 2
print(tree.lca(5,9)) # 1
