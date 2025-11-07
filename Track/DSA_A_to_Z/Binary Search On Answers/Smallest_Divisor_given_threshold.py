
"""
PROBLEM: 
Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

The test cases are generated so that there will be an answer.

ANSWER: BINARY Search on Answers(divisor)
"""

import math

class Solution:
    def smallestDivisor(self, arr: List[int], threshold: int) -> int:
        # min, max of the divisor
        lo,hi = 1, max(arr)+1

        res = float("inf")

        while lo<=hi:
            mid = lo + (hi-lo)//2
            cur_sum = sum([math.ceil(x/mid) for x in arr])

            if cur_sum <= threshold:
                res = min(res, mid)
                hi = mid-1
            else:
                lo = mid + 1
        
        return res