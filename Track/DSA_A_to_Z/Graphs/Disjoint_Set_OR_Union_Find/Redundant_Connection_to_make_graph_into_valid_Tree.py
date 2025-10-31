class UF:
    def __init__(self):
        self.parent = {}
        self.components = 0
        self.size = {}
    
    def find_parent(self, node):
        if node == self.parent[node]:
            return node

        self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        for node in [u,v]:
            if node not in self.parent:
                self.parent[node] = node
                self.size[node] = 1
                self.components += 1
        
        up, vp  = self.find_parent(u), self.find_parent(v)
        if up == vp:
            return False
        
        self.components -= 1

        if self.size[up] < self.size[up]:
            self.parent[up] = uv
            self.size[vp] += self.size[up]
        else:
            self.parent[vp] = up
            self.size[up] += self.size[vp]
        
        return True
  
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UF()

        for u,v in edges:
            if not uf.union(u,v):
                return [u,v]
        
        return -1
        