"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3, Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1, Output: ["()"]

SOLUTION: https://leetcode.com/problems/generate-parentheses/solutions/2542620/python-java-w-explanation-faster-than-96-w-proof-easy-to-understand
- At step basically you have 2 options
  1. if len(s) == 2n -> this might be balanced string (SINCE WE MUST INCLUDE ALL n opening+closing)
  2. S + ( | This can be done only if nclose < n
  3. S + ) | This can be done only if nclose < nopen, because if nclose>nopen it wont be balanced

"""
class Solution:
    def solve(self, nopen, nclose, s):
        print(nopen, nclose, s)
        # you know that balanced str will have double length
        # and since we never let nclose > nopen, everything is balanced for sure if len = 2n
        if len(s) == self.n * 2:
            self.res.append(s)
            return
        
        if nopen < self.n: # you can add more opening brackets
            self.solve(nopen+1, nclose, s+"(")
        
        if nclose < nopen: # you can add more closing brackets
            self.solve(nopen, nclose+1, s+")")

    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.res = []
        self.solve(0,0,"")

        print(self.res)
        return self.res
        