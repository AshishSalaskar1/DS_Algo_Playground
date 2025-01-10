"""
Problem: https://leetcode.com/problems/as-far-from-land-as-possible/description/

Solution: Multisource BFS

-> Find shortest distance from each 0(water) to any 1(land) -> and then take max of this shortest distance
"""

from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        nr, nc = len(grid), len(grid[0])
        dist = [[-1 for _ in range(nc)] for _ in range(nr)]
        q = deque()
        vis = set()

        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == 1:
                    q.append((i,j, (i,j)))
                    vis.add((i,j, (i,j)))
        
        max_res = -1
        while len(q) > 0:
            i,j, org_src = q.popleft()
            if grid[i][j] == 0:
                dist[i][j] = max(dist[i][j], abs(i-org_src[0])+abs(j-org_src[1]))
                max_res = max(max_res, dist[i][j])

            for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                x,y = i+dx, j+dy
                if 0<=x<nr and 0<=y<nc and (x,y) not in vis:
                    vis.add((x,y))
                    q.append((x,y,org_src))
        
        # print(*dist, sep="\n")
        return max_res

        