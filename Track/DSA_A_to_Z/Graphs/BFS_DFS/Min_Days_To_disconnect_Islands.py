"""
Problem: https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/

Solution: https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/solutions/5618297/beginner-friendly-solution-with-brute-force-dfs-visualization-step-explanation/
"""

from typing import List

class DFS:
    @staticmethod
    def run(i, j, arr, vis):
        if i>=0 and j>=0 and i<len(arr) and j<len(arr[0]) and arr[i][j] == 1 and (i,j) not in vis:
            vis.add((i,j))
            deltas = [(i+1, j), (i,j+1), (i,j-1), (i-1,j)]
            for r,c in deltas:
                DFS.run(r, c, arr, vis)

    @staticmethod
    def check_num_islands(arr) -> int:
        nr, nc = len(arr), len(arr[0])
        nislands = 0
        vis = set()
        for i in range(nr):
            for j in range(nc):
                if arr[i][j] == 1 and (i,j) not in vis:
                    nislands += 1
                    DFS.run(i,j,arr,vis)

        return nislands


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        nr, nc = len(grid), len(grid[0])
        vis = set()

        # Check initial number of islands
        nislands = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == 1 and (i,j) not in vis:
                    nislands += 1
                    DFS.run(i,j,grid,vis)

        # print(nislands)
        if nislands == 0 or nislands>1:
            return 0

        vis = set()
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    nislands = DFS.check_num_islands(grid)
                    if nislands == 0 or nislands>1:
                        return 1
                    grid[i][j] = 1


        return 2