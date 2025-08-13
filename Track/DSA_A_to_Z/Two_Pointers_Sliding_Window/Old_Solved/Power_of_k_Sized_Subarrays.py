"""
PROBLEM: leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/description/

"""
from collections import deque
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        if k==1:
            return nums
        q = deque()

        res = []
        for right in range(n):
            if q and q[0]< right-k+1: # new window starting from (right-k+1, right) => jst remove first element
                q.popleft()
            if q and nums[right] != nums[right-1]+1: # this new window is not continious -> clear everything
                q.clear()

            q.append(right)

            if right>=k-1: # result appending starts from k-1
                # append only if qsize==k
                res.append( nums[q[-1]] if len(q) == k else -1 )
        
        return res
            
                



        
        