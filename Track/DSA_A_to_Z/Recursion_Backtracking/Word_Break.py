"""
PROBLEM: Word Break
- Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
- Note that the same word in the dictionary may be reused multiple times in the segmentation.


SOLUTION: Front partition/check way
- function solve(i):
    - Can you break the word from i:n into allowed ones
    - for end in i -> n:
        if s[i:end] in vocab/dictionary:
            - solve(end+1) | you know that one valid break is s[i:end], lets see next
        - ONLY GO AHEAD IF THERE IS BREAKS (valid word breaks)
    
    - In any case if i==n => res=True
        - means the s[i:n] has been broken into words succesfully
        - Why? We dont increment `i` if you cant break it

"""
from functools import cache
class Solution:
    @cache
    def solve(self, i: int) -> None:
        if i >= len(self.s):
            self.res = True
            return

        n = len(self.s)

        results = []
        for j in range(i, n):
            if self.s[i:j+1] in self.vocab:
                self.solve(j+1)



    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        self.res = False
        self.vocab = set(wordDict)
        self.s = s
        self.solve(0,)

        return self.res