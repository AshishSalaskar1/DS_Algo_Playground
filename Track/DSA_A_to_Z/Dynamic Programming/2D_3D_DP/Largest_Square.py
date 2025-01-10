"""
PROBLEM: https://leetcode.com/problems/maximal-square

SOLUTION: https://leetcode.com/problems/maximal-square/solutions/600149/python-thinking-process-diagrams-dp-approach
- Here, res means its a RESxRES matrix
- Why min of Up, Left and Diagonally top-left?
    -> You can make cur 2 IFF all others are >=1
    -> You can add up something to this 2 IFF all 3 are valid squares (ie >=1)
    00 01
    10 [11]

"""
class Solution:
    def maximalSquare(self, arr: list[list[str]]) -> int:
        arr = [[int(x) for x in row] for row in arr]
        nr, nc = len(arr), len(arr[0])
        dp = arr.copy()
        res = 0

        for i in range(nr):
            for j in range(nc):
                res = max(res, dp[i][j])
                if i==0 or j==0:
                    continue
                elif arr[i][j] == 1:
                    dp[i][j] = min([dp[i-1][j],dp[i][j-1],dp[i-1][j-1]]) + 1
                    res = max(res, dp[i][j])

        print(*dp, sep="\n")
        return res*res