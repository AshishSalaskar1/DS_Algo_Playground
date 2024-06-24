"""
Problem: Minimum Flips to Make a OR b Equal to c

- https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/solutions/3606850/clear-and-intuitive-explanation-of-bit-manipulation-python

EXAMPLE:
0010 -> 0 0 [0] [1]
0110 -> 0 1 [0]  0
----
0101 -> 0 1  0   1

SOLUTION
- Consider each bit in all 3
- if bit of `c` = 1 => either bit in `a` or `b` must be 1 (1 OR anything = 1, flip bits such that atleast one is 1)
- if bit of `c` = 0 => both buts in `a` and `b` must be 1 (0 OR O = 0, flip such that both bits are set to 0)
"""

class Solution:
    def minFlips2(self, a: int, b: int, c: int) -> int:
        flips = 0
        for i in range(31):
            # i'th bit of c is 1
            if (c >> i) & 1:
                flips += ((a >> i) & 1) == 0 and ((b >> i) & 1) == 0
            # i'th bit of c is 0
            else:
                flips += (a >> i) & 1
                flips += (b >> i) & 1
        return flips
    
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        for i in range(31):
            abit = a & (1<<i) 
            bbit = b & (1<<i)
            cbit = c & (1<<i)
            # print(abit, bbit, cbit)
            abit = 1 if abit>0 else 0
            bbit = 1 if bbit>0 else 0
            cbit = 1 if cbit>0 else 0

            print(abit, bbit, cbit)
            # print()

            if cbit == 0: # c bit = 0
                if (abit==0 and bbit==1) or (abit==1 and bbit==0):
                    flips += 1
                elif (abit==1 and bbit==1):
                    flips += 2
            else: # c bit is 1
                if (abit==0 and bbit==0):
                    flips += 1

        return flips