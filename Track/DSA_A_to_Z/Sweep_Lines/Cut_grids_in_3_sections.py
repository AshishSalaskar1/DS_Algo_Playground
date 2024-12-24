"""
PROBLEM: https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/description/

SOLUTION: Sweeplines

"""
class Solution:
    def check_cuts(self, events):
        cur_rectangles, cuts_left = 0, 3
        for time, incr in events:
            cur_rectangles += incr
            
            if incr == -1 and cur_rectangles == 0:
                cuts_left -= 1
            
            if cuts_left == 0:
                return True
        
        return False
                
            
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        h_events, v_events = [], []
        for xstart,ystart, xend, yend in rectangles:
            v_events.append((ystart, 1))
            v_events.append((yend, -1))
            h_events.append((xstart, 1))
            h_events.append((xend, -1))

        # In case of same time, pick the ends first (hence x[0],x[1] and not x[0],-x[1])
        v_events.sort(key=lambda x:(x[0],x[1]))
        h_events.sort(key=lambda x:(x[0],x[1]))
        
        return self.check_cuts(h_events) or self.check_cuts(v_events)
