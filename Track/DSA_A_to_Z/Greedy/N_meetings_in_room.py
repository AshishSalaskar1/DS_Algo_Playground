"""
PROBLEM: 
There is one meeting room in a firm.
There are N meetings in the form of (start[i], end[i]) where start[i] is start time of meeting i and end[i] is finish time of meeting i.
What is the maximum number of meetings that can be accommodated in the meeting room when only one meeting can be held in the meeting room at a particular time?

Note: Start time of one chosen meeting can't be equal to the end time of the other chosen meeting.

SOLUTION:
GREEDY -> You need the meeting that ends first so that you can finish earlier and start more meetings

"""
class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        meetings = list(zip(start, end))
        meets = sorted(meetings, key=lambda x:x[1])
        
        # consider first meet is already picked
        last_end = meets[0][1]
        res = 1
        
        for meet in meets[1:]:
            if meet[0] > last_end: # pick if it can be scheduled
                last_end = meet[1]
                res += 1
            # dont pick otherwise
        
        return res
        