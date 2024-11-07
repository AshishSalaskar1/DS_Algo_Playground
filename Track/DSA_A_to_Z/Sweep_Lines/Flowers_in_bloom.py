"""
PROBLEM: https://leetcode.com/problems/number-of-flowers-in-full-bloom/

SOLUTION: 
- Classic example of Sweepline (Given enter,exit of ppl from meetingroom. Find at each time what was the number of ppl in meeting room)

CATCHES
1. events.append((end+1, -1))
    - end+1 because, usually on end date/event you do flowers += delta
    - BUT, in this case flowers remains bloomed till data (IT GETS DE-BLOOMED on end+1)

2. Since the queries are huge you need to use binary search
    - Instead of storing (start,end,flower_count) in dict, better store it as 2 arrays - event_change_days,flower_till_day
    - WHY not (start,end,flower_count)? You will have to handle overlaps ( [1,3,2], [3,5,4] for i=2 you need to pick 4 and not 2 - SINCE IT WAS UPDATED LAST)

Binary Search on event_change_days
- bisect_left(arr,x) gives the index in which the element x might be inserted so that its sorted
- here, event_change_days is already sorted
- bisect_left(event_change_days, query_day) will give us the idx of (day+1) where it will be inserted (SO DO IDX-1)

event_change_days = [3,5,6]
bisect_left(arr, 4) = 1 (returns index = 1, since if it was inserted it should have been here)
- but, wkt from 3->5 there is no change in flowers (only change happens at events)
- So, 4 would lie between 3->5 and hence you need flowers_at_loc[3] and not flowers_at_loc[4]

bisect_left(arr, 5) = 2 (returns index = 2, since if it was inserted it should have been here - BISECT_RIGHT())

"""
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        events = []
        last_day = 0
        for start, end in flowers:
            last_day = max(last_day, end)
            events.append((start, +1))
            events.append((end+1, -1)) # end+1 => BECAUSE (1,3) flower still remains bloomed till 3, on 4th it deblooms
        
        events.sort(key=lambda x:x[0])

        event_change_days = []
        flower_till_day = []
        flowers = 0
        for event, delta in events:
            flowers += delta
            event_change_days.append(event)
            flower_till_day.append(flowers)

        
        res = []
        for i in people:
            idx = bisect.bisect_right(event_change_days, i) - 1  # WHY idx-1? read docstring on top 
            res.append(flower_till_day[idx] if idx>=0 else 0)

        return res


        