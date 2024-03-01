"""
Link: https://www.codingninjas.com/studio/problems/matrix-traps_8365440

Problem: Find all islands of 0 which are trapped within edges
- Islands of 0 such that they dont touch the edges

SOLUTION: Same as O, X islands
- Iterate through edge cells and do BFS wherever u see 0 and keep vis track
- Finally iterate through all 0s n check which of these werent covered by outer edge BFS's
"""

from typing import *

def matrixTraps(nr: int, nc: int, arr: List[List[int]]):
    vis = set()
    for i in range(nr):
        for j in range(nc):
            if i==0 or j==0 or i==nr-1 or j==nc-1:
                if arr[i][j] == 0:
                    q = [(i,j)]
                    vis.add((i,j))

                    while len(q) != 0:
                        x1,y1 = q.pop(0)
                        xdelta = [0,1,0,-1]
                        ydelta = [1,0,-1,0]
                        for xd, yd in zip(xdelta, ydelta):
                            x2, y2 = x1+xd, y1+yd
                            if x2>=0 and y2>=0 and x2<nr and y2<nc and arr[x2][y2]==0 and (x2,y2) not in vis:
                                vis.add((x2,y2))
                                q.append((x2,y2))

    
    trap_count = 0
    # print(vis)
    for i in range(nr):
        for j in range(nc):
            if arr[i][j] == 0 and (i,j) not in vis:
                trap_count += 1
    
    return trap_count

# (1, 2), (3, 1), (2, 1), (4, 2), (1, 0), (0, 2), (4, 0)