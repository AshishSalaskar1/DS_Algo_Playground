"""
PROBLEM: Sum of Beauty of All Substrings
https://leetcode.com/problems/sum-of-beauty-of-all-substrings/

Expected TC: O(N^2)

SOLUTION:
-> Iterate all substrings (N**2) 
-> Since you maintain counter (can have 27 elements at max) => consider this as O(1)

TC: O(N^2+26) = O(N*N)

"""

class Solution:
    def get_beauty(self, cmap):
        minv, maxv = float('inf'), float("-inf")

        for num, count in cmap.items():
            minv = min(minv, count)
            maxv = max(maxv, count)
        
        return maxv-minv

    def beautySum(self, s: str) -> int:
        n = len(s)
        res = 0

        for i in range(n):
            cmap = {}
            for j in range(i,n):
                cmap[s[j]] = cmap.get(s[j],0) + 1
                beauty = self.get_beauty(cmap)
                if beauty > 0:
                    res += beauty
        
        return res


        