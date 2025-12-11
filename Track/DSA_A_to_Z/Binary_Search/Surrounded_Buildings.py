"""
https://leetcode.com/problems/count-covered-buildings/description/?envType=daily-question&envId=2025-12-11

SIMPLE IDEA
- if you are at (curx,cury) -> you check these 2 things
1. There is some x < curx and some x > curx
2. There is some y < cury and some y > cury
"""
from collections import defaultdict
import bisect
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        rmap, cmap = defaultdict(list), defaultdict(list)

        for r,c in buildings:
            rmap[r].append(c)
            cmap[c].append(r)

        res = 0
        for x,y in buildings:
            yaxis_points, xaxis_points = sorted(rmap[x]), sorted(cmap[y])

            # check top bottom - if there are `y`s before and after `cur_y`
            yaxis_check = bisect.bisect_left(yaxis_points, y)

            # check left right - if there are `x`s before and after `cur_x`
            xaxis_check = bisect.bisect_left(xaxis_points, x)

            if 0<yaxis_check<(len(yaxis_points)-1 )and 0<xaxis_check<(len(xaxis_points)-1):
                res += 1

        return res
