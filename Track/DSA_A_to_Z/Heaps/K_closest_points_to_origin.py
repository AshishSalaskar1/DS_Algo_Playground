from queue import PriorityQueue
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = PriorityQueue()

        for [x,y] in points:
            pq.put( (math.sqrt(x**2 + y**2), [x,y]) )
        
        res = []
        while k > 0:
            res.append(pq.get()[1])
            k -= 1
        
        return res


        