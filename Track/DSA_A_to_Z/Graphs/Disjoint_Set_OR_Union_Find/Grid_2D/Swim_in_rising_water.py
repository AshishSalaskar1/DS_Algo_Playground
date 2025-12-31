"""

NOT BEST OPTIMIZED - BFS based, Binary Search based, Union Find approach
Find path from (0,0) -> (nr,nc) such that the max element in that path is minimized
Why is this the answer? You will have to wait till res seconds for water to get filled
SAME AS: https://leetcode.com/problems/path-with-minimum-effort/

Here your dist[i][j] => Path from 0,0 -> i,j having max value in path = dist[i][j] (this is min for all paths from 0,0 -> i,j)
- MinHeap -> (cur_dist, (x2,y2))


ITERATIONS
- We pick the item from queue which we want to minimize (dist in this case, max value from src->dest)
=> pop: cur_dist, (x1,y1)
-> Find all 4 options from (x1,y1)
    1. check if they are valid positions
    2. new_res = max(arr[x2][y2], cur_dist)
        -> update and push if neeed

- we dont maintain any vis array in Djikstras, since we already 
"""

from queue import PriorityQueue
class Solution:
    def swimInWater(self, arr: List[List[int]]) -> int:
        pq = PriorityQueue()
        nr, nc = len(arr), len(arr[0])
        dist = [[float("inf") for _ in range(nc)] for _ in range(nr)]

        dist[0][0] = arr[0][0] # you need atleast arr[0][0] to start swimming
        pq.put((arr[0][0],(0,0))) # max of path = arr[0][0]

        while pq.qsize() != 0:
            cur_res, (x1,y1) = pq.get()
            for dx,dy in zip([0,1,-1,0],[1,0,0,-1]): # check all 4 directions
                x2, y2 = x1+dx, y1+dy
                if x2<nr and y2<nc and x2>=0 and y2>=0:
                    new_res = max(cur_res, arr[x2][y2])
                    if dist[x1][y1] != float("inf") and new_res < dist[x2][y2]:
                        dist[x2][y2] = new_res
                        pq.put((new_res, (x2,y2)))

        
        return dist[-1][-1]

        