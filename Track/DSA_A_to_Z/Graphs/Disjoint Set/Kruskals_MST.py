from typing import List


"""
Logic: DSU on Sorted weight edges
- DSU -> add_edge -> return True if edge was added, False if not added (u->v was already added and had same super parent)
- Sort edges based on weights and then add_edge for each, if added -> add wt to result
- This way you never add same edge again to a region (you need min edge between 2 edges which you already got since you sorted by weigth)

"""

class DSU:
    def __init__(self, V):
        self.parents = [x for x in range(V+1)]
        self.sizes = [1 for x in range(V+1)]
    
    def get_parent(self, node):
        if self.parents[node] == node:
            return node

        self.parents[node] = self.get_parent(self.parents[node]) #path compression
        return self.parents[node]

    def add_edge(self, u,v):
        up = self.get_parent(u)
        vp = self.get_parent(v)

        if vp == up:
            return False # indicate didnt add it
        elif self.sizes[up] < self.sizes[vp]:
            self.parents[up] = vp
            self.sizes[vp] += self.sizes[up] # vp tree will become bigger now
        else:
            self.parents[vp] = up
            self.sizes[up] += self.sizes[vp]
        
        return True
        

def kruskalMST(n: int, edges: List[List[int]]) -> int:
    # sort acc to weights since you need Minimum Spanning Tree
    edges = sorted(edges, key=lambda x:x[2])

    total_wt = 0
    dsu = DSU(n)

    for u,v,wt in edges:
        if dsu.add_edge(u,v): # this node is already added -> will cause cycle/its already reachable
            total_wt += wt
    
    return total_wt
    