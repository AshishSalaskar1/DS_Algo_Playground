"""
Problem: https://leetcode.com/problems/trapping-rain-water-ii/?envType=daily-question&envId=2025-01-19
- 3D Rain water trapping

Solution: https://leetcode.com/problems/trapping-rain-water-ii/solutions/1138028/python3-visualization-bfs-solution-with-explanation

Algorithms: Multi Source BFS + PQ (modified Djikstras kind of approach)

-> Reverse thinking: Start thinking from boundaries (which can never contain any water)
cur_max_height_seen = 0 (Consider this as level in BFS)
1. Initially visit all boundary nodes (they can never hold any water)
2. Pop cells in PQ having smallest size 
    - iterate their nbrs
        1. if height[nbr] > cur_max_height_seen: 
            - This nbr is greater than current cell
            - So this cant store any water, this acts like a new Boundary -> add to PQ as a boundary
        2. if height[nbr] < cur_max_height_seen: 
            - add their diff directly to the res 
        - Why do you add it now first time when it was seen? [IMPORTANT]
            - Think of it, the max water that can be enclosed is min(nbr heights)-cur_ht ( this is assuming cur_ht is smaller)
            - So since you used pq, the node from where you reached cur_node will have the smallest hieght amongst all its neighbors
        - Why diff with cur_max_height_seen and not prev_parent_node?
            - This is similar to finding the NEXT GREATER ELEMENT
            - Consider your cur_h=4, and the nbr_ht=6 (nbr you can from first). Now diff here is 2 
            - BUT, there can be another neighbor of nbr_ht, which is greater than 6 
            - ( 1,2,3,4 -> here if you are 1, you pick 4 and not 2 which is its immediate neigbor)
        - Why not use max_heap here then? Since you want to maximise diff b/w curr cell and the tallest boundary?
"""

from queue import PriorityQueue

class Solution:
    def trapRainWater(self, arr: List[List[int]]) -> int:
        nr, nc = len(arr), len(arr[0])
        pq = PriorityQueue()
        vis = set()
        
        res = 0
        for r in range(nr):        
            for c in range(nc):
                if r==0 or r==nr-1 or c==0 or c==nc-1:
                    pq.put((arr[r][c],r,c))
                    vis.add((r,c))
        
        
        cur_max_height_seen, res = 0,0
        while pq.qsize()>0:

            cur_h, r, c = pq.get()
            cur_max_height_seen = max(cur_max_height_seen, cur_h)

            for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                nextr, nextc = r+dx, c+dy
                if 0<=nextr<nr and 0<=nextc<nc and (nextr, nextc) not in vis:
                    vis.add((nextr, nextc))
                    pq.put((arr[nextr][nextc],nextr,nextc))

                    if arr[nextr][nextc] < cur_max_height_seen:
                        res += (cur_max_height_seen-arr[nextr][nextc])
        
        return res
