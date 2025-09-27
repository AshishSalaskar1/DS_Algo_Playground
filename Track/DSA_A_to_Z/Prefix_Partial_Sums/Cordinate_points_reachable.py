"""
Link: https://leetcode.com/contest/biweekly-contest-166/problems/distinct-points-reachable-after-substring-removal/


LOGIC: Prefix sum on sequence

- Step 1: Iterate all the paths and generate positions
- Step 2: 
    - When you remove a subset of points, that basically means you are removing/discarding the distance travelled in that path
    - OR: from destination point, you substract the (x,y) that was travelled in this subset
    - EX: dest=(xdest,ydest), subset = [i...j] = (xstart,ystart) -> (xend, yend) 
    - Delta path taken that you need to remove = (xend, yend)  -  (xstart,ystart)
    - FINAL POINT after removing this subset = =(xdest,ydest)- [(xend, yend)  -  (xstart,ystart)]
"""
class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        steps = [[0,0]]

        for i, ch in enumerate(s):
            steps.append(steps[-1].copy())
            if ch == "U": steps[-1][1] += 1
            elif ch == "D": steps[-1][1] -= 1
            elif ch == "L": steps[-1][0] -= 1
            elif ch == "R": steps[-1][0] += 1

        final = steps[-1]
        res = set()

        for i in range(len(s)-k+1):
            xdelta = steps[i+k][0] - steps[i][0]
            ydelta = steps[i+k][1] - steps[i][1]
            res.add((final[0]-xdelta, final[1]-ydelta))

        return len(res)
            
        