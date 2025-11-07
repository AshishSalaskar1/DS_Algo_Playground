"""
Problem: Separate Squares I
Link: https://leetcode.com/problems/separate-squares-i/

"""

class Solution:
    def does_split_half(self, ylines, y):
        larea, rarea = 0,0

        for start, end in ylines:
            side = end-start
            # does overlap the middle
            if start<=y<=end: # it splits
                larea += (y-start)**2
                rarea += (end-y)**2
            elif y>end: # left side
                larea += side**2
            else:
                rarea += side**2

        return rarea, larea
        
    def separateSquares(self, squares: List[List[int]]) -> float:
        
        ylines = []
        max_y = 0
        for x,y,side in squares:
            max_y = max(max_y, y+side)
            ylines.append((y,y+side))

        low, high = 0, max_y
        while high - low > 1e-6:
            mid = (low + high) / 2
            above, below = self.does_split_half(ylines, mid)
            if above > below:
                low = mid
            else:
                high = mid
    
        return low
                
            