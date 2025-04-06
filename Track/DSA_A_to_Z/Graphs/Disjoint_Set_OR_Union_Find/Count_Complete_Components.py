"""
Problem: Count the Number of Complete Components
Link: https://leetcode.com/problems/count-the-number-of-complete-components

SOLUTION:
1. Use UF/BFS/DFS to find all the components
2. A connected component is complete if and only if the number of edges in the component is equal to m*(m-1)/2, where m is the number of nodes in the component.
3. So you need these things
    a) Components grouped together
    b) No of nodes in each component
    c) count of edges in each component

-> Using UF you already get (a) and (b). 
For (c) we maintain it separately. We do this after the UF is made
"""

from collections import defaultdict
class UF:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def find_parent(self, u):
        if self.par[u] == u:
            return u
        
        self.par[u] = self.find_parent(self.par[u])
        return self.par[u]

    def add(self, u, v):
        up, vp = self.find_parent(u), self.find_parent(v)

        if up == vp:
            return 
        
        if self.size[up] > self.size[vp]:
            self.par[up] = vp
            self.size[vp] += self.size[up]
        else:
            self.par[vp] = up
            self.size[up] += self.size[vp]
        

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)
        comp_edge_count = defaultdict(int)

        for i,j in edges:
            uf.add(i,j)
        
        for u,v in edges:
            root = uf.find_parent(u)
            comp_edge_count[root] += 1

        res = 0
        for node in range(n):
            uf.find_parent(node) # just for path compression

            if node == uf.par[node]:
                node_count = uf.size[node]
                needed_edges = (node_count * (node_count-1)) // 2


                if comp_edge_count[node] == needed_edges:
                    res += 1
        
        return res




        


        
        