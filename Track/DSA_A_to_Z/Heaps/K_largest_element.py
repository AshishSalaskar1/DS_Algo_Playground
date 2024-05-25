from queue import PriorityQueue
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = PriorityQueue()
        for x in nums:
            pq.put(-x)
        
        # remove top k-1 items
        for _ in range(k-1):
            pq.get()
        
        # return top kth
        return -pq.get()
        

        