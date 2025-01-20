"""
PROBLEM:
You are given an array of integers nums and an integer k.

Return the maximum sum of a 
subarray
 of nums, such that the size of the subarray is divisible by k.

SOLUTION:
k =2, arr=[1,2,3,4,5,6,7,8,9]

(ONE BASED INDEXING) 
 1 2 3 4 5 6 7 8
[1,2,3,4,5,6,7,8,9]

prefix[8] = x
- Now subarray sum of size which are multiples of k=2 (2,4,6,8,10....), 
    => means prefix[8]-MIN(prefix[6], prefix[4],prefix[2],prefix[0])
    - We use min, since we want to maximise prefix[8]-prefix[j]

IMP: If you do `i%k` you see that all multiples of (0->k-1) will be grouped into similar buckets
- prefix[8]-MIN(prefix[6], prefix[4],prefix[2],prefix[0])
    6%2 = 0, 4%2 = 0, 2%2=0 .....
- prefix[9]-MIN(prefix[7], prefix[5],prefix[3],prefix[1])
    7%2 = 1, 5%2=1, 3%2 = 1

SOLUTION: Just have a `min_prefix_sum` array which stores min-value out of all prefix sums of multiples of that remainder
"""
class Solution:
    def maxSubarraySum(self, arr: List[int], k: int) -> int:
        n = len(arr)
        res = float("-inf")

        min_prefix_sum = [float("inf")]*(k)
        min_prefix_sum[0] = 0 # IMP

        prefix_sum = 0
        for i in range(1,n+1):
            prefix_sum += arr[i-1]

            rem = i%k
            res = max(res, prefix_sum-min_prefix_sum[rem])

            min_prefix_sum[rem] = min(min_prefix_sum[rem], prefix_sum)
        
        return res



        