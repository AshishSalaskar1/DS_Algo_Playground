"""
Problem: Given a array can you divide your array into 2 subsets such that sum of each subsets is same
- You need to use all elements, sum(subset1) = sum(subset2)

intuition
- SUM(subset1) + SUM(subset2) = SUM(arr) [BUT SUM(subset1)=SUM(subset2)]
- 2*SUM(subset1) = SUM(ARR)
- SUM(subset1) = SUM(subset2) = SUM(ARR) / 2

Solution
- Find SUM expected of each subset
- If SUM is float => You cant make sum which is in float (would require you to split each item)
- If not float => can_you_make_subset_sum_target(arr, SUM(arr)//2)

"""

def subsetSumToK(arr, target):
    n = len(arr)
    dp = [[False for _ in range(target+1)] for _ in range(n)]

    for i in range(n):
        for j in range(target+1):
            if j==0: # to make 0 target -> dont pick anything 
                dp[i][j] = True
            elif i==0: # you have only first element (1 coin)
                dp[i][j] = True if j==arr[i] else False
            elif arr[i] > j: # you cant pick current one (curr > needed_target)
                dp[i][j] = dp[i-1][j]
            else: # you can either pick this one or ignore
                dp[i][j] = dp[i-1][j-arr[i]] or dp[i-1][j]
    
    return dp[-1][-1]

def canPartition(arr, n):
    expected_sum = sum(arr)/2

    if int(expected_sum) != expected_sum:
        return False
    
    # int(expected_sum) -> since we use sum(arr)/2 and not sum(arr)//2
    return subsetSumToK(arr, int(expected_sum))