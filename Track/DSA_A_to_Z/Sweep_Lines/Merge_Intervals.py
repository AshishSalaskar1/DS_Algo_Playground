"""
IDEA:
- start: active++, end: active--
- when active goes from 0 to 1, new interval starts -> Save previous interval if any
- when active goes from 1 to 0, interval ends -> Save end time
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        events = []
        for start,end in intervals:
            events.append((start, "s"))
            events.append((end, "e"))

        # in case of tie, pick start first
        # better: use "astart", "bend" to solve tie automatically
        events = sorted(events, key = lambda x: (x[0], 0 if x[1] == "s" else 1))
        res = []

        active_intervals = 0
        active_interval_start = None
        active_interval_end = None
        for i in range(len(events)):
            time, op = events[i]

            if op == "s":
                if active_intervals == 0: # new interval starts
                    if active_interval_start is not None: # to ignore first start
                        res.append((active_interval_start, active_interval_end))
                    active_interval_start = time
                active_intervals += 1
            else:
                active_interval_end = time
                active_intervals -= 1

        res.append((active_interval_start, active_interval_end))
        return res

        