"""
https://leetcode.com/problems/find-substring-with-given-hash-value/description/?envType=problem-list-v2&envId=rolling-hash
"""

class Hasher:
    def __init__(self, s, k, modnum):
        self.n = len(s)
        self.s = s
        self.modnum = modnum
        self.k = k

        self.hash = [0] * (self.n + 1)
        self.revhash = [0] * (self.n + 1)
        self.pow = [0] * (self.n + 1)

        self.pow[0] = 1

        for i in range(1, self.n + 1):
            val = ord(s[i - 1]) - ord('a') + 1
            self.hash[i] = (self.hash[i - 1] * self.k + val) % self.modnum
            self.pow[i] = (self.pow[i - 1] * self.k) % self.modnum

        for i in range(self.n - 1, -1, -1):
            val = ord(s[i]) - ord('a') + 1
            self.revhash[i] = (self.revhash[i + 1] * self.k + val) % self.modnum

    def get_revhash(self, l, r):
        # EXTRA MOD NEEDED HERE for dealing with negative mod
        return (self.revhash[l] - (self.revhash[r + 1] * self.pow[r - l + 1]) % self.modnum + self.modnum) % self.modnum

class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        hasher = Hasher(s, power, modulo)
        n = len(s)

        for i in range(n - k + 1):
            if hasher.get_revhash(i, i + k - 1) == hashValue:
                return s[i:i + k]
