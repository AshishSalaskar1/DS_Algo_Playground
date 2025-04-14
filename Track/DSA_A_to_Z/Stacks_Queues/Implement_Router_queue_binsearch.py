"""
Problem: Implement Router (https://leetcode.com/problems/implement-router/)

Tasks:
1. FIFO Queue with fixed size -> deque((src, dest, ts))
2. Check for duplicates -> set(tuple(src, dest, ts))
3. Check how many packets are there with same destination within [start_ts, end_ts] 
    => dest_map: dict[dest:[ sorted_ts ]]
    => Use bisect.left to get index to remove
    => bisect.right-bisect.left gives you the span

"""
from collections import deque, defaultdict
from typing import List
import bisect

class Router:

    def __init__(self, memoryLimit: int):
        self.q = deque()
        self.size = memoryLimit
        self.items = set()
        self.dest_map = defaultdict(list)  # destination -> sorted list of timestamps

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        cur_item = (source, destination, timestamp)

        if cur_item in self.items:
            return False

        if len(self.q) == self.size:
            rsrc, rdest, rts = self.q.popleft()
            self.items.remove((rsrc, rdest, rts))

            # Remove timestamp from sorted list
            idx = bisect.bisect_left(self.dest_map[rdest], rts)
            # validation since the dest might not always be present 
            if 0 <= idx < len(self.dest_map[rdest]) and self.dest_map[rdest][idx] == rts:
                self.dest_map[rdest].pop(idx)

        self.q.append(cur_item)
        self.items.add(cur_item)
        bisect.insort(self.dest_map[destination], timestamp)  # keep sorted
        return True

    def forwardPacket(self) -> List[int]:
        if not self.q:
            return []
        
        source, destination, timestamp = self.q.popleft()
        self.items.remove((source, destination, timestamp))

        idx = bisect.bisect_left(self.dest_map[destination], timestamp)
        if 0 <= idx < len(self.dest_map[destination]) and self.dest_map[destination][idx] == timestamp:
            self.dest_map[destination].pop(idx)

        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.dest_map:
            return 0
        
        timestamps = self.dest_map[destination]
        left = bisect.bisect_left(timestamps, startTime)
        right = bisect.bisect_right(timestamps, endTime)
        return right - left
