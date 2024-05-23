class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals) # sort based on (start,end) times
        n = len(intervals)
        res = []

        for i in range(n):
            if len(res) == 0: # first element -> always pickup
                res.append(intervals[i])
                continue

            if intervals[i][0] <= res[-1][1]: # add to existing picked, if start is less then end of last_taken
                # why max? last_taken.end can be > current.end
                # [[1,4],[2,3]] => TAKE [1,4] => now (2,3) gets merged but it becomes [1,4] instead of [1,3]
                res[-1][1] = max(intervals[i][1], res[-1][1])
            else:
                res.append(intervals[i])
        
        return res

        