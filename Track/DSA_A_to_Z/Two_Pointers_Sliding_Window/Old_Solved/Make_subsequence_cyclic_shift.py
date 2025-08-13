"""
PROBLEM: https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/?envType=daily-question&envId=2024-12-04

Answer: https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/solutions/6110638/100-beats-short-simple/?envType=daily-question&envId=2024-12-04

SOLUTION:
- Keep `l` and `r` on s1 and s2 start respectively
- Increment both if s1[l] = s2[r] or can be made equal to s2[r]

IF SUBSEQUENCE -> `r` should reach the end
"""

class Solution:
    def get_next(self, char):
        if char=="z":
            return "a"
        
        return chr(ord(char)+1)

    def canMakeSubsequence(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        l,r = 0,0

        while l<n1 and r<n2:
            if s1[l] == s2[r] or self.get_next(s1[l])==s2[r]:
                r += 1
            l += 1
        return r==n2

        