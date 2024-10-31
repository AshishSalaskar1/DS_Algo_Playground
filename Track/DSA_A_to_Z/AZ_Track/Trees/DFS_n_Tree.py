
from collections import deque

class Tree:
    def __init__(self, n) -> None:
        self.adj = [list() for _ in range(n+1)] # DONT DO [list()]*n
        self.par = [0]*(n+1)
        self.val = [0]*(n+1)
        self.depth = [0]*(n+1)
        self.isLeaf = [False]*(n+1)
        self.nChild = [0]*(n+1)
        self.subTreeSum = [0]*(n+1)

    def dfs(self, node, parent, depth):
        self.depth[node] = depth
        self.par[node] = parent

        self.nChild[node] = 0
        self.subTreeSum[node] = 1
        for child in self.adj[node]:
            if child!=parent:
                self.nChild[node] += 1
                self.dfs(child, node, depth+1)
                self.subTreeSum[node] += self.subTreeSum[child]

        if self.nChild[node] == 0:
            self.isLeaf[node] = False

    def bfs(self, root):
        q = deque([(root,0,1)])

        while len(q) != 0:
            node, par, depth = q.popleft()
            self.depth[node] = depth
            self.nChild[node] = 0
            self.par[node] = pare

            for child in self.adj[node]:
                if child != par:
                    self.nChild[node] += 1
                    q.append((child, node, depth+1))

            if self.nChild[node] == 0:
                self.isLeaf[node] = True




tree = Tree(10)
tree_edges = [(1,2),(1,8),(2,3),(2,4),(4,5),(4,6),(4,7),(8,9)]

for u,v in tree_edges:
    tree.adj[u].append(v)
    tree.adj[v].append(u)

tree.dfs(1,0,1)
print(tree.par, tree.depth, tree.isLeaf, sep="\n")


tree.bfs(1)
print(tree.par, tree.depth, tree.isLeaf, sep="\n")
