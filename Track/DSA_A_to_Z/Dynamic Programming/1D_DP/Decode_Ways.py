"""
https://leetcode.com/problems/decode-ways/submissions/1824074734/

VIDEOS: 
- https://www.youtube.com/watch?v=jFZmBQ569So&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=20
- https://www.youtube.com/watch?v=FEkZxCl_-ik


ALGO:
- dp[i] = number of decodings you can do with s[:i] chars

- Cases
1, 2, 2, 3(i)

last = 3
last2 = 23

dp[i] += num_ways(1,2) + 23 # i.e if last 2 are valid
dp[i] += num_ways(1,2,2) + 3 # i.e if last is valid

Why not dp[i-1]+1? 
- Remember if this char can be added, it still stays as 1-decode ( 1 refers to whatever the number was before)
- But, if you can attach this to diferent then it becomes >1
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        cmap = {str(i+1):chr(ord('A')+i) for i in range(0,26)}
        #dp[i] -> how many decodings are possible taking [0:i] items from s
        dp = [0 for _ in range(n)]
        dp[0] = 1 if s[0] in cmap else 0

        for i in range(1,n):
            last_2_chars = s[i-1]+s[i]
            last_char = s[i]
            
            if last_char in cmap:
                dp[i] += dp[i-1]
            if last_2_chars in cmap:
                if i-2>=0:
                    dp[i] += dp[i-2]
                else: # IMP, there are only 2 chars -> STILL U HAVE 2 ways ( Ex: [1,2])
                    dp[i] += 1

        return dp[-1]




        
