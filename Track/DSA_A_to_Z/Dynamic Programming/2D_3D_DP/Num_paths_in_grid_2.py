"""
Given a grid of size n*m, you need to find the total number of different paths from (1, 1) to (n, m). 
You are allowed to move from (x, y) to (x+1, y) and (x, y) to (x, y+1). 

The grid may have some blocked cells, represented by 1, and it is not allowed to move to a blocked cell. 
An empty cell is represented by 0. 

You are also given an integer k and you can convert at most k blocked cells into unblocked cells.

0 -> unblocked
1 -> blocked
"""


class Solution:

    def solve(self, i, j, k):
        if i>=self.nr or j>=self.nc:
            return 0
        
        if i==self.nr-1 and j==self.nc-1:
            return 1
        

        if self.arr[i][j] == 0:
            return self.solve(i+1,j,k)+self.solve(i,j+1,k)
        elif self.arr[i][j] == 1 and k>0:
            return self.solve(i+1,j,k-1)+self.solve(i,j+1,k-1)

        return 0

    def num_grid_paths(self, arr, k):
        self.arr = arr
        self.nr, self.nc = len(arr), len(arr[0])

        return self.solve(0,0,k)
 

sol = Solution()


arr = [
    [0, 1, 1],
    [1, 1, 0],
    [1, 0, 0]
]
k = 2 # 6
print(sol.num_grid_paths(arr, k))

arr = [
    [0, 1, 1],
    [1, 1, 0],
    [1, 0, 0]
]
k = 1 # 0
print(sol.num_grid_paths(arr, k))


arr = [
    [1, 0, 0],
    [0, 1, 0]
]

k = 0 #  0
print(sol.num_grid_paths(arr, k))
