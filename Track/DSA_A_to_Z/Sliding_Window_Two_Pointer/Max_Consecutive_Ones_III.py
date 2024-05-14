"""
PROBLEM:
- Link: https://leetcode.com/problems/max-consecutive-ones-iii/
- Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's


SOLUTION:
- Change question: Find max subarray such that it has at max "k" zeros
- Two pointer + sliding window
- Take 2 ptrs left and right
    - If arr[right] = 0, 0count++
    - if 0count > k: SLIDING WINDOW REDUCE
        - left++ until 0count <= k
    - r++
    - maxLen = max(maxLen, right-left+1)

"""

class Solution:
    def longestOnes(self, arr: List[int], k: int) -> int:
        n = len(arr)
        l,r = 0,0 

        zero_count = 0
        max_len = 0

        while l<=r and l<n and r<n:
            if arr[r] == 0: # in case its 0 -> increment 0 count
                zero_count += 1
            
            if zero_count > k: # shrink window from left until zero_count <= k
                while l<=r and l<n and r<n and zero_count > k:
                    if arr[l] == 0:
                        zero_count -= 1
                    l += 1
  
            r+= 1 # increment right
            max_len = max(max_len, r-l)

        return max_len

        