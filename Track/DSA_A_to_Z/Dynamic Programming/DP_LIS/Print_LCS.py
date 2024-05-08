"""
SOLUTION:
- Maintain a res array - which stores the LIS till `i`
- res[0] = [arr[0]]
- for i : 1->n:
    res[i] = arr[i] # smallest LIS of size 1
    max_lis_len = 1
    for j : 0->i:
        if arr[j] < arr[i] and newLen beats max_lis_len:    
            1. update max_lis_len
            2. res[i] = [ LIS[j] + arr[i] ]
            - Existing LIS of res + this char
"""

def longestIncreasingSubsequence(N, arr):
    n = len(arr)
    dp = [0 for _ in range(n)]
    dp[0] = 1 

    res = [None for _ in range(n)]
    res[0] = [arr[0]]

    for i in range(1,n):
        max_lis_len = 1
        res[i] = [arr[i]]
        for j in range(0,i):
            if arr[j] < arr[i]:
                new_lis_len = 1 + dp[j]
                if new_lis_len > max_lis_len: # update 
                    max_lis_len = new_lis_len
                    res[i] = [*res[j], arr[i]]

        dp[i] = max_lis_len

    return res[dp.index(max(dp))]