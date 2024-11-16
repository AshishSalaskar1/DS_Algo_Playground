"""
Problem: https://leetcode.com/problems/sum-of-scores-of-built-strings/?envType=problem-list-v2&envId=rolling-hash

SOLUTION:
- This is solved in a pure Brute Force - Double Hashing way
- Ideal solution is to use Z function
"""
class Hasher:
    def __init__(self, s, base, mod) -> None:
        self.n = len(s)
        self.base = base
        self.mod = mod

        # Precompute hashes and powers of base
        self.hash = [0] * (self.n + 1)
        self.power = [1] * (self.n + 1)

        for i in range(self.n):
            self.hash[i + 1] = (self.hash[i] * base + ord(s[i])) % mod
            self.power[i + 1] = (self.power[i] * base) % mod

    def get_hash(self, l, r):
        # Hash of substring s[l:r+1]
        return (self.hash[r + 1] - self.hash[l] * self.power[r - l + 1]) % self.mod


class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)
        base1, mod1 = 151, (10**9) + 7
        base2, mod2 = 181, (10**9) + 9

        hasher1 = Hasher(s, base1, mod1)
        hasher2 = Hasher(s, base2, mod2)

        def lcp_len(i):
            """Binary search to find the LCP length of s[0:] and s[i:]."""
            lo, hi = 0, n - i
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if (hasher1.get_hash(0, mid - 1) == hasher1.get_hash(i, i + mid - 1) and
                        hasher2.get_hash(0, mid - 1) == hasher2.get_hash(i, i + mid - 1)):
                    lo = mid + 1
                else:
                    hi = mid - 1
            return hi

        # Calculate the total score
        total_score = 0
        for i in range(n):
            total_score += lcp_len(i)

        return total_score
