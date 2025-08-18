"""
PROBLEM: 
Given a boolean 2D matrix grid of size N x M. Find the number of distinct islands where a group of connected 1s (horizontally or vertically) forms an island. 
Two islands are considered to be same if and only if one island is equal to another (not rotated or reflected).


EXAMPLE
[
    [1, 1, 0, <1, 1>], 
    [1, 0, 0, 0, 0], 
    [0, 0, 0, 0, 1],
    [<1, 1>, 0, 1, 1]
]
- Here we have 3 distinct islands
    1. Top left with 3 1s
    2. Bottom right with 3 1s
    3. <1,1> 
- The (3) are considered same, but the (1),(2) are different since same vals but shapes are different

HOW TO REPRESENT EACH island
- You need relative directions/path
- SET( (base_row-row), (base_col-col), ... )
- Here base cells are one where you started from, ideally all others become RELATIVE POSITION FROM BASE

"""
class Solution:
    def dfs(self, r, c, base_r, base_c):
        if r<0 or c<0 or r>=self.nr or c>=self.nc or self.arr[r][c] == 0 or (r,c) in self.vis:
            return

        self.vis.add((r,c))
        self.curpath.add((base_r-r, base_c-c))

        for x,y in zip(
            [0,1,0,-1],
            [1,0,-1,0]
        ):  
            r2, c2 = r+x, c+y
            self.dfs(r2,c2,base_r, base_c)
            self.vis.add((r,c))



    def countDistinctIslands(self, arr):
        self.arr = arr
        self.nr, self.nc = len(arr), len(arr[0])
        self.vis = set()
        self.islands = set()

        for i in range(self.nr):
            for j in range(self.nc):
                if self.arr[i][j] == 1 and (i,j) not in self.vis:
                    self.curpath = set()
                    self.dfs(i,j,i,j)
                    self.islands.add(frozenset(self.curpath))
        
        return len(self.islands)


      