class Solution:
    # O(N) -> not in place though
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for interval in intervals:
			# the new interval is after the range of other interval, so we can leave the current interval baecause the new one does not overlap with it
            if interval[1] < newInterval[0]:
                result.append(interval)
            # the new interval's range is before the other, so we can add the new interval and update it to the current one
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval
            # the new interval is in the range of the other interval, we have an overlap, so we must choose the min for start and max for end of interval 
            elif interval[1] >= newInterval[0] or interval[0] <= newInterval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        
        result.append(newInterval); 
        return result


    # O(NlogN)
    def insert2(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        # ADD THIS NEW INTERVAL
        intervals.append(new_interval)

        # Sort again, because after adding new its no longer sorted
        intervals = sorted(intervals)

        # VANILLA MERGE INTERVALS
        res = [intervals[0]]
        for x in intervals:
            if x[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], x[1])
            else:
                res.append(x)
        
        return res



        