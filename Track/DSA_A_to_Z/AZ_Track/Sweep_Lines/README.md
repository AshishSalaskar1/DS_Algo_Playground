# Sweep Line Algorithms

### Intuition
- Consider you have a straight vertical line, you sweep this line from Left -> Right
- Now, there maybe points of interest where you would want to place this line and check for some properties (ex, how many planks does it intersect. etc)
<br><br>

**Note**
1. Most of sweep line problems can be done using `Merge Overlap Intervals` using sorting and some sort of combination. But, hard to find a common pattern in this approach and requires ad-hoc thinking

---
## Q1: Meeting room duration with atleast `k` occupancy
- You have intervals (enter,exit) indicating when a person entered and left the meeting room
- Now, you need to find the duration for which the meeting room had atleast `k` people
- Example
  - intervals = (1,5), (2,8), (7,10), (9,11)
  - k = 2
  - answer = 5 => (2,5)+(7,8)+(9,10) # these ranges had atleast 2 people in the room

**Solution**
1. Add `(enter,+1)`, `(exit,-1)` to `events`
  - Here enter, exit are time_points where you will sweep line
  - Enter = One person added, Exit = One person left (Hence, +1 and -1)
2. Sort(`events`)
3. Iterate (`event_time`, `delta`) in events
  - `num_ppl` += `delta`
  - Lets say now `num_ppl>=k`, at this time i.e `event_time` you have >=`k`
  - **Till when will this property hold?** = Till next event comes.
    - Since events are sorted based on time, there cannot be any changes between `events[i][0]` and `events[i+1][0]`. After that it can change at `events[i+1][0]`
    - So your `num_ppl` holds good in time frame `events[i+1][0]` - `events[i][0]`
    - This is one duration where your condition holds true. Keep on summating such durations

    ```py
    def meeting_duration_k(intervals, k):
        points = []
        for entry, exit in intervals:
            points.append((entry, 1)) # enter means num_ppl += 1
            points.append((exit, -1)) # exit means num_ppl += 1

        events = sorted(points)
        nevents = len(events)
        res, cur_ppl = 0, 0

        for i in range(0, nevents):
            cur_ppl += events[i][1]
            if cur_ppl >= k and i+1<nevents: # if you have >= k people
                # now the cur_ppl will remain same untill next event (event[i+1])
                res += events[i+1][0] - events[i][0]

        return res
    ```
---
### Question Bank
- Leetcode Discussion Refs: https://leetcode.com/discuss/study-guide/2166045/line-sweep-algorithms
- [SIMPLE] CSES-Restaurant Customers: https://cses.fi/problemset/task/1619
