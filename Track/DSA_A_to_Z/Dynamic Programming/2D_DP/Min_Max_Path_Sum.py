"""
Link: https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/description/

IDEA:
=> Can you just do max path sum? NO
- Because, at each step if you just take max it wont lead to max later
- WHY? POSxPOS=POS (Fine), NEGxNEG=POS(two minimums) 

MIN MAX IDEA:
1. If current value is positive 
    - You will multiply this with the path product
    # MIN_TILL_NOW: +ve * MIN = +ve ( smallest )=> MINIMUM
    # MAX_TILL_NOW: +ve * MAX = +ve ( largest ) => MAXIMUM 
2. If current value is negative
    - You will multiply this with the path product 
    # MIN_TILL_NOW: -ve * MAX = -ve ( larger )=> MINIMUM
    # MAX_TILL_NOW: -ve * MIN = -ve ( smaller) => MAXIMUM 

"""


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        mod = 10**9 + 7
        m, n = len(grid), len(grid[0])

        maxgt = [[0] * n for _ in range(m)]
        minlt = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                val = grid[i][j]

                if i == 0 and j == 0:
                    maxgt[i][j] = minlt[i][j] = val

                elif i == 0:  # first row (only from left)
                    maxgt[i][j] = minlt[i][j] = maxgt[i][j - 1] * val

                elif j == 0:  # first column (only from top)
                    maxgt[i][j] = minlt[i][j] = maxgt[i - 1][j] * val

                else:
                    if val >= 0: # CUR IS +ve => MIN: min of choices, MAX: max of choices
                        # MIN: +ve * MIN = +ve ( smallest )=> MINIMUM
                        # MAX: +ve * MAX = +ve ( largest ) => MAXIMUM 
                        maxgt[i][j] = max(maxgt[i][j - 1], maxgt[i - 1][j]) * val
                        minlt[i][j] = min(minlt[i][j - 1], minlt[i - 1][j]) * val
                    else: # CUR is -ve => MIN: max of choices, MAX: min of choices
                        # MIN: -ve * MAX = -ve ( larger )=> MINIMUM
                        # MAX: -ve * MIN = -ve ( smaller) => MAXIMUM 
                        maxgt[i][j] = min(minlt[i][j - 1], minlt[i - 1][j]) * val
                        minlt[i][j] = max(maxgt[i][j - 1], maxgt[i - 1][j]) * val

        res = maxgt[m - 1][n - 1]
        return res % mod if res >= 0 else -1