
# link: https://leetcode.com/problems/data-stream-as-disjoint-intervals/
"""
Interval: sequence of numbers for start,end having only 1 difference
1,3 -> 1,2,3
1,5 -> 1,2,3,4,5

arr: 1 2 3 6 7
res = [1,3][6,7]
"""

from sortedcontainers import SortedList, SortedSet, SortedDict 
class SummaryRanges:

    def __init__(self):
        self.ranges = SortedSet()
        # 1 2 3 6 7
        
    def addNum(self, val: int) -> None:
        self.ranges.add(val)
        

    def getIntervals(self) -> List[List[int]]:
        arr = list(self.ranges)
        n = len(arr)

        if n == 0:
            return None

        res = [[arr[0],arr[0]]]

        for x in arr[1:]:
            if x-res[-1][1] == 1:
                res[-1][1] = x
            else:
                res.append([x,x])
        
        return res

        





        