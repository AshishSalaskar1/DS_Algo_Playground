"""
https://leetcode.com/problems/count-of-integers/?envType=problem-list-v2&envId=2chw7ar7
"""
from functools import cache
MOD = (10**9) + 7
class Solution:
    def get_ways(self, r: str):
        # cound between 0 -> n
        n = len(r)       
        @cache
        def solve(index, bound, csum):
            if csum > self.maxsum:
                return 0
            if index == n:
                return 1 if self.minsum <= csum <= self.maxsum else 0
            
            ans = 0
            maxd = int(r[index]) if bound else 9
            for d in range(maxd+1):
                ans += solve(
                    index+1,
                    True if bound and d==maxd else False,
                    csum+d
                )
                ans = ans%MOD
            return ans
        
        return solve(0, True, 0)


    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        self.minsum = min_sum
        self.maxsum = max_sum

        return (self.get_ways(num2)-self.get_ways(str(int(num1)-1)))%MOD