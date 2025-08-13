# Sweep Line Cheatsheet

Idea
- Sort critical events along a line (usually time or coordinate)
- Maintain active count/structure while sweeping

Classic encoding
- Interval [L,R): push (L,+1), (R,-1); sort and accumulate to count overlaps
- For k-overlaps duration, when count>=k add next_event_time - cur_event_time

Data structures
- Simple counts via prefix of deltas
- Ordered maps/multisets or heaps for more complex variants (e.g., max overlap value)

Pitfalls
- Inclusivity: [L,R) vs [L,R]; order exits before entries when equal if needed
- Large coordinates: compress if necessary

Practice
- Restaurant Customers (CSES)
- Car Pooling (LC)
- My Calendar II (LC)

Refs
- Repo Sweep_Lines README

# Sweep Line Cheatsheet (verbatim)

Meeting room duration with at least k occupancy (from Sweep_Lines/Meeting_room_k_occupancy.py)
```python
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
```

---

## 🗺️ Quick map
- 🧮 Event sorting (enter/exit)
- 📊 Active set/counter maintenance
- ⏱️ Aggregate durations/overlaps

## ✅ Study checklist
- [ ] Event ordering ties consistent (enter before exit or vice versa)?
- [ ] Are updates applied before measuring segment length?
- [ ] Active structure minimal (counter vs map vs tree) for needs?
