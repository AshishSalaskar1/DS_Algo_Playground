"""
PROBLEM:https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/

SOLUTION: 
- Sample cases in which it can block: https://imgur.com/a/jXg6Y7i
- Intersection formaula: https://imgur.com/a/two-circles-intersect-conicide-ZX7mo8X
- My Solution: https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/solutions/5548616/union-find-solution-check-for-blocking-conditions/

"""

class UF:
    def __init__(self, n) -> None:
        self.par = [i for i in range(n)]
        self.size = [1 for i in range(n)]
    
    def find_parent(self, node: int) -> int:
        if self.par[node] == node:
            return node
        
        self.par[node] = self.find_parent(self.par[node])
        return self.par[node]

    def union(self, u:int, v: int) -> None:
        upar, vpar = self.find_parent(u), self.find_parent(v)
        if upar == vpar:
            return 

        if self.size[vpar] < self.size[upar]: # add upar in vpar
            self.par[upar] = vpar
            self.size[vpar] += self.size[upar]
        else: # add vpar into upar
            self.par[vpar] = upar
            self.size[upar] += self.size[vpar]

class Solution:
    def canReachCorner(self, xr: int, yr: int, circles: List[List[int]]) -> bool:
        bounds = {
            "left": 0,
            "right": 1,
            "top": 2,
            "bottom": 3
        }

        n = len(circles)
        uf = UF(n+4)

        for i, circle in enumerate(circles):
            x, y, r = circle[0], circle[1], circle[2]

            if r>= max(xr, yr):# radius of circle > Rectangle
                return False
            if x-r <= 0: # intersects Left boundary
                uf.union(i, n+bounds["left"])
            if y-r <= 0: # intersects bottom boundary
                uf.union(i, n+bounds["bottom"])
            if x+r >= xr: # intersects right boundary
                uf.union(i, n+bounds["right"])
            if y+r >= yr: # intersects top boundary
                uf.union(i, n+bounds["top"])
            
            for j in range(i): # check if circle intersects with any other circles seen till now
                x2,y2,r2 = circles[j][0], circles[j][1], circles[j][2]
                if (x-x2)**2 + (y-y2)**2 <= (r+r2)**2: # check if the circles coincide
                    uf.union(i,j)
        
        # check if any of the connections block our WAY
        if uf.find_parent(n+bounds["left"]) == uf.find_parent(n+bounds["right"]) \
            or uf.find_parent(n+bounds["top"]) == uf.find_parent(n+bounds["bottom"]) \
            or uf.find_parent(n+bounds["left"]) == uf.find_parent(n+bounds["bottom"]) \
            or uf.find_parent(n+bounds["top"]) == uf.find_parent(n+bounds["right"]):
            return False

        return True
        