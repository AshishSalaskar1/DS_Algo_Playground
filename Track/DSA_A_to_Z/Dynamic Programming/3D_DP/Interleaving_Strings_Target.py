"""
PROBLEM: https://leetcode.com/problems/interleaving-string/

SOLUTION:
res = False
- solve(i,j,k)
    - i,j,k represent index where you are present at for s1,s2,s3 respectively
Base Case: 
    0. When res=True => return (You already found out one combination that works)
    1. When you reach end of s3 -> check if s1 and s2 are also totally utilized
    - Why not end of s1,s2 and s3? One of s1 or s2 may end before, but still items are left in s3 and other string

- If s1[i] == s3[k] or s2[j] == s3[k] => Pick relevant char and move ahead
- If both satisfy conditions try out both conditions. Why? You might reach end only by taking one of these options

- No need to set as False as hard stop, because some cases maybe be false but other paths may work
"""

class Solution:
    @cache
    def solve(self, i: int, j: int, k:int):
        if self.res is True:
            return

        if k == len(self.s3): # you completed forming new string - check if you used all chars in s1 and s2
            if i==len(self.s1) and j==len(self.s2):
                self.res = True
                return

        # pick s1 char if it matches - In case both s1,s2 char match: Try out both options
        if i<len(self.s1) and self.s1[i] == self.s3[k]:
            self.solve(i+1, j, k+1)

        # pick s2 char if it matches
        if j<len(self.s2) and self.s2[j] == self.s3[k]:
            self.solve(i, j+1, k+1)


    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.res = False

        # cant form the result string
        if len(s1)+len(s2) != len(s3):
            return False

        self.solve(0,0,0)
        return self.res