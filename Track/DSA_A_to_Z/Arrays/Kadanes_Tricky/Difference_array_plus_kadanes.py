"""
Maximum Score Of Spliced Array
LINK: https://leetcode.com/problems/maximum-score-of-spliced-array/

A   : 20  40  20  70  30 = 180
B   : 50  20  50  40  20 = 180
A-B :-30  20 -30  30  10

=> GAIN in `B replacing something in `B` with something in `A`
- This is exaclty DIFFERENCE(A-B)

=> Why A-B and not B-A?
- Assume you replace i=0 from A in B
- B[0] = 50 replaced by 20 => 50-20 = 30 ( this is actuall the loss, you negate it)
- So its -(50-20)
= THIS IS SAME AS DONG -(B-A) = A-B

==> SOLUTION
1. Call solve(arr1, arr2) and solve(arr2, arr1)
2. Calculate diff array
3. Find max-subarray-sum of (A-B) -> this indicates what more you can gain
4. ANS = max-syb-sum(A-B) + SUM(B)

Example Contd:
A   : 20  40  20  70  30 = 180
B   : 50  20  50  40  20 = 180
A-B :-30  20 -30  30  10
Max Subarray Sum of ( A-B ) = [30,10] = 40
Res = 180+40

=> try same with (B,A) and check
"""
class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        def getscore( arr1: list[int], arr2: list[int], n) -> int:
            diff = [-(arr2[i]-arr1[i]) for i in range(n)]

            csum, res = 0, 0
            for x in diff:
                csum = max(0, csum+x)
                res = max(res, csum)
             
            return sum(arr2)+res 
        
        n = len(nums1)
        return max(getscore(nums1,nums2, n), getscore(nums2,nums1, n))
        