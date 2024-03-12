"""
PROBLEM: Given array find 2 subsets such the absolute difference of theirs sums is equal 
(You cant ignore any elements, it should be there in one of 2 subsets)

INTUITION:
- S1 + S2 = S ==> S2 = S-S1
- Partition sums are (S1) and (S-S1)
- Find all possible subsets which give sum as S1 and then check which gives least diff

SOLUTION:
- We have DP of size `N`x `target+1`, 
    where each dp[i][j] = can you make target=j using first `i` values (You can ignore also)
- So last row in dp -> dp[n-1] = Can you make targets (j=0 to target ) using all `n` values. Biggest subset sum you can make = target (including all in S1 and s2={})
- Here you iterate through all items in last row
    - Wherever you find True -> means you can sum `j` using all `n` coins
    - For each of these S1=`j`, check |S1 - (S-S1)| and find `j` or `S1` giving least abs difference

"""
# return last row
def subset_sum_tf(n, k, arr):
    dp = [[False for _ in range(k+1)] for _ in range(n)]

    for i in range(n):
        for j in range(k+1):
            if j == 0:
                dp[i][j] = True
            elif i == 0:
                dp[i][j] = (arr[i] == j)
            else:
                if arr[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i]]
  
    return dp


def minSubsetSumDifference(arr, n) -> int:
    totalSum = sum(arr)
    minAbsSum = float('inf')

    dp = subset_sum_tf(n, totalSum, arr)

    for i in range(0, totalSum+1):
        s1 = dp[-1][i] # True|False -> Can you make or not
        if s1:
            curDiff = abs(i-(totalSum-i))
            minAbsSum = min(minAbsSum, curDiff)

    return 0 if minAbsSum == float('inf') else minAbsSum