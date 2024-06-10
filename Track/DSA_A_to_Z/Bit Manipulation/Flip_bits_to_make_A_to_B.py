"""
https://leetcode.com/problems/minimum-bit-flips-to-convert-number/
"""

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # XOR -> Count set bits
        # XOR -> sets 1 where this is mismatch in bits
        res = start ^ goal

        count = 0
        while res != 0:
            count += 1
            res = res&(res-1) # unset rightmost set bit
        
        return count
        