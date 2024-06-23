"""
PROBLEM: Maximum Performance of a Team
- https://leetcode.com/problems/maximum-performance-of-a-team/

SIMILAR: https://leetcode.com/problems/maximum-performance-of-a-team/

MAIN DIFFERENCE - at most k (not totally j)

SOLUTION:
- https://leetcode.com/problems/maximum-subsequence-score/?envType=study-plan-v2&envId=leetcode-75 
- https://leetcode.com/problems/maximum-subsequence-score/solutions/3557261/python3-heap-similar-questions-beats-94-810ms/?envType=study-plan-v2&envId=leetcode-75

"""

from queue import PriorityQueue

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        nums1, nums2 = speed, efficiency
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
            
            # check all possible - at most k
            res = max(res, csum*n2)
            
            # These check is not needed -> AT MOST (You can pick lesser ones also)
            # if len(pq.queue) == k:
            #     res = max(res, csum*n2)
        
        return res % (10**9 + 7)