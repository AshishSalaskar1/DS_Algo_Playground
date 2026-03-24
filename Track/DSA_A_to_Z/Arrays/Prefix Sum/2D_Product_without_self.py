"""

PROBLEM: https://leetcode.com/problems/construct-product-matrix/?envType=daily-question&envId=2026-03-24

-> Flatten array and it becomes ( Find product of array except self)

TRICK:

arr[r][c] = flattened_arr[ (r*nc)+c ]


IMP: There is an inplace 2D version of this which might get bit tricky
https://leetcode.com/problems/construct-product-matrix/submissions/1957985462/?envType=daily-question&envId=2026-03-24
"""

MOD = 12345

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        nr, nc = len(grid), len(grid[0])
        flatarr = [item for row in grid for item in row]
        nfl = len(flatarr)
        lprod, rprod = [0]*nfl, [0]*nfl

        cprod = 1
        for i in range(nfl):
            cprod = (cprod*flatarr[i])%MOD
            lprod[i] = cprod
        
        cprod = 1
        for i in range(nfl-1,-1,-1):
            cprod = (cprod*flatarr[i])%MOD
            rprod[i] = cprod
        
        flatres = []
        for i in range(nfl):
            cur_res = 0
            if i==0: flatres.append(rprod[1])
            elif i == (nfl-1): flatres.append(lprod[-2])
            else: flatres.append((lprod[i-1]*rprod[i+1])%MOD)
        
        res = [[0 for _ in range(nc)] for _ in range(nr) ]
        for r in range(nr):
            for c in range(nc):
                res[r][c] = flatres[(nc * r) + c]
        
        return res

        