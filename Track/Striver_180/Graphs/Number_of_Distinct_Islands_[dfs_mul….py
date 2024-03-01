"""
https://www.geeksforgeeks.org/problems/find-the-number-of-islands/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=find_the_number_of_islands

Given a grid of size n*m (n is the number of rows and m is the number of columns in the grid) consisting of '0's (Water) and '1's(Land). Find the number of islands.
Note: An island is either surrounded by water or boundary of grid and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.

1.
Input: grid = {{0,1},{1,0},{1,1},{1,0}}
Output: 1

2: 
Input: grid = {{0,1,1,1,0,0,0},{0,0,1,1,0,1,0}}
Output: 2


ALGO
- Consider each cell as one node in graph (i,j) is one node, u have nr*nc nodes
- In logic to find nbrs you check all 8 directions of the current node here
- No need to VIS array since we are replacing 1 -> 0 whenever we visit that particular node.
  This also works because before making it 0, we already add i,j to Q, so that doesnt need to be 1
  
 - If you didnt replace 1->0 after each visit, you need to maintain a visited tracker

"""

class Solution:
    def get_nbrs(self, i, j):
        nbrs = []
        
        paths = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
        for x_add,y_add in paths:
            x = i+x_add
            y = j+y_add
            
            
            if x>=self.nr or x<0:
                continue
            
            if y>=self.nc or y<0:
                continue
            
            if self.grid[x][y] == 1:
                nbrs.append((x,y))
        
        return nbrs
        
        
    def do_bfs(self, i, j):
        q=[(i,j)]
        # self.vis.add((i,j))
        self.grid[i][j] = 0
        
        while len(q) != 0:
            x1,y1 = q.pop(0)
            # find all nbrs of node as x,y
            for x2,y2 in self.get_nbrs(x1,y1):
                # if (x2,y2) not in self.vis:
                    q.append((x2,y2))
                    self.grid[x2][y2] = 0
                    # self.vis.add((x2,y2))
                    
        
    def numIslands(self,grid):
        self.vis = set()
        self.grid = grid
        self.nr = len(grid)
        self.nc = len(grid[0])
        islands = 0
        
        for i in range(self.nr):
            for j in range(self.nc):
                if self.grid[i][j] == 1:
                    islands += 1
                    self.do_bfs(i,j)
                    # print(i,j)
                    # print(self.grid)
        
        return islands