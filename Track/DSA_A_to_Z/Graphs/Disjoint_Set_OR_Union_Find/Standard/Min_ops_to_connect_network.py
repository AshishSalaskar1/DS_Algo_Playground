"""
Problems:
- You are given edges connecting nodes -> all nodes may not be connected
- You can remove one edge and put in between some other 2 nodes
- MST creation WITH REPLACEMENT

INTUITION:
- If there are I islands you need I-1 edges to connect all these together (will make it a MST)
- But while doing so, you dont want to break the existing components

SOLUTION: DSU
- While adding edge you dont add it if super_parents of both are same,
  This means that particular edge isnt needed -> THATS AN EXTRA EDGE
- Add all nodes to DSU and count the extra ones
- [IMP] Now, at last calculate number of islands (get_parent(i)=i for i in 0->V)
 - WHY CANT U JUST DO set(self.parents)? -> path compression may not have happened for all nodes
 - All nodes in same component might not lead to same parent (component depth>1)
 - Example: [[0,1],[0,2],[3,4],[2,3]]
 
- If islands==1 (only one island, no need to connect) or extra_edges >= (islands-1) return islands-1


"""

class DSU:
    def __init__(self,v):
        self.parents = [x for x in range(v)]
        self.sizes = [1 for _ in range(v)]

    def get_parent(self, node):
        if self.parents[node] == node:
            return node

        self.parents[node] = self.get_parent(self.parents[node])
        return self.parents[node]

    def add_edge(self, u, v):
        up = self.get_parent(u)
        vp = self.get_parent(v)

        if up == vp:
            return True # both are already part of same component - NO NEED OF THIS EDGE
        elif self.sizes[up] < self.sizes[vp]:
            self.parents[up] = vp
            self.sizes[vp] += self.sizes[up]
        else:
            self.parents[vp] = up
            self.sizes[up] += self.sizes[vp]

        return False

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        dsu = DSU(n)  
        extra_edges_available = 0
        for u,v in connections:
            if dsu.add_edge(u,v):
                extra_edges_available += 1
        
        islands = 0
        # check how many islands (need to check since path_compression might not have happened for all nodes)
        for x in range(n):
            if dsu.get_parent(x) == x:
                islands += 1
                
        if islands==1 or extra_edges_available >= islands-1:
            return islands-1 # you need min ISLANDS-1 edges, even if more are available
        else:
            return -1

        