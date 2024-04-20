
class DSU:
    def __init__(self, V) -> None:
        self.size = [1 for _ in range(V+1)] # 1 based node indexing
        self.parent = [x for x in range(V+1)] # every node is parent is node of itself

    def find_par(self, node):
        # return ultimate parent of u and also do path compression in the process
        if self.parent[node] == node:
            return node

        # path compression -> add each node directly to its parent
        # (this flattens tree to height 2 -> hence UNION_BY_RANK doesnt work with compression)
        self.parent[node] = self.find_par(self.parent[node])
        return self.parent[node]

    def add_edge(self, u, v):
        # find ultimate parents of each
        upu = self.find_par(u)
        upv = self.find_par(v)

        if upu == upv: # already belong to same component
            return
        if self.size[upu] < self.size[upv]: # if size(u) < size(v) -> attach comp(u) to v
            self.parent[upu] = upv
            self.size[upv] += self.size[upu]
        else: # if size(v) < size(u) -> attach component of v to u
            self.parent[upv] = upu
            self.size[upu] += self.size[upv]


edges = [(1,2), (2,3), (4,5), (6,7), (5,6)]

ds = DSU(7)
for u,v in edges:
    ds.add_edge(u,v)

print("PARENTS: ", ds.parent)
print("SIZES: ", ds.size)

# check if they belong to same component
check_pairs = [(1,3), (4,7), (1,7)]
for x,y in check_pairs:
    print(x,y,ds.find_par(x) == ds.find_par(y))
