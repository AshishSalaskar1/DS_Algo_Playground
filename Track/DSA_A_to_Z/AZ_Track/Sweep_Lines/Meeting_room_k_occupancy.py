"""
# Sweep Line Algorithms

### Intuition
- Consider you have a straight vertical line, you sweep this line from Left -> Right
- Now, there maybe points of interest where you would want to place this line and check for some properties (ex, how many planks does it intersect. etc)

## Q: Meeting room duration with atleast `k` occupancy
- You have intervals (enter,exit) indicating when a person entered and left the meeting room
- Now, you need to find the duration for which the meeting room had atleast `k` people

Example:
intervals = (1,5), (2,8), (7,10), (9,11)
k = 2
answer = 5 => (2,5)+(7,8)+(9,10) # these ranges had atleast 2 people in the room

"""

def meeting_duration_k(intervals, k):
    points = []
    for entry, exit in intervals:
        points.append((entry, 1)) # enter means num_ppl += 1
        points.append((exit, -1)) # exit means num_ppl += 1

    events = sorted(points)
    nevents = len(events)
    res = 0
    cur_ppl = 0

    for i in range(0, nevents):
        cur_ppl += events[i][1]
        if cur_ppl >= k and i+1<nevents: # if you have >= k people
            # now the cur_ppl will remain same untill next event (event[i+1])
            res += events[i+1][0] - events[i][0]

    return res

intervals = [(1,5), (2,8), (7,10), (9,11)]
k = 2
print(meeting_duration_k(intervals,k))
