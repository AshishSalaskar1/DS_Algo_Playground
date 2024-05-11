"""
Link: https://leetcode.com/problems/longest-string-chain/


SOLUTION:
Same LONGEST INCREASING SUBSEQUENCE with 2 changes
- Instead of INCREASING, you can check if its PREDECESSOR
- Order can be jumbled -> SORT ACC TO LEN
  why? because we know that if in (a,b) a is predeccesor of b then len(a) = len(a)+1 and so on
  - lengths will be in sorted order: x,x+1,x+2,x+3 

"""
class Solution:
    def is_predecessor(self, s1, s2):
        """
        Return is s1 is PREDECESSOR of s2
        -> s2 can be created by inserting exactly one more char in s1

        "ab","axx" = False
        "ab","abx" = True
        """
        n1,n2 = len(s1), len(s2)
        if n1 != n2-1:
            return False

        p1,p2 = 0,0
        while p2<n2:
            if p1 < n1 and s1[p1] == s2[p2]:
                p1 += 1
                p2 += 1
            else:
                p2 += 1
        
        return p1==n1 and p2==n2


    def longestStrChain(self, words: List[str]) -> int:
        # you can take any order -> SORT BY LENGTH
        words = sorted(words, key=lambda x:len(x))
        n = len(words)
        dp = [1 for _ in range(n)]

        for i in range(n):
            for j in range(i):
                if self.is_predecessor(words[j], words[i]):
                    dp[i] = max(dp[i], 1+dp[j])
        

        return max(dp)
        

        