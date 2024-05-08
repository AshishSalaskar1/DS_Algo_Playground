"""
PROBLEM:  Number of Longest Increasing Subsequence
- Given an integer array nums, return the number of longest increasing subsequences.
- Notice that the sequence has to be strictly increasing


Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.

SOLUTION:
- You cant directly do dp[j]+dp[i] since its considers only best count and not total count (same LIS_len but diff elements)
- So you need to mantain a n_updates array which gets updated in 2 cases
    - UPDATE: You saw the same LIS again
    - RESET: You found a new LIS

https://leetcode.com/problems/number-of-longest-increasing-subsequence/solutions/3797231/best-python-solution-full-explanation-100/
https://leetcode.com/problems/number-of-longest-increasing-subsequence/


"""


class Solution:
    def findNumberOfLIS(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [0 for _ in range(n)]
        n_updates = [1 for _ in range(n)] # each LIS len has atleast 
        dp[0] = 1 

        for i in range(1,n):
            max_lis_len = 1
            for j in range(0,i):
                if arr[j] < arr[i]:
                    new_len =  1 + dp[j]
                    if new_len == max_lis_len: # same LIS found again -> incremenet n_udpates
                         n_updates[i] += n_updates[j]
                    elif new_len > max_lis_len: # new LIS found
                        max_lis_len = new_len # update LIS
                        n_updates[i] = n_updates[j] # reset n_udpates with n_updates of arr[j]

            dp[i] = max_lis_len

        lis, nlis = max(dp), 0
        for i in range(n):
            if dp[i]==lis:
                nlis += n_updates[i]
        

        return nlis

        