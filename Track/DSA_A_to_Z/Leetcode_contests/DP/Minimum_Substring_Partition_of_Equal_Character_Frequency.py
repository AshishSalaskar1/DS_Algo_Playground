"""
Link: https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/description/
"""
class Solution:
    @cache
    def solve(self, i, s):
        if i >= len(s):
            return 0

        hmap = {}
        m = float('inf')

        for j in range(i, len(s)):
            hmap[s[j]] = hmap.get(s[j], 0) + 1 
            if len(set(hmap.values())) == 1:  # can split
                m = min(m, self.solve(j+1, s) + 1)

        return m

    
    def minimumSubstringsInPartition(self, s: str) -> int:
        return self.solve(0, s)
                    
                
                
                
            
                
                    
        