# DP DOESNT WORK: https://leetcode.com/problems/shortest-path-in-binary-matrix/solutions/667137/why-does-dp-not-work/
# SIMPLE BFS (Given start to end) -> since length of path = nearest path = BFS with 8 directions
# BFS gives you shortest dist from src -> dest in terms of number of hops (which is what you need here). 

class Solution:
    def shortestPathBinaryMatrix(self, arr: List[List[int]]) -> int:
        nr, nc = len(arr), len(arr[0])
        src, dest = (0,0), (nr-1,nc-1)
        vis = set() # also add parent


        if arr[0][0] == 1 or arr[nr-1][nc-1]:
            return -1

        if nr==1 and nc==1:
            return 1

        q = [(src, 1)]

        while len(q) != 0:
            (ux,uy), udist = q.pop(0)
            

            dxs = [1,0,-1,0,-1,1,-1,1]
            dys = [0,1,0,-1,-1,-1,1,1]
            for dx, dy in zip(dxs, dys):
                vx = ux+dx
                vy = uy+dy

                if vx<nr and vy<nc and vx>=0 and vy>=0 and arr[vx][vy]==0 and (vx,vy) not in vis:
                    if (vx,vy) == dest:
                        return 1+udist
                    q.append(((vx,vy), 1+udist))
                    vis.add((vx,vy))
        
        return -1
        


            

                