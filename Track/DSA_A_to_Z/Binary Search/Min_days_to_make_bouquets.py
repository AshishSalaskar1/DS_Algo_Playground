"""
Link: https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/

SOLUTION: Binary Search Applied on answers
- Min days you can make all bouquets: 0 (all bloom at day 0)
- Max days you can make all bouquets: max(arr) (you will wait till all flowers bloom)
- Do bin_search on lo=0,hi=max(arr)
    - for each time(mid), check how many consecutive flowers you can pull and check
"""

class Solution:
    def can_make(self, arr, size, n, time):
        arr = [True if x<=time else False for x in arr]
        rem_n = n
        count = 0
        for x in arr:
            if x is True:
                count += 1
            else: # whenever you see a FALSE (check in the prev consec flowers you can choose )
                # 
                rem_n -= (count//size)
                count = 0 # reset count
        
        rem_n -= (count//size) # [T,T,F,F,T,T,T]
        return True if rem_n<=0 else False

    def minDays(self, arr: List[int], m: int, k: int) -> int:
        lo,hi = 1, max(arr)
        min_days_needed = float("inf")
        while lo<=hi:
            mid = lo + (hi-lo)//2
            if self.can_make(arr, k, m, mid):
                min_days_needed = min(min_days_needed,mid)
                hi = mid-1
            else:
                lo = mid+1
        return min_days_needed if min_days_needed!=float("inf") else -1
               