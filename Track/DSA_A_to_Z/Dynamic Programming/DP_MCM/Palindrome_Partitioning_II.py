class Solution:
    def check_palindrome(self, s):
        return s == s[::-1]

    @cache
    def solve(self, i, s):
        if i >= self.n:
            return 0            
        
        min_res = float("inf")
        for cut in range(i, self.n):
            if self.check_palindrome(s[i:cut+1]):
                res = 1 + self.solve(cut+1, s)
                min_res = min(min_res, res)
        
        return min_res

    def minCut(self, s: str) -> int:
        if self.check_palindrome(s):
            return 0
            
        self.n = len(s)
        self.s = s
        return self.solve(0,s)-1
        