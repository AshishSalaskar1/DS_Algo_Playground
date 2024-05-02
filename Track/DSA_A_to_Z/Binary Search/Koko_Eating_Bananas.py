"""
Problem: https://leetcode.com/problems/koko-eating-bananas/description/

Important Part Missing in questions: Use Ceil in case of fractions
Ex: speed = 4, [3,6,7,11]
Pile = 3 takes 3/4=1 hours to finish
Pile = 6 takes 6/4=2 hours to finish
Pile = 7 takes 3/7=1 hours to finish
Pile = 11 takes 3/11=1 hours to finish

This takes 5 hours to finish all piles which is < H=8
You need to find MIN SPEED such that ITS<H but you can finish all bananas

SOLUTION: Binary Search on answers
- Lower bound: 1 - Speed of eating 1 bananas per hour
- Highest Bound: max(arr)
    - Fastest time you can eat all bananas = len(arr) [rememeber you cant eat 2 piles even if you have that speed]
    - For this fastest time, what will be the speed?
    - To make sure you eat each pile in 1 hr, make sure your speed=max(arr) so that you can eat the biggest pile in 1 hr

"""
import math
class Solution:
    def is_possible(self, arr, hrs, speed):
        hrs_taken = sum([math.ceil(x/speed) for x in arr])
        print(speed, hrs_taken, hrs)
        return hrs_taken <= hrs

    def minEatingSpeed(self, arr: List[int], h: int) -> int:
        lo, hi = 1, max(arr)
        res = float("inf")
        

        while lo<=hi:
            mid = lo + (hi-lo)//2
            # print("=>", lo, mid, hi)
            if self.is_possible(arr, h, mid):
                # print(mid)
                res = min(res, mid)
                hi = mid-1
            else:      
                lo = mid+1
        
        return res if res != float("inf") else -1
        