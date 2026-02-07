"""
https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/?envType=daily-question&envId=2026-02-07

SOLUTION:
- Simple prefix suffix sum with one change
- FOR FROM -1 --> (n-1)
    - Why? str = "aaabbbaba"
    - You need to check both nothing on right and nothing on left
    -> |aaabbbaba and aaabbbaba|
    - -1 checks making everything in string as 'b'
    - (n-1) checks making everything in string as 'a'

"""
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)

        bleft, aright = [0]*n,[0]*n
        bleft[0] = 1 if s[0] == "b" else 0
        aright[-1] = 1 if s[-1] == "a" else 0

        for i in range(1,n): bleft[i] = bleft[i-1] + (1 if s[i]=="b" else 0)
        for i in range(n-2,-1,-1): aright[i] = aright[i+1] + (1 if s[i]=="a" else 0)

        res = n

        # MOST IMPORTANT: (-1 -> n-1) 
        for i in range(-1,n):
            blcount = bleft[i] if i>=0 else 0
            arcount = aright[i+1] if (i+1)<n else 0

            res = min(res, blcount + arcount)
        
        return res