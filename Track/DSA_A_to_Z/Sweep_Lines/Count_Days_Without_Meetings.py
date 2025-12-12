"""
https://leetcode.com/problems/count-days-without-meetings/?envType=problem-list-v2&envId=o1qf3c31
"""
from collections import defaultdict
class Solution:

    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        n = len(meetings)

        events = []

        # GIVES MEMORY LIMIT EXCEEDED
        # for day in range(1,days+1): events.append((day, "ZRES"))

        for start,end in meetings:
            events.append((start,"BSTART"))
            events.append((end+1,"AEND"))
        events.sort()

        nmeetings = 0
        free_days = 0
        prev_seen_day = 1

        for day, event in events:
            if prev_seen_day < day and nmeetings == 0:
                free_days += day-prev_seen_day
            
            nmeetings += 1 if event=="BSTART" else -1
            prev_seen_day = day
        
        # still some days might remain: Ex last event was at 6, but there are 10 days
        if prev_seen_day <= days and nmeetings == 0:
            free_days += days-prev_seen_day+1
        
        return free_days

    def countDaysHashMap(self, days: int, meetings: List[List[int]]) -> int:
        n = len(meetings)

        events = defaultdict(list)

        # GIVES MEMORY LIMIT EXCEEDED
        # for day in range(1,days+1): events.append((day, "ZRES"))

        for start,end in meetings:
            events[start].append(("BSTART"))
            events[end+1].append(("AEND"))


        nmeetings = 0
        res = 0
        for day in range(1, days+1):
            for event in sorted(events[day]):
                if event == "AEND": nmeetings -= 1
                elif event == "BSTART": nmeetings += 1
            
            if nmeetings == 0: res += 1
        
        return res

        