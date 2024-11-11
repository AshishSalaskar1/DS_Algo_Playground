"""
https://leetcode.com/problems/distinct-echo-substrings/description/?envType=problem-list-v2&envId=rolling-hash


Problem: 
- You need to find substrings such that its a plus of 2 substrings
- Ex: "ee" => e+e, abcabc = abc+abc, "leetcodeleetcode" = leetcode + leetcode

Observations:
1. Since you do str+str to form longer_str, it has to have even number of chars (odd lengths cant be split into two same length strings)

SOLUTION:
- for k in range [2,4,6,8.....n]
    - Try all possible substrings of size `k`
    - if hash(l, mid) == hash(mid+1, r) => this means [xxx|yyy] xxx == yyy => ANSWER
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
             self.h1.get_hash(l,r)
        )

class Solution:
    def is_echo_subtring(self, l, r, k):
        
        mid = (l+r)//2
        return self.hasher.get_hash(l,mid) == self.hasher.get_hash(mid+1, r)

    def distinctEchoSubstrings(self, s: str) -> int:
        n = len(s)
        self.s = s
        self.hasher = DoubleHasher(s)
        res = set()

        for k in range(2,n+1,2): # you can have of length n also => leetcodeleetcode
            for left in range(n-k+1):
                right = left+k-1 # since ranges are inclusive
                if self.is_echo_subtring(left, right, k):
                    res.add( s[left:right+1] )
        
        return len(res)
        