"""
PROBLEM: Maximum Subsequence Score
- https://leetcode.com/problems/maximum-subsequence-score/?envType=study-plan-v2&envId=leetcode-75

SIMILAR: https://leetcode.com/problems/maximum-performance-of-a-team/

SOLUTION:
- https://leetcode.com/problems/maximum-subsequence-score/?envType=study-plan-v2&envId=leetcode-75 
- https://leetcode.com/problems/maximum-subsequence-score/solutions/3557261/python3-heap-similar-questions-beats-94-810ms/?envType=study-plan-v2&envId=leetcode-75

"""
from queue import PriorityQueue

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pq = PriorityQueue()

        arr = sorted(list(zip(nums1, nums2)), key=lambda x:(x[1],x[0]), reverse=True)
        res = 0
        csum = 0

        for n1,n2 in arr:
            # add current one
            csum += n1
            pq.put(n1)

            if len(pq.queue) > k: # exceeds k
                csum -= pq.get()
            
            # again it became full
            # why n2 is min here for that k elements? Because you are iterating from [small<-big]
            if len(pq.queue) == k:
                res = max(res, csum*n2)
        
        return res
        

        


"""
(1,2) (3,1) (3,3) (2,4)
"""