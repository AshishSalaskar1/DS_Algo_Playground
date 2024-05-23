
"""
-> SORT ONLY BY END TIME - Earlier you finish the more you can take

-> For each interval, dont add to res in case it overlaps
-> In this case you can remove this (remove_count += 1)
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        arr = sorted(intervals, key = lambda x:(x[1],x[0]))
        n = len(arr)
        res = []
        remove_count = 0

        for x in arr:
            if len(res) == 0:
                res.append(x)
                continue
            
            if x[0] < res[-1][1]:
                remove_count += 1
            else:
                res.append(x)

        return remove_count 
        

"""

# Example 1:

# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
# Example 2:

# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
# Example 3:

# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

=> Sort by start,end will fail in this case
-> SORT ONLY BY END TIME - Earlier you finish the more you can take
"""