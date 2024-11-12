"""
https://leetcode.com/problems/longest-happy-prefix/submissions/1449928081/?envType=problem-list-v2&envId=rolling-hash

Problem:
- Find longest substring in string such thats its both prefix and suffix

Solving:
Ex 1: level
1. "leve" == "evel"
2. "lev" == "vel"
3. "le"=="el"
4: "l" == "l" => SAME => RES

Ex 2: "ababab"
1. "ababa" == "babab"
2. "abab" == "abab" => RES

-> leftEnd = n-2, rightEnd = 1 (you dont want to compare entire string)

"""

class Hasher:
    def __init__(self, s, k, modprime) -> None:
        self.n, self.k, self.modprime = len(s), k, modprime

        self.hash = [0]*(self.n+1)
        self.pow = [0]*(self.n+1)

        self.pow[0] = 1

        for i in range(1,self.n+1):
            self.hash[i] = ((self.hash[i-1]*self.k) + ord(s[i-1]) + 1) % self.modprime
            self.pow[i] = (self.pow[i-1]*self.k)  % self.modprime

    
    def get_hash(self, l, r):
        return (self.hash[r+1] - (self.hash[l]*self.pow[r-l+1]) )  % self.modprime


class DoubleHasher:
    def __init__(self, s) -> None:
        self.s = s
        self.h1 = Hasher(s, 151, (10**8)+7)
        self.h2 = Hasher(s, 181, (10**8)+21)
    
    def get_hash(self, l, r) -> (int, int):
        return (
            self.h1.get_hash(l,r),
             self.h2.get_hash(l,r)
        )


# 0 1 2 3

class Solution:
    def longestPrefix(self, s: str) -> str:
        hasher = DoubleHasher(s)
        n = len(s)-1

        left_end, right_start = n-1, 1
        res = ""

        while left_end>=0 and right_start<=n:
            if hasher.get_hash(0,left_end) == hasher.get_hash(right_start,n):
                return s[0:left_end+1]

            
            left_end -= 1
            right_start += 1
        
        return res
