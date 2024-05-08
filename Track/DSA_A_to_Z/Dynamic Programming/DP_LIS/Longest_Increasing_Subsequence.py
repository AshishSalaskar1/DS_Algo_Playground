"""
LONGEST INCREASING SUBSEQUENCE

SOLUTION:
- dp[i] = LIS by using elements upto `i`
- dp[0] = 1 (only 1 element is present, pick that)
- for i in 1->n:
    - LIS(i) = 1 (assuming you pick only this ele and nothing else)
    - j: iterate from 0->i
        - if arr[j] < arr[i] ==> j can be in LIS including a
        - update LIS = max(LIS[i], 1 + dp[j])
    - dp[i] = LIS(i)

- return MAX(DP) <== its not needed that you pick all elements


VARIATIONS of LIS
1. MIND DELETION TO MAKE ARRAY SORTED
- Min Deletions = len(arr) - LIS(arr)

2. MAXIMUM LIS SUM
- DP[i] -> Max sum of IS ending at i
- Same logic, but in internal for loop instead of max_len pick max_sum

3. MAXIMUM LENGTH BITONIC SEQUENCE
- Bitonic : Increasing than decreasing (ONLY ONE PEAK)
Solution: Two dp arrays -> LIS and LDS
- LIS[i] - length of longest IS ending at i
- LDS[i] - Lenght of lontest Decreasing Subseq starting from i (Populated by reverse traversal L<-R)
- Max len = max(LDS[i]+LCS[i]-1)
WHY? lis gives max increasing subseq till i, n lds gives max decreasing subseq starting from i. Here, i is considered as peak

LDS <PEAK> LIS

"""

def LIS(arr):
    n = len(arr)
    dp = [0 for _ in range(n)]
    dp[0] = 1 

    for i in range(1,n):
        max_lis_len = 1
        for j in range(0,i):
            if arr[j] < arr[i]:
                max_lis_len = max(max_lis_len, 1 + dp[j])
        dp[i] = max_lis_len

    return max(dp) # IMP
            

nums = [10,9,2,5,3,7,101,18] # 2,3,7,101 => 4
