"""
PROBLEM: https://leetcode.com/problems/palindrome-partitioning-ii/
- Given a string s, partition s such that every substring of the partition is a palindrome
- Return the minimum cuts needed for a palindrome partitioning of s


SOLUTION: FRONT/HEAD PARTITION METHOD
- Can recursivel
- solve(i, s)
  => Min cut to make sure all are palindromes GIVEN that you make one cut befor "i" (you need to include "i")
    - "aab" -> passing f(0) would mean ur cutting before start |aab
    - "aab" -> passing f(2) would mean ur cutting at end aab|
    - SO U DO RES-1 to offset this INITIAL CUT
  - for cut in range(i,n):
        - if ispalindrome(s[i:cut+1]) # +1 to make sure its inclusive
            res = 1 + solve(cut+1) # you can make another cut after "cut" since its a palindrom from s[i:cut]
        - else continue
  => You dont stop going further if its not palindrome, because s[i:cut] is not pal, but s[i:cut+1] can be a palindrome

=> Example - aab
f(0) => |a => 1 + f(1),
        |aa => 1 + f(2),
        |aab # not palindrome

f(0) -> f(1) => |a|a => 1+f(2)
        |a|ab # not palindrome

f(0) -> f(2) => |aa|b => 1+f(3) = 1+1 = 2

SO RES = f(0), f(2)= you make cuts at 0 and 2 (Initial cut is before 0)
       = f(0) + f(2) - 1

"""

class Solution:
    def check_palindrome(self, s): 
        # can be improved to O(n//2) using 2 pts, now its O(n)
        return s == s[::-1]

    @cache
    def solve(self, i, s):
        if i >= self.n:
            return 0            
        
        min_res = float("inf")
        for cut in range(i, self.n): # check all even if you find palindrome
            if self.check_palindrome(s[i:cut+1]):
                res = 1 + self.solve(cut+1, s)
                min_res = min(min_res, res)
        
        return min_res

    def minCut(self, s: str) -> int:
        if self.check_palindrome(s):
            return 0
            
        self.n = len(s)
        self.s = s
        return self.solve(0,s)-1 # offset 1 due to considering whole string 
        