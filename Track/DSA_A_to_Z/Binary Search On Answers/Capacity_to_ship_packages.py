"""
PROBLEM:
A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

SOLUTION: Binary Search on answers (here answers = capacity of ship)
- Min capacity of ship: 1
- Max capacity of ship: sum(arr) -> you will carry all weights in single day
- Simple binary search and check if for given capacity(mid) the number of days takes <= days_given
"""

class Solution:
    def can_carry(self, weights, days, capacity):
        ndays = 1
        csum = 0

        for x in weights: 
            if x > capacity: # this item cant fit in the SHIP
                return False
            if csum+x <= capacity:
                csum += x
            else: # you cant pick in current day, pick this is next day
                ndays += 1
                csum = x # IMP -> You automatically pick it up next day
        
        print(f"Capacity: {capacity}, days taken: {ndays}")
        return ndays <= days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo,hi = 0, sum(weights) # max: you can ship everything on one day
        res = float("inf")

        while lo<=hi:
            mid = lo + (hi-lo)//2 # capacity of ship
            print(f"=> {lo}<-{mid}->{hi}")

            if self.can_carry(weights, days, mid):
                print(f"possible in {mid} capacity")
                res = min(res, mid)
                hi = mid-1
            else:
                lo = mid+1
            
            print(f"<= {lo}=={hi}")
        
        return res




        