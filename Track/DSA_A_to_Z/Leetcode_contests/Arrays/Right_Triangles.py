"""
Problem: https://leetcode.com/problems/right-triangles/description/
You are given a 2D boolean matrix grid.

Return an integer that is the number of right triangles that can be made with the 3 elements of grid such that all of them have a value of 1.

Note: [Right angle doesnt mean 3 in all diections - NOT EVEN USING MODULO]
A collection of 3 elements of grid is a right triangle if one of its elements is in the same row with another element and in the same column with the third element. The 3 elements do not have to be next to each other.


LOGIC:
1. Keep a count of ones in each row and col -> precompute row and col counts for 1
2. Iterate through i,j for all cells
   num_right_sides which include arr[i][j] = (row_map[i]-1 ) * (col_map[j]-1)
   - Why -1 on both? both maps give you count of ones BUT curr element arr[i][j] is also 1 (so you remove that from both)
"""

class Solution:
    def numberOfRightTriangles(self, arr: List[List[int]]) -> int:
        nr, nc = len(arr), len(arr[0])
        rmap, cmap = {}, {}
        
        for i in range(nr):
            for j in range(nc):
                if arr[i][j] == 1:
                    rmap[i] = rmap.get(i,0)+1
                    cmap[j] = cmap.get(j,0)+1
        
        print(rmap, cmap)
                
        res = 0
        for i in range(nr):
            for j in range(nc):
                if arr[i][j] == 1:
                    rows = rmap[i]-1
                    cols = cmap[j]-1
                    if rows*cols >= 1:
                        res += rows*cols
                    
     
        return res
                                
                         
"""
[0,0],
[0,1],
[1,1]


{0: 2, 1: 1, 2: 1} ROWS
{0: 3, 2: 1}       COLS
2? not 1?
"""
                    