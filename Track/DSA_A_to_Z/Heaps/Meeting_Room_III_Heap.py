"""
https://leetcode.com/problems/meeting-rooms-iii/solutions/7441895/solution-of-the-day-it-cant-be-more-simp-30hz
"""

from heapq import heapify, heappush, heappop
from collections import deque
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        free = list(range(n)); heapify(free)
        busy = []
        mcount = [0]*n

        for start,end in sorted(meetings):
            duration = end-start

            # remove all events which end at or before start
            while busy and busy[0][0] <= start:
                _, roomid = heappop(busy)
                heappush(free, roomid)
            
            # can you ingest current meeting
            if free: # YES YOU CAN
                free_roomid = heappop(free)
                heappush(busy, (end, free_roomid))
                mcount[free_roomid] += 1
            else: # NO -> DO IT AFTER THE EARLIEST ENDING MEETING
                earliest_end_ts, roomid = heappop(busy)
                heappush(busy, (earliest_end_ts+duration, roomid))
                mcount[roomid] += 1
        
        return mcount.index(max(mcount))

