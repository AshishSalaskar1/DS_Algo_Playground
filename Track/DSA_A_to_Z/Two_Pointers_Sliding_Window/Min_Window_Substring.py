"""
Minimum Window Substring:  https://leetcode.com/problems/minimum-window-substring/

"""
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def isValid(smap, tmap):
            for ch, count in tmap.items():
                if smap.get(ch,0) < count:
                    return False
            return True

        
        n = len(s)
        l,r = 0, 0
        cmap = {}
        tmap = Counter(t)
        
        minSize = float("inf")
        res = "" 

        if s == t: return t

        while r<n:
            wsize = r-l+1
            cmap[s[r]] = cmap.get(s[r],0) + 1

            while l<=r and isValid(cmap, tmap):
                if wsize < minSize:
                    minSize = wsize
                    res = s[l:r+1]

                cmap[s[l]] -= 1
                if cmap[s[l]] == 0: cmap.pop(s[l])
                l += 1

                wsize = r-l+1
                

            r += 1
        
        return res



        