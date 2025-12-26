"""
PROBLEM: https://leetcode.com/problems/minimum-penalty-for-a-shop/description
[Minimise Ns]  x  [Minimise Ys]
"""
class Solution:
    def bestClosingTime(self, arr: str) -> int:
        n = len(arr)
        yc, nc = [0]*n, [0]*n

        ycount, ncount = 0,0
        for i in range(n):
            if arr[i] == "N": ncount += 1
            nc[i] = ncount
        for i in range(n-1,-1,-1):
            if arr[i] == "Y": ycount += 1
            yc[i] = ycount

         
        pos, minpenalty = -1, float("inf")
        for i in range(n):
            ncount = nc[i-1] if i>0 else 0
            ycount = yc[i]

            penalty = ncount + ycount
            if penalty < minpenalty:
                minpenalty = penalty
                pos = i
        
        # special check -> close at the end after all customers
        if nc[-1] < minpenalty: pos = n

        return pos
