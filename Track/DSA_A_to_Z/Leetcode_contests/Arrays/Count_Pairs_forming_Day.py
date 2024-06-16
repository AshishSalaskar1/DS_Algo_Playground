"""
PROBLEM: https://leetcode.com/problems/count-pairs-that-form-a-complete-day-ii/
- Given an integer array hours representing times in hours, return an integer denoting the number of pairs i, j where i < j and hours[i] + hours[j] forms a complete day.

- A complete day is defined as a time duration that is an exact multiple of 24 hours.
- Needed TC is O(N), You can use extra space if needed

SOLUTION:
- https://leetcode.com/problems/count-pairs-that-form-a-complete-day-ii/solutions/5319980/map-dictionary-remainder-method-explained-in-detail-o-n-o-1


INTUITION
- If cur hour = hr, hr%24 will give you number of hours you need to add to this to get multiple of 24
- Just check if (24 - hr%24) is already seen and add counts
- Edge case, in case rem=0 you need another rem=0 (which means both dont need anything to add i.e both are multiples of 24)
- LOGIC: each element in hmap is extra hours you need to make total as multiple of 24
    -> 0 means its already multiple of 24, n it can be paired with other multiples of 24
"""

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cmap = {}
        res = 0

        for hour in hours:
            rem = hour % 24

            if rem == 0: # this is multiple of 24, you need another multiple of 24
                res += cmap.get(0, 0)
            else:
                needed = 24-rem # you need these many hours to make another 24
                res += cmap.get(needed, 0)

            cmap[rem] = cmap.get(rem, 0) + 1
        
        return res