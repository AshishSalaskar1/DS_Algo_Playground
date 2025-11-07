"""
Minimum Time to Activate String
Link: https://leetcode.com/problems/minimum-time-to-activate-string/

INTUITION: BS on Answers
- if [0:i] is valid -> then anything [0:(i+1,..)] is also valid, since you need num_valid_strings >= k 
- Num of subsets given len N = n(n+1) / 2

- Valid Subsets = All subsets-invalid_subsets
- Ex: [-----*---*--*--]
- invalid subsets - [[-----]*[---]*[--]*[--]]
- For mid -> you visit all positions from order<mid as *(1) and then do Valid Subsets = All subsets-invalid_subsets



"""
class Solution:
    def check_ispossible(self, mid: int):
        arr = [False]*self.n

        # True: star, False: blank
        for i in range(mid+1):
            arr[self.order[i]] = True
        
        # check all bad subset -> subsets containing all o 
        total_subsets = (self.n * (self.n+1)) // 2
        invalid_subsets = 0

        invsize = 0
        for x in arr:
            if x is False: invsize += 1
            elif x is True:
                invalid_subsets += (invsize * (invsize+1)) // 2
                invsize = 0
        
        invalid_subsets += (invsize * (invsize+1)) // 2
        return (total_subsets-invalid_subsets) >= self.k
        

    def minTime(self, s: str, order: List[int], k: int) -> int:
        self.order = order
        self.k = k
        self.n = len(s)
        
        lo,hi = 0, self.n-1
        res = float("inf")
        while lo<=hi:
            mid = lo + ((hi-lo)//2)

            if self.check_ispossible(mid):
                res = mid
                hi = mid-1
            else:
                lo = mid+1
        
        return res if res!=float("inf") else -1
        