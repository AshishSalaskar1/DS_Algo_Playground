"""
PROBLEM: https://leetcode.com/problems/rectangle-area-ii/

SOLUTION: Sweep Lines on Horizontal + Vertical
YT Video: https://www.youtube.com/watch?v=xm5-u_l8tTY


INTUITION:
- HORIZONTAL SWEEP LINE: Will find you CUR_X and PREV_X (assume X_left and X_right) => this gives you width
- VERTICAL SWEEP LINE: This will give you the height of each segments which you can multiply with WIDTH to get area
- Both of these intervals to be sorted, horizontal is done once since its stable. Vertical intervals get added/removed hence sort it each time

WHY use 0 for prev_h and prev_v?
- In this case wkt x,y >= 0, that means all rectangles lie on positive x,y axis
- If -inf <= x,y <= inf , then you would have initialized by -inf for both prev_h and prev_v

NOTES:
- You add x1,x2 into h_intervals along with open and close. While sorting you need to make sure that open comes before close. (Hence, 2nd param = O for open and 1 for close)
- When you see start of x_range, append its height y1,y2 to v_intervals => SORT
- When you see end of x_range, remove its height y1,y2 from v_intervals 
- But both these add/remove operations you do after calculating AREA
"""
MOD = 10**9+7

class Solution:
    def get_vertical_area(self, h_width):
        area = 0
        prev_v_boundary = 0
        
        for l,r in self.v_intervals:
            # you need overlapping area: prev=1, cur=[3,5], you need [3,5] n not [1,5]
            prev_v_boundary = max(prev_v_boundary, l) 
            cur_interval_area = (r-prev_v_boundary)*h_width
            if cur_interval_area > 0:
                area += cur_interval_area % MOD

            prev_v_boundary = max(prev_v_boundary, r)
        
        return area

    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        
        h_events = []
        for x1,y1,x2,y2 in rectangles:
            h_events.append( (x1, 0, y1, y2) )
            h_events.append( (x2, 1, y1, y2) )
        
        h_events = sorted(h_events)
        total_area = 0
        self.v_intervals = []
        prev_h_boundary = 0
        for x1, close, y1, y2 in h_events:
            h_width = x1-prev_h_boundary
            # print(x1, total_area)
            total_area += self.get_vertical_area(h_width) % MOD
            # print(x1, total_area)

            if close == 1: # this rectangle closes here
                self.v_intervals.remove((y1,y2))
            else: # this rectangle starts here -> includes its y-width for further calculations
                self.v_intervals.append((y1,y2))
                self.v_intervals = sorted(self.v_intervals)
            
            prev_h_boundary = x1


        return total_area % MOD


        