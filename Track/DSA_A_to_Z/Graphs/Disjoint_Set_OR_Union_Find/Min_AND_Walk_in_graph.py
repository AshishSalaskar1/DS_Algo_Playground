"""
Problem: https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/description/?envType=daily-question&envId=2025-03-20


INTUTION:
- You can any path between u and v (even repeat paths) and then min AND of that path weights
- AND properties (roughly stated): 
    a) AND with itself = same number
    b) AND with bigger number will always lead to bigger 
    c) AND with smallest number will cause reduction
    MAIN -> No matter how many bigger or repeated numbers you AND, MIN GETS DECIDED BY SMALLEST OF THE LOT

SOLUTION:
- Use UF to find connected components
- if u and v dont belong to same component => res =- 1
  else, find AND of all the edges in that component ( since you want min, n you can repeat paths any times n surely react u->v)



"""
class UF:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1 for i in range(n)]
    
    def find_par(self, u):
        if self.par[u] == u:
            return u

        self.par[u] = self.find_par(self.par[u])
        return self.par[u]
    
    def add(self, u, v):
        up, vp = self.find_par(u), self.find_par(v)

        if up == vp:    
            return

        if self.size[up] > self.size[vp]:
            self.par[vp] = up
            self.size[up] += self.size[vp]
        else:
            self.par[up] = vp
            self.size[vp] += self.size[up]


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        uf = UF(n)
        comp_edge_and = [float("inf") for i in range(n)]

        for u,v, w in edges:
            uf.add(u,v)
        
        for u,v,w in edges:
            root = uf.find_par(u)
            
            comp_edge_and[root] = (comp_edge_and[root] & w) if comp_edge_and[root] != float("inf") else w 

        
        res = []
        for u,v in query:
            if uf.find_par(u) != uf.find_par(v):
                res.append(-1)
            else:
                res.append(comp_edge_and[uf.find_par(u)])
        
        return res