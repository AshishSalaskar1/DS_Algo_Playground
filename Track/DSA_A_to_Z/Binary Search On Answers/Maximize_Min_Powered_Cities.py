"""
Problem: https://leetcode.com/problems/maximize-the-minimum-powered-city/?envType=daily-question&envId=2025-11-07

Great Solution: https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/description/

IMPORTANT REMINDERS:
- Here you are not using prefix sum, instead the the diff array ( range addition queries using prefix sum)
- Generally, in Prefix+Range queries you do 
    1. prefix[i-R]+=val, prefix[i+R+1]-=val
    2. Calculate prefix array again -> then prefix[i+R] - prefix[i-R-1]
    BUT HERE, (2) is not needed since you are traversing sequentially
    - Also, you never update the range before the current city/item ( hence no need to go back and re-cal prefix, from here onways you consider this)


CHECK FUNCTION
- At each city, check if it has atleast `target` power
- If not,
    - Then you need (target-curStations). Now to get these extra powers you can assign one station to any of [cur-r : cur+r]
    - 💡You know that all station before curStation are fine, hence no point in putting the stations anywhere that gives power to prev ones
    - Better use would be to place it at the farthest right that it only gives this curStation enough power
    ==> place it at curStation + (range) 
        -> in this way you extra stations from [curStations+r: curStation+r+r] = [curStations+r: curStation+2r]
        
"""
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        prefix = [0]*n


        for i, val in enumerate(stations):
            left = max(0,i-r)
            right = min(n, i+r+1)

            prefix[left] += val
            if right<n: prefix[right] -= val


        def isPossible(minTarget, prefix, r, k):
            """
            - Check if every city can be powered by atleast `minTarget` stations
            - Because you need to check if min(powered_stations) >= minTarget
            """
            diff = prefix.copy()

            newTaken = 0
            curPower = 0

            for i in range(n):
                curPower += diff[i]
                
                if curPower < minTarget: # you need min `minTarget`
                    extraNeeded = minTarget-curPower
                    newTaken += extraNeeded

                    if newTaken > k: return False

                    # give the `extraNeeded` to (i+r)th station
                    # LEFT BOUND
                    #  this is same as doing diff[i] += extraNeeded
                    curPower += extraNeeded 
                    
                    
                    # RIGHT BOUND
                    right = min(n, i+(2*r)+1)
                    if right<n: diff[right] -= extraNeeded
                
            return True


        lo, hi = min(stations), sum(stations)+k+1
        res = 0

        while lo<=hi:
            mid = lo + (hi-lo)//2
            if isPossible(mid, prefix, r, k):
                res = max(res, mid)
                lo = mid+1
            else:
                hi = mid-1
        
        return res

        
        