"""
Last Day Where You Can Still Cross
https://leetcode.com/problems/last-day-where-you-can-still-cross/?envType=daily-question&envId=2025-12-31


ASK:
- What is the last day where you can cross ( TOP and BOTTOM are connected)

FLIP LOGIC:
- Initially consider all cells are water
- Iterate from end to start
    - each cell is then land addition
    - Whenever you see that TOP and BOTTOM are connected -> ANS

DUMMY NODES:
-1: TOP ROW
-2: BOTTOM ROW

"""
class UF:
    def __init__(self):
        self.par = {-1:-1, -2:-2}
        self.size = {-1:1, -2: 1}
    
    def findpar(self, node: int) -> str:
        if node == self.par[node]:
            return node
        
        self.par[node] = self.findpar(self.par[node])
        return self.par[node]
    
    def union(self, u: int, v: int) -> None:
        for node in [u,v]:
            if node not in self.par:
                self.par[node] = node
                self.size[node] = 1

        up, vp = self.findpar(u), self.findpar(v)

        if up == vp: return

        if self.size[up] > self.size[vp]:
            self.par[vp] = up
            self.size[up] += self.size[vp]
        else:
            self.par[up] = vp
            self.size[vp] += self.size[up]

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        uf = UF()
        nr, nc = row, col

        landcells = set()

        def getidx(r: int, c: int):
            return (r*nc) + c
        
        for day in range(len(cells)-1,-1,-1):
            r,c = cells[day]

            r-=1;c-=1 # cells are 1 indexed
            landcells.add((r,c)) 

            if r == 0: # TOP ROW - START = -1
                uf.union(getidx(r,c), -1) 
            elif r == nr-1: # BOTTOM ROW - end = -2
                uf.union(getidx(r,c), -2) 

            # connect it to all its neighbor land cells
            for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                newr, newc = r+dr, c+dc
                if 0<=newr<nr and 0<=newc<nc and (newr,newc) in landcells:
                    uf.union(getidx(r,c), getidx(newr, newc))
            
            # check if top and bottom are connected
            if uf.findpar(-1) == uf.findpar(-2):
                return day
        
        return -1



        