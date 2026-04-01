"""
https://leetcode.com/problems/robot-collisions/?envType=daily-question&envId=2026-04-01
5  4  3  2  1
2 17  9  15 10
R R.  R. R.  R


1 2  3 4  5 
2 17 9 15 10


3  5  2  6
10 10 15 12
R  L. R. L

R.  R.  L.  L
2   3   4   6
15. 10. 10 12
"""
class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        vals = [(x,y,z,i) for i, (x, y, z) in enumerate(zip(positions, healths, directions))]
        vals = sorted(vals)
        # vals = sorted([[x, y, z, i] for i, (x, y, z) in enumerate(zip(positions, healths, directions))])
        
        lstk, rstk = [], []
        
        for pos, wt, d, i in vals:
            if d == "R":
                rstk.append([pos, wt, d, i])
            else:
                alive = True
                
                while rstk:
                    if rstk[-1][1] == wt:
                        rstk.pop()
                        alive = False
                        break
                    elif rstk[-1][1] > wt:
                        rstk[-1][1] -= 1
                        alive = False
                        break
                    else:
                        rstk.pop()
                        wt -= 1
                
                if alive:
                    lstk.append([pos, wt, d, i])
        
        res = lstk + rstk
        res.sort(key=lambda x: x[-1])
        
        return [x[1] for x in res]
        



        