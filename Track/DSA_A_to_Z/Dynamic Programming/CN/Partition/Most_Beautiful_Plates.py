"""
Plates

- You are given a `n` stacks of place. Imagine stack as L->R
- Each plate has a profit value and you need to pick exactly `k` plates
- Now in each `stack` you can only pick the stack from bottom ( not from mid )
Ex: 
[
 [10,10,100,30],
 [8,50,10,50]
]
-> you can pick [10],[10,10],[10,10,100].... ( [10,100] is not allowed)

FIND MAX PROFIT THAT YOU CAN GET BY PICKING `k` PLATES EXACTLY


SAMPLES:
k = 5 # 250
[
 [10,10,100,30],
 [8,50,10,50]
]

k=3 # 180
[
    [80,80],
    [15,50],
    [20,10]
]

TABULATION: 

dp[row][plates] = max profit using first `row` rows and taking `plates` plates

"""
import copy
class Solution:
    def solve_tabulation(self, arr, k):
        nr, nc = len(arr), len(arr[0])

        # prefix[i][j] = sum of arr[i][0..j]
        prefix = copy.deepcopy(arr)
        for i in range(nr):
            for j in range(1, len(prefix[i])):
                prefix[i][j] += prefix[i][j-1]

        # dp[row][plates] = max profit using first `row` rows and taking `plates` plates
        dp = [[0 for _ in range(k+1)] for _ in range(nr+1)]

        for row in range(1, nr+1):
            for plates in range(0, k+1):
                dp[row][plates] = dp[row-1][plates]  # take 0 from this row

                for take in range(1, min(plates, nc)+1):
                    dp[row][plates] = max(
                        dp[row][plates], 
                        prefix[row-1][take-1] + dp[row-1][plates-take]
                    )

        return dp[-1][-1]
                
                
    def solve(self, arr, k):
        nr, nc = len(arr), len(arr[0])
        didEnd = False
        
        def dp(row, rem):
            nonlocal didEnd
            if rem==0:
                didEnd = True
                return 0
            
            if row >= nr:
                return 0
                
            best = 0
            cursum = 0
            
            # ignoring everything in current row
            best = max(best,dp(row+1, rem))
            
            for col in range(min(nc, rem)):
                cursum += arr[row][col]
                best = max(
                    best,
                    cursum+dp(row+1, rem-(col+1))
                )
            
            return best
        
        res =  dp(0,k)
        return res if didEnd is True else -1
            
            

k = 5 # 250
arr = [
 [10,10,100,30],
 [80,50,10,50]
]
# print(Solution().solve(arr,k))
print(Solution().solve_tabulation(arr,k))

k=3 # 180
arr = [
    [80,80],
    [15,50],
    [20,10]
]
# print(Solution().solve(arr,k))
print(Solution().solve_tabulation(arr,k))


k=8 # 180
arr = [
    [80,80],
    [15,50],
    [20,10]
]
print(Solution().solve(arr,k))
