"""
https://leetcode.com/problems/multi-source-flood-fill/description/

LOGIC:
- Same as multi source - but in BFS you only visit node only once
- HERE, if you reach same node at same time from other node -> pick the bigger color

HACKY+GREAT SOLUTION:
- Just sort sources by color
- By this you will always start by largest color n first time u visit cells will always be the largest one
- No need to worry about it later

SOLUTION:
- Seen array contains if it was seen, if yes at what time and what color
- While visiting nbrs
    1. Never seen bfore -> continue as usual
    2. If seen, check if time of being seen is same => IF YES update the color in seen
- When you update the arr[r][c] => use the color from seen ( since it might have changed )
"""
# from collections import defaultdict
from queue import deque

class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        nr, nc = n, m
        arr = [[0 for _ in range(nc)] for _ in range(nr)]


        seen = {}
        q = deque()

        for r,c,color in sources:
            q.append((0,r,c,color))
            seen[(r,c)] = [color, 0]
        
        while q:
            time, r,c,color = q.popleft()

            color = seen[(r,c)][0] # COLOR = Latest seen
            arr[r][c] = seen[(r,c)][0]

            for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                nextr, nextc = r+dx, c+dy
                newcords = (nextr,nextc)
                if 0<=nextr<nr and 0<=nextc<nc: # VALID CASE
                    if newcords not in seen: # SEEING FIRST TIME
                        q.append((time+1, nextr, nextc, color))
                        seen[newcords] = [color ,time+1]
                    elif newcords in seen and seen[newcords][1] == (time+1): # seen but replace now
                        seen[newcords][0] = max(seen[newcords][0], color)
        
        return arr
        