"""
Link: https://leetcode.com/problems/maximum-difference-score-in-a-grid/description/


SOLUTION:
- dp[i][j] = max score of path starting from (i,j)
- At each point [i][j], you have these options
    1. Pick this point with right + dp[right]
    2. Pick this point with left + dp[left]
    3. New path from [i,j] -> [i+1,j] (Dont pick path after next point)
    4. New path from [i,j] -> [i,j+1] (Dont pick path after next point)

    dp[i][j] = max(1,2,3,4)

"""

class Solution:
    def maxScore(self, arr: List[List[int]]) -> int:
        nr,nc = len(arr), len(arr[0])
        dp = [[0 for _ in range(nc)] for _ in range(nr)]

        res = float("-inf")
        for i in reversed(range(nr)):
            for j in reversed(range(nc)):
                rpick, rnew , dpick , dnew = float('-inf'), float('-inf') , float('-inf') ,float('-inf')

                # can you move down
                if i+1<nr: # DOWN
                    dpick = (arr[i+1][j]-arr[i][j]+dp[i+1][j]) # pick curr element and then path down
                    dnew = arr[i+1][j]-arr[i][j] # new path from arr[i][j] -> arr[i+1][j] (dont go forward from arr[i+1][j])
                # can you move right
                if j+1<nc: # RIGHT
                    rpick = (arr[i][j+1]-arr[i][j]+dp[i][j+1])  # pick curr element and then path right
                    rnew = arr[i][j+1]-arr[i][j] # new path frm arr[i][j+1] -> arr[i][j+1] (dont go forward from arr[i][j+1])
                
                # WAY1 -> pick curr element in existing path -> max(rpick, dpick)
                # WAY2 -> you start new paths from [i][j] = max(rnew, dnew)
                # DP = MAX(WAY1, WAY2)
                max_by_adding_in_existing_path = max(dpick,rpick)
                max_by_starting_new = max(dnew,rnew)
                dp[i][j] = max(max_by_adding_in_existing_path,max_by_starting_new)   
                res = max(res, dp[i][j])
        
        return res        