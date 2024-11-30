"""
Problem: https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/?envType=daily-question&envId=2024-11-29

PING PONG Djikstras
- Here each cell has value(time) before which you cant leave that cell. You cant wait there also without any movement
[Note]: In some problems you can wait in that cell till you reach that exit time (https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/)

Solution Here: ping pong between this cell and previous one in case you dont meet the time
- You came from (x,y) -> (u,v) but arr[u][v] is greater that time_taken[x][y] + 1
- You are at (u,v) : go back to (x,y) and return => THIS USED 2 seconds of time 
MAIN LOGIC:
- if the difference in time is even -> you can go back and come to this node again 
- if differnce is odd -> you wont be able to be back in odd time, hence you will need to wait 1 more second
Note: Here diff = allow_time = arr[r][c] - time you have reached the node (r,c)
"""
from collections import defaultdict
from queue import PriorityQueue

class Solution:
    def minimumTime(self, arr: List[List[int]]) -> int:
        nr, nc = len(arr), len(arr[0])

        if arr[0][1] > 1 and arr[1][0] > 1:
            return -1

        vis = set()
        pq = PriorityQueue()

        pq.put((0,0,0))
        vis.add((0,0))

        while not pq.empty():
            curtime, row, col = pq.get()
            
            if (row, col) == (nr-1, nc-1):  return curtime
            for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                dr, dc = row+dx, col+dy
                if 0<=dr<nr and 0<=dc<nc and (dr,dc) not in vis:
                    if curtime+1 >= arr[dr][dc]: # you arrived later than needed
                        pq.put((curtime+1, dr, dc))
                    else: # you arrived before you can leave -> ping pong
                        wait = 1 if (arr[dr][dc]-curtime+1) %2 == 1 else 0
                        pq.put((arr[dr][dc]+wait, dr, dc))

                    vis.add((dr,dc))
        return -1

                    