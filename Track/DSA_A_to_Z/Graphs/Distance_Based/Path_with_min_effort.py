"""
PBLM: https://leetcode.com/problems/path-with-minimum-effort/description/

SOLUTION: Dikstras + MAX_ABS_DIST instead of distance
PQ Entry: (max_abs_distance(src,u), (ux,uy)) - max abs distance from src to ux,uy

WHILE PQ is not empty
-> u_max_abs_diff, (ux,uy) <- popped from Queue
-> For ux,uy you can mode 4 directions -> pick valid ones
-> Valid node -> (ux,uy) -> (vx,vy) found
    1. new_abs_diff = ABS Difference between U,V = |arr[ux][uy]-arr[vx][vy]|
    2. MAX ABS DIFF from src -> U was u_max_abs_diff,
       Now from src -> V it becomes max(u_max_abs_diff, new_abs_diff)

"""

from queue import PriorityQueue

class Solution:
    
    def minimumEffortPath(self, arr: List[List[int]]) -> int:
        pq = PriorityQueue()
        nr, nc = len(arr), len(arr[0])

        dist = [[float("inf") for _ in range(nc)] for _ in range(nr)]
        dist[0][0] = 0 # ABS src-src = 0
        pq.put((0, (0,0)))

        while pq.qsize() != 0:
            u_max_abs_diff, (ux,uy) = pq.get()

            dxs = [1,0,-1,0]
            dys = [0,1,0,-1]

            for dx,dy in zip(dxs,dys): # UP, DOWN, LEFT, RIGHT
                vx = ux + dx
                vy = uy + dy

                if vx<nr and vy<nc and vx>=0 and vy>=0: # valid moves 
                    new_abs_diff = abs(arr[ux][uy]-arr[vx][vy]) # abs diff between U,V
                    new_max_abs_dist = max(new_abs_diff, u_max_abs_diff) # new MAX ABSOLUTE DISTANCE
                    if new_max_abs_dist < dist[vx][vy]:
                        dist[vx][vy] = new_max_abs_dist
                        pq.put((new_max_abs_dist, (vx,vy)))
        
        return dist[nr-1][nc-1]



        