"""
Problem: https://leetcode.com/problems/shortest-bridge/

Solution: MultiSource BFS
1. Find first arr[i][j] = 1 -> DFS(i,j) and visit all nodes of ISLAND_1 and put them in Q
2. BFS -> From any node in ISLAND_1 to nearest node of ISLAND_2
    - How to check if you reached ISLAND_2? if cur_node=0 and next_node=1
    - if next_node = 1 => while adding to Q the dist = dist (dont need bridges to connect 1s)
    - if next_node = 0 => while adding to Q the dist = dist+1 (need one bridge to flip 0-1)

References
Multi Source BFS
- https://leetcode.com/problems/walls-and-gates/ (https://leetcode.ca/all/286.html)
- https://leetcode.com/problems/as-far-from-land-as-possible/
- https://leetcode.com/problems/map-of-highest-peak/
- https://leetcode.com/problems/rotting-oranges/
"""
from collections import deque

class Solution:
    def shortestBridge(self, grid) -> int:
        # FIRST DFS -> put all nodes of island 1 in QUEUE for multisource DFS
        def dfs(i, j):
            q.append((i, j, 0))
            vis.add((i, j))

            for deltax, deltay in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                newx, newy = i + deltax, j + deltay

                if 0 <= newx < nr and 0 <= newy < nc and (newx, newy) not in vis and grid[newx][newy] == 1:
                    vis.add((newx, newy))
                    dfs(newx, newy)

        n = len(grid)
        nr, nc = len(grid), len(grid[0])
        vis = set()
        q = deque()

        first_seen = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    first_seen = True
                    dfs(i, j)
                    break
            if first_seen:
                break

        # Second BFS -> min distance from any node on ISLAND 1 -> to nearest node in ISLAND 2
        while len(q) > 0:
            x, y, dist = q.popleft()
            # vis.add((newx, newy))

            for deltax, deltay in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                newx, newy = x + deltax, y + deltay

                if 0 <= newx < nr and 0 <= newy < nc and (newx, newy) not in vis:
                    vis.add((newx, newy)) # THIS NEEDS TO BE HERE
                    if grid[newx][newy] == 1:
                        return dist
                    else:
                        q.append((newx, newy, dist + 1))

        return -1