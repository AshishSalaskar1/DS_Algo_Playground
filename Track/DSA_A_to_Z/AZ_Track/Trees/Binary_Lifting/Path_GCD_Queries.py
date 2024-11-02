import math


def gcd(*nums):
    return math.gcd(*nums)

class Tree:
    def __init__(self, n, node_vals) -> None:
        self.depth = [0]*(n+1)
        self.adj = [[] for _ in range(n+1)]
        self.lift = [[0 for _ in range(29)] for _ in range(n+1)]
        self.dp = [[0 for _ in range(29)] for _ in range(n+1)] # Aggregate from [node, node+(2^i)) EXCLUDING 2^i
        self.val = node_vals
    
    def dfs(self, node, par, depth):
        
        self.depth[node] = depth

        self.lift[node][0] = par
        self.dp[node][0] = self.val[node]

        for i in range(19,-1,-1):
            self.lift[node][i] = self.lift[self.lift[node][i-1]][i-1]
            self.dp[node][i] = gcd(
                self.dp[node][i-1], # FIRST HALF 
                self.dp[self.lift[node][i-1]][i-1] # SECOND HALF
            ) 
        
        for child in self.adj[node]:
            if child!=par:
                self.dfs(child, node, depth+1)
        
    def path_gcd(self, u, v): # u,v are NODE INDEXES
        if self.depth[u] < self.depth[v]:
            u, v = v,u

        ans = 0 # GCD(NOTHING) = 0
        
        # bring to same levels
        lvl_diff = self.depth[u] - self.depth[v]
        for i in range(19,-1,1):
            if lvl_diff & (1<<i):
                u = self.lift[u][i]
                ans = gcd(ans, self.dp[u][i])
        
        # one is ancestor of another
        if u == v:
            return gcd(ans, self.val[u])  # beacuse you excluse 2^i th val while jumping
        
        # shift each by max lvl such that its child of LCA
        for i in range(19,-1,-1):
            if self.lift[u][i] != self.lift[v][i]:
                ans = gcd(ans, self.dp[u][i])
                u = self.lift[u][i]

                ans = gcd(ans, self.dp[v][i])
                v = self.lift[v][i]
        
        # remember you are at LCA.child 
        # YOU HAVENT ADDED vals of LCA, and both both childs (Since dp ignore 2^i th value)
        return gcd(
            ans,
            self.val[u],
            self.val[v],
            self.val[self.lift[u][0]]
        )

#                1  2  3  4   5  6  7  8  9  10
tree_vals = [ 0, 2, 2, 3, 4, 16, 8, 7, 8, 9, 10] # 1-INDEXED
tree_edges = [(1,2),(1,8),(2,3),(2,4),(4,5),(4,6),(4,7),(8,9)]
tree = Tree(10, tree_vals)


for u,v in tree_edges:
    tree.adj[u].append(v)
    tree.adj[v].append(u)

tree.dfs(1,0,1)

print(tree.path_gcd(3,8)) # 1 : 3->2->2->8
print(tree.path_gcd(4,8)) # 4 : 4->2->2->8
print(tree.path_gcd(5,6)) # 8 : 16->8
print(tree.path_gcd(4,6)) # 4 : 4->16->8



        