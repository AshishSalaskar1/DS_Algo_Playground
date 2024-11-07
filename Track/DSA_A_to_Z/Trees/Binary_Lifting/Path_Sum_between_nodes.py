"""
PROBLEM:
- You are given a n-ary tree, and Queries of form (u,v)
- You need to return the path sum from u -> v (there exists only one path since its a tree not a graph)





EXAMPLE:
           3(1)
          /   \
         4(2)  5(3)
       /   \     \
      1(4)  3(5)  1(6)

# prefix[node] = prefix sum from root(1) to current node

- U,V are nodes
- LCA is LCA(u,v)

path_sum = prefix[u] + prefix[v] - 2*prefix[lca] + val[lca]
- Why - 2*prefix[lca]? If you see the path root->LCA was considered in each of the two prefix sums (prefix[node] = sum(root->node))
- But, we need to include the value where they meet (LCA) also once (in previous step you deleted both)
  So, + val[lca]

Example path:
4,5 => 1->4->3 = 8

lca = 2, prefix[2] = 7
prefix[4] +  prefix[4] = 18 - 2*prefix[lca] = 18 - 2*prefix[2] = 18-14 = 4 + val[2] = 8
2 - 7
          0  1  2  3  4   5  6 
prefix = [0, 3, 7, 8, 8, 10, 9]
"""




class Tree:
    def __init__(self, n, arr) -> None:
        self.val = arr
        self.adj = [[] for _ in range(n+1)]
        self.lift = [[0 for _ in range(20)] for _ in range(n+1)]
        self.depth = [0 for _ in range(n+1)]
        # prefix[node] = prefix sum from root(1) to current node
        self.prefix = [0 for _ in range(n+1)]

    def dfs(self, node, par, depth, psum):
        self.depth[node] = depth
        self.lift[node][0] = par
        self.prefix[node] = psum + self.val[node]

        # calculate lifts
        for i in range(1,20):
            self.lift[node][i] = self.lift[self.lift[node][i-1]][i-1]

        for ch in self.adj[node]:
            if ch != par:
                self.dfs(ch, node, depth+1, self.prefix[node])
    
    def lca(self, u, v):
        # make sure u is deeper
        if self.depth[u] < self.depth[v]:
            u,v = v,u

        # bring both to same level
        lvl_diff = self.depth[u] - self.depth[v]
        for i in range(19,-1,-1):
            if lvl_diff & (1<<i):
                u = self.lift[u][i]
                v = self.lift[v][i]
        
        if u == v:  return u

        # get highest lvl jst below LCA
        for i in range(19, -1, -1):
            if self.lift[u][i] != self.lift[v][i]:
                u = self.lift[u][i]
                v = self.lift[v][i]

        return self.lift[u][0] # parent(u,v) = LCA
    
    def path_sum(self, u, v):
        lca = self.lca(u, v)
        print(u,v, lca)

        return self.prefix[u]+self.prefix[v] - (2*self.prefix[lca]) + self.val[lca]



arr = [-1, 3, 4, 5, 1, 3, 1]
edges = [(1,2),(1,3),(2,4),(2,5),(3,6)]

tree = Tree(10, arr)

for u,v in edges:
    tree.adj[u].append(v)
    tree.adj[v].append(u)


tree.dfs(1,0,1,0)
print(tree.prefix)

print(tree.path_sum(4,6)) # 14
print(tree.path_sum(4,5)) # 8