"""
PROBLEM: Maximum Subsequence Score
- https://leetcode.com/problems/maximum-subsequence-score/?envType=study-plan-v2&envId=leetcode-75

SIMILAR: https://leetcode.com/problems/maximum-performance-of-a-team/

SOLUTION:
- https://leetcode.com/problems/maximum-subsequence-score/?envType=study-plan-v2&envId=leetcode-75 
- https://leetcode.com/problems/maximum-subsequence-score/solutions/3557261/python3-heap-similar-questions-beats-94-810ms/?envType=study-plan-v2&envId=leetcode-75

INTUTION:
- U need to select SUBSEQUENCE and not SUBSTRING
- You need to maximize the SUMS(sumlist)*min(minlist)

- Sorting REVERSE BASED ON minList, makes sure that at i, minlist[i] is lowest element from [0,i]
- for each sumEle, minEle
    1. csum += sumEle and add sumEle to minheap
    2. if len(minheap) == k: You have a subsequence of size=k
        now res = max(res, csum*minEle) [wkt that minEle will always be lesser than any index < i]
        csum -= minheap.get() # you are popping lowest value since we need to maxise
            - NOT DOING SLIDING WINDOW (since this is subsequence and NOT subset)
            - You dont need to worry abt minlist value of the item which was removed (IT WILL SURELY BE > minEle)

Example:
k = 3
sumlist = [1,3,3,2]
minlist = [2,1,3,4]

[(2, 4), (3, 3), (1, 2), (3, 1)]
At 2, we know that 2 is min_val among [(2, 4), (3, 3), (1, 2)]

"""
from queue import PriorityQueue

class Solution:
    def maxScore(self, sumlist: List[int], minlist: List[int], k: int) -> int:
        pq = PriorityQueue()

        arr = sorted(list(zip(sumlist, minlist)), key=lambda x:(x[1],x[0]), reverse=True)
        res = 0
        csum = 0

        for sumele,minele in arr:
            # add current one
            csum += sumele
            pq.put(sumele)
            
            # why minele is min here for that k elements? Because you are iterating from [small<-big]
            if len(pq.queue) == k:
                res = max(res, csum*minele)
                csum -= pq.get()
        
        return res
        

        


"""
(1,2) (3,1) (3,3) (2,4)
"""