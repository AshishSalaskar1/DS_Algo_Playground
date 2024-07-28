"""
PROBLEM: https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special

SOLUTION: 
- https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special/solutions/5546339/sieve-of-eratosthenes/
- Special number is one having exactly 2 divisors (apart from itself)
    - So all squares of primes are special number
    - prime nums have only 1 divisor apart from itself (which is 1)
    - prime^2: will have 2 divisors -> 1, sqrt(num) [and itself also]
"""

import math
class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        n = int(math.sqrt(r+1))
        isprime = [True]*(n+1)
        isprime[0] = isprime[1] = False

        for i in range(2, int(math.sqrt(n))+1):
            if isprime[i]:
                for j in range(i*2, n+1, i):
                    isprime[j] = False


        special_nums = 0
        for i in range(2, n+1):
            if isprime[i] and l<=i*i<=r:
                special_nums += 1

        return (r-l+1)-special_nums


        