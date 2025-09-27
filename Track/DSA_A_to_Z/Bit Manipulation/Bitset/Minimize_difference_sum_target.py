"""
Minimize Difference between target and chosen elements
https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/description/


Here why do you use temp bitset?
- Lets say your bitset = 1 # only 0-sum is possible
- Row = (1,2,3)
WRONG: for val in row: bitset |= bitset<<val
- Here, you add 1 to bitset, then add 2 to the (bitset+1)
- You want to add all these together

HENCE, tempbitset = 0 -> 
temp_bitset = (bitset+1) | (bitset+2) | (bitset+3)
bitset = temp_bitset
"""

class RecursiveSol:
    def minimizeTheDifference(self, arr: List[List[int]], target: int) -> int:
        n = len(arr)
        @lru_cache(maxsize=None)
        def solve(row, csum):
            if row == n:
                return abs(csum-target)
            
            min_diff = float("inf")
            for cnum in arr[row]:
                min_diff = min(min_diff,solve(row+1, csum+cnum))

                if csum+cnum > target:
                    break

            return min_diff

        # OPTIMIZATIONS:
        for i in range(n):
            arr[i] = sorted(set(arr[i]))
        
        return solve(0,0)
        
class BitsetSolution:
    def minimizeTheDifference(self, arr: List[List[int]], target: int) -> int:
        n = len(arr)
        bitset = 1
        MAX_LIMIT = (70**2) + 1

        for row in arr:
            temp_bitset = 0
            # add val to each of the previously seen nums
            for val in set(row):
                temp_bitset |= bitset<<val
            
            bitset = temp_bitset
            
        
        # CAN BE OPTIMIZED: Start searchin LEFT<- TARGET ->RIGHT
        ans = float("inf")
        for i in range(MAX_LIMIT, -1, -1):
            if bitset & (1<<i) != 0:
                ans = min(ans, abs(i-target))
        return ans



        