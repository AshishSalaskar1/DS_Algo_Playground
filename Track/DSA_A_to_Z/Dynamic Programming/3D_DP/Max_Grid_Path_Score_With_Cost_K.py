"""
https://leetcode.com/problems/maximum-path-score-in-a-grid/

SOLUTION:
DP[row][col][cost] = Max score you can obtain by using exactly `cost` and `row x col` values

"""


class Solution:
    def maxPathScore(self, arr: List[List[int]], k: int) -> int:
        nr, nc = len(arr), len(arr[0])
        dp = [[[float("-inf") for _ in range(k+1)] for _ in range(nc)] for _ in range(nr)]

        cost_map = {0: 0, 1: 1, 2: 1}

        start_cost = cost_map[arr[0][0]]
        start_score = arr[0][0]
        if start_cost <= k:
            dp[0][0][start_cost] = start_score
        
        for r in range(nr):
            for c in range(nc):
                for cost in range(k+1):
                    if dp[r][c][cost] == float("-inf"):
                        continue
                    if r+1<nr: # next row is pickable
                        next_row_cost = cost + cost_map[arr[r+1][c]]
                        if next_row_cost <= k:
                            dp[r+1][c][next_row_cost] = max(
                                dp[r+1][c][next_row_cost],
                                dp[r][c][cost] + arr[r+1][c]
                            )
                    if c+1<nc: # next col is pickable
                        next_col_cost = cost + cost_map[arr[r][c+1]]
                        if next_col_cost <= k:
                            dp[r][c+1][next_col_cost] = max(
                                dp[r][c+1][next_col_cost],
                                dp[r][c][cost] + arr[r][c+1]
                            )
        
        # Check max_score using all rows+cols+[cost<k]
        result = -1
        for cost in range(k + 1):
            if dp[nr - 1][nc - 1][cost] >= float("-inf"):
                result = max(result, dp[nr - 1][nc - 1][cost])

        return result if result >= 0 else -1

                     

        


        