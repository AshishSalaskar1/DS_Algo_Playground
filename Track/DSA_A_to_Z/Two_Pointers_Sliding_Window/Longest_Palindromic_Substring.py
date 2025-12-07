"""
IDEA:
- Given a point `i`, can you find the largest palindrome with `i` as center
    1. ODD LENGTH PALINDROMES: You can consider `i` as center and move 1 each on left and right outwards till s[l]=s[r]
    2. EVEN LENGTH PALINDROMES: You can consider `i`,`i+1` as center and move 1 each on left and right outwards till s[l]=s[r]


SOLUTION: Expand out from every point
- for `i` in range(n):
    EXPAND(left=i, right=i) # assuming `i` is centre of large odd length palindrome
    EXPAND(left=i, right=i+1) # assuming (i,i+1) are centres of large even length palindrome
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def expand(left: int, right: int, n: int):
            nonlocal res, maxlen
            while left>=0 and right<n and s[left] == s[right]: 
                if right-left+1 > maxlen:
                    maxlen = right-left+1
                    res = s[left:right+1]
                left -= 1
                right += 1

        
        maxlen, res = 0,""
        for i in range(n):
            # assuming this is center of ODD length palindromic string
            l,r = i,i
            expand(l,r,n)

            # assuming this is center of EVEN length palindromic string
            l,r = i,i+1
            expand(l,r,n)
        
        return res


        