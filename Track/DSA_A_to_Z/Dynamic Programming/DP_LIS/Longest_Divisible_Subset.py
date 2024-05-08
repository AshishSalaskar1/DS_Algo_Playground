"""
PROBLEM:
Link: https://leetcode.com/problems/largest-divisible-subset/
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

- answer[i] % answer[j] == 0, or
- answer[j] % answer[i] == 0



SOLUTION:
- Consider it same as PRINTING LCS
- SORT THE ARRAY (Since they asked for subarray and not subsequence)

DP Defns
- DP[i] = max subarray len from 0->i, where each element is divisble by arr[i] or vice versa
- res[i] = List of numbers which gives DP[i]

- Maintain a res array - which stores the LIS till `i`
- res[0] = [arr[0]]
- for i : 1->n:
    res[i] = arr[i] # smallest LIS of size 1
    max_lis_len = 1
    for j : 0->i:
        if arr[j],arr[i] are divisible by either AND newLen beats max_lis_len:    
            1. update max_lis_len
            2. res[i] = [ LIS[j] + arr[i] ]
            - Existing LIS of res + this char
    dp[i] = max_lis_len

INTUITION
- You are location i, 
    - If any index j<i and arr[i] is divisible by arr[j] (or vice versa)
    - Then arr[i] is also divisible by the elments divisible by arr[j] which is res[j]

"""

class Solution:
    def largestDivisibleSubset(self, arr: List[int]) -> List[int]:
        arr = sorted(arr)
        n = len(arr)
        dp = [0 for _ in range(n)]
        res = [None for _ in range(n)]

        dp[0] = 1
        res[0] = [arr[0]]

        for i in range(1,n):
            max_len = 1
            res[i] = [arr[i]]
            for j in range(0,i):
                if arr[j]%arr[i] == 0 or arr[i]%arr[j] == 0:
                    new_len = 1 + dp[j]
                    if new_len > max_len:
                        max_len = new_len
                        res[i] = [*res[j], arr[i]]
            dp[i] = max_len

        # print(dp)
        # print(res)
        return res[dp.index(max(dp))]
