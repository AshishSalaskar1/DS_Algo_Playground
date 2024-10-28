"""
PROBLEM: https://leetcode.com/problems/my-calendar-ii/description/

SOLUTION: Line Sweep Each time

VERY BAD TIMECOMPLEXITY = but can be done via line sweep

O(Q * NLog(n) + n )
"""
class MyCalendarTwo:

    def __init__(self):
        self.events = []

    def book(self, start_time: int, end_time: int) -> bool:
        self.events.append((start_time, 1))
        self.events.append((end_time, -1))
        self.events.sort()

        cur_events = 0
        for i in range(len(self.events)):
            cur_events += self.events[i][1]
            if cur_events >= 3:
                self.events.remove((start_time, 1))
                self.events.remove((end_time, -1))
                return False
        
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)