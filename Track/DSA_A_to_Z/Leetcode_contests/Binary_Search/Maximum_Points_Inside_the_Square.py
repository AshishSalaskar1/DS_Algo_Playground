"""
Link: https://leetcode.com/problems/maximum-points-inside-the-square/description/

SOLUTION:
- BINARY SEARCH ON ANSWERS
- mid = length of square
- min: 0, max= max of abs of both x,y cordinates of all points
"""


class Solution:
    def is_possible(self, pts, hmap, sqlen):
        """
        How many pts can you place within square of len=sqlen
        -> -1 : you cant place (it has more than 1 type of points)
        """
        hst = set()
        for [x,y] in pts:
            if x>=-sqlen and x<=sqlen and y<=sqlen and y>=-sqlen:
                if hmap[(x,y)] in hst:
                    return -1
                hst.add(hmap[(x,y)])
        
        return len(hst)
                

            
        
    def maxPointsInsideSquare(self, pts: List[List[int]], s: str) -> int:
        hmap = {}
        maxsqlen = 0
        for i in range(len(pts)):
            x,y = pts[i][0],pts[i][1]
            maxsqlen = max(maxsqlen, max(abs(x), abs(y)))
            hmap[(x,y)] = s[i]
        
        lo, hi = 0, maxsqlen+1
        res = 0
        while lo<=hi:
            mid = lo+ (hi-lo)//2
            possible_pts = self.is_possible(pts, hmap, mid)
            if possible_pts != -1: # square was formed
                res = max(res, possible_pts)
                lo = mid+1
            else:
                hi = mid-1
        
        return res
                
            
#         for i in reversed(range(0,maxsqlen+1)):
#             possible_pts = self.is_possible(pts, hmap, i)
#             if possible_pts != -1:
#                 return possible_pts
            
        