from collections import defaultdict
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        events = defaultdict(list)
        for start,end,seats in bookings:
            events[start].append(seats)
            events[end+1].append(-seats)
        
        res = []
        nseats = 0
        for i in range(1,n+1):
            for seats in events[i]:
                nseats += seats
            res.append(nseats)
        
        return res

        