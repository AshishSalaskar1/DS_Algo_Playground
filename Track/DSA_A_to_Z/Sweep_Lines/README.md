# Sweep Line Algorithms

### Intuition
- Consider you have a straight vertical line, you sweep this line from Left -> Right
- Now, there maybe points of interest where you would want to place this line and check for some properties (ex, how many planks does it intersect. etc)
<br><br>

**Note**
1. Most of sweep line problems can be done using `Merge Overlap Intervals` using sorting and some sort of combination. But, hard to find a common pattern in this approach and requires ad-hoc thinking
2. Dont use this to solve `Merge Intervals Problem` - Might become a bit complex. Better to do that using sort + iteration approach ( can be done though)


### **Comparison Trick**
 - Generally events are in form `(time, start|end)`
 - Now you need to sort such that if time ties then `start` should be come first and then `end`
 - Sol1: `sorted(events, lambda x:(x[0],0 if x[1]=="start" else 1))`
 - Sol2 **Auto tie break**: `events` = `(time, astart, bend)` *(Here start will automatically come before b)*
- 💡 **MOST CASES** -> time tie -> Prefer `end` then `start`
- Great example with lots of camparisons: `Count_Mentions.py`

### ❓ Common Postprocessing ❓
When you are doing sweepline -> you only visit the `event_points`. If you need some answer for other points in which events havent occured how would you do it?
1. **Save Critical Points -> SORT -> Some Operation**
   - Save all your critical point changes to a hashMap -> sort it ( be careful about same day events )
   - Now you will have all critical points and then you can find the res
    1. **If needed for all points**: Better to iterate this critical points array and do something to get answers
    2. **If its point queries** -> better to use binary search
2. **Saving Events in HashMap instead of List**
   - Put all events in dict: `events[time/day]` = `[ events ]`
   - Iterate for each day -> process all events *(sort for ordering)* -> save result for that day
   - - Ex: `Count_Days_Without_Meetings.py` , `Shifting_Letters_2.py`
3. **Directly adding each day as dummy event** 
   - Put all events
   - Then put each day as dummy event which indicates that you need to save result -> but make sure this dummy event comes after every other event type
   - Cons: Might give MLE since you are adding every index to events list -> sorting ( TOO MANY EVENTS TO SORT)
   - Ex: `Count_Days_Without_Meetings.py`  

### 🏮 **Sweepline + Binary Search**
**REMEMBER**: `bisect.bisect_right(ts)-1` | `if bisect_op > 0`

**Issue**: Lets say you are asked to give the `concurrent` meetings at any index `i`
- Start: add events -> sort -> run sweepline
- **Iteration**: At `critical_point` -> wehever the `concurrent` changes save it in a `map` or even better `SortedMap` if possible
- **Queries**: Now you get `concurrent_at(ts)` queries *( but you  may not have count at exactly k)*
- **PostProcessing**
  1. `criticalTsList` = [ `sorted set of all criticalPointTimestamps`] *(I**MP: timestamps not the actual critical point active values**)*
  2. **concurrent_at(ts)** -> 
     1. `criticalTsNearest` = `bisect.bisect_right(criticalTsList, ts)-1`
     2. `res` = `CriticalPointMap[criticalTsNearest]`
- ❓❓❓ Why `bisect.bisect_right(ts)-1`?
  - `criticalTsList` = `[0,2,2,2,5]`
  - In case `ts=1` if `criticalTsList` not in `ts` -> bisect returns ideal place to insert this in the array to mantain sorted order. This means it will insert it after the critical point just before `ts` ===> **res=1**
  - Now, we know that the value of `active` remains same until another critical point  comes. So the critical point just before `ts` should be my answer ===> **HENCE -1** = `bisect.bisect(ts)-1`
  - WHY **BISECT_RIGHT**? If the `ts` is already present and multiples then we need the last occurence of the `ts` -> right most ( hence bisect_right). *(You need to make sure in sorting+processing that right most is the last update in case of same critical points)*
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
- Yt Video Best: https://www.youtube.com/watch?v=QBQvTjNaIRw
- [SIMPLE] CSES-Restaurant Customers: https://cses.fi/problemset/task/1619
- [SIMPLE] My Calendar II - https://leetcode.com/problems/my-calendar-ii/description/
- [SIMPLE] Car Pooling - https://leetcode.com/problems/car-pooling/submissions/1436410743/
