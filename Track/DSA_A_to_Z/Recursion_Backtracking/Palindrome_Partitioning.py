"""
PROBLEM: https://leetcode.com/problems/palindrome-partitioning/
- Given a string, partition it such that each partition is a palindrome
- Find all such possible partitions
- s = "aab" --> [["a","a","b"],["aa","b"]]


SOLUTION: Front Partition/Pickup + Backtracking(since you need path) + only allow palindromes
- def solve(i): How can divide arr/str after i (include i) into partitions
    - if i == len(s) -> res (since you have partitioned everything before n -> [0:n-1])
    - What all palindromes can you make starting from i? s[i:i], s[i:i+1] ... s[i:n]
        - for end: i -> n:
            if s[i:end+1] is palindrome: # in case palindrome is not found, you just skip n check if next range can be a palindrome
                path.add(s[i:end+1])
                solve(end+1) # you pick new_str, n remaning you let the function partition for you
                path.pop() <- BACKTRACKING

"""

def ispal(s):
    return s == s[::-1]

class Solution:
    def solve(self, i:int):
        if i == len(self.s): # you have partitioned everything
            self.res.append(self.path.copy())
        
        # try to make all possible palindromes starting from i (including i)
        for end in range(i, len(self.s)):
            new_str = self.s[i:end+1]
            if ispal(new_str):
                self.path.append(new_str)
                self.solve(end+1)
                self.path.pop()


    def partition(self, s: str) -> List[List[str]]:
        self.s = s
        self.path = []
        self.res = []

        self.solve(0)
        return self.res
        