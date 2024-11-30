"""
Problem: https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner

SOLUTION: Simple DJIKSTRAS
- Consider each blocker as 1-sec time penalty -> else 0 second
- In this way you are trying to find shortest path from start to end
"""

from queue import PriorityQueue

class Solution:
    def minimumObstacles(self, arr: List[List[int]]) -> int:
        nr, nc = len(arr), len(arr[0])
        pq = PriorityQueue()

        dist = [[float("inf") for _ in range(nc)] for _ in  range(nr)]

        dist[0][0] = arr[0][0]
        pq.put((arr[0][0], 0, 0))

        while not pq.empty():
            curdist, row, col = pq.get()
            for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                drow, dcol = row+dx, col+dy
                if 0<=drow<nr and 0<=dcol<nc:
                    new_dist = curdist+arr[drow][dcol]
                    if new_dist < dist[drow][dcol]:
                        dist[drow][dcol] = new_dist
                        pq.put((new_dist, drow, dcol))
        
        return dist[nr-1][nc-1] if dist[nr-1][nc-1]!=float('inf') else dist[nr-1][nc-1]

        