"""
PROBLEM: Nearest Exit from Entrance in Maze
https://leetcode.com/problems/nearest-exit-from-entrance-in-maze


SOLUTION: Simple BFS
- BFS ensures you visit gradually outwards from src
- You escape if in case these conditions are true
        1) arr(x,y) = "." 
        2) x=0 or nr-1 or y=1 or y=nc-1 [first row, last row, first col, last col <- any of these]

"""

from collections import deque
class Solution:
    def nearestExit(self, arr: List[List[str]], entrance: List[int]) -> int:
        nr, nc = len(arr), len(arr[0])
        # print(arr[2][2])

        q=deque([(entrance[0],entrance[1],0)])
        vis = set([(entrance[0],entrance[1])])

        while len(q) != 0:
            ux,uy,steps = q.popleft()

            dxs = [0,1,0,-1]
            dys = [1,0,-1,0]
            
            for dx,dy in zip(dxs,dys):
                vx,vy = ux+dx, uy+dy
                if vx>=0 and vy>=0 and vx<nr and vy<nc and arr[vx][vy] == "." and (vx,vy) not in vis:
                    if vx == nr-1 or vy==nc-1 or vx==0 or vy==0: # reached escape
                        return steps+1
                    q.append((vx,vy,steps+1))
                    vis.add((vx,vy))
                    
        
        return -1
            
             


"""
["+","+",".","+"],
[".",".",".","+"],
["+","+","+","."]
"""