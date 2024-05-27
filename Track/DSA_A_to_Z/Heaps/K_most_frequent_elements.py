from queue import PriorityQueue
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = PriorityQueue()
        cmap = Counter(nums)

        for num, count in Counter(nums).items():
            pq.put( (-count,num) ) 
        
        res = []
        while k>0:
            res.append(pq.get()[1])
            k -= 1
        
        return res


        