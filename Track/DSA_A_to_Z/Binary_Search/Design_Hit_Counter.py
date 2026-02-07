"""
https://www.naukri.com/code360/problems/hit-counter_1230785?leftPanelTabValue=SUBMISSION


- Simple Binary Search

-> BISECT_LEFT -> return the position where you will insert "key" in the array and if duplicates are there put in left most position

IN SHORT: First index before the key

OPTIONS:
- If getHits(ts) are gauranted that will be called with non-decreasing timestamps, we can use a queue to store the timestamps and remove the old timestamps that are out of the 5-minute window. This would allow us to achieve O(1) time complexity for both hit and getHits operations.
- Somthing similar to timeseries DBs
"""
import bisect

class HitCounter:

    def __init__(self):
        self.timestamps = []

    def hit(self, timestamp: int) -> None:
        self.timestamps.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # 5 minutes = 300 seconds
        start_ts = timestamp - 300
        
        first_index = bisect.bisect_left(self.timestamps, start_ts)
        return len(self.timestamps) - first_index
