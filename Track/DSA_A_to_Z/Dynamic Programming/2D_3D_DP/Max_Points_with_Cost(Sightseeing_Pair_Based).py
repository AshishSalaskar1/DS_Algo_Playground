"""
PROBLEM: https://leetcode.com/problems/maximum-number-of-points-with-cost/?envType=daily-question&envId=2024-08-17

SOLUTION:
Video: https://www.youtube.com/watch?v=lk7WUhAwYGA

Combimation of 2 problems:  
    1. Min falling sum: https://leetcode.com/problems/minimum-falling-path-sum/
    2. Best sightseeing pair: https://leetcode.com/problems/best-sightseeing-pair/description/
       - In this you find arr[i] + arr[j] + (i-j) and j>i always


CONDITION: a[i] + a[j] - abs(i-j) 

CASE i>j:
    a[i] + a[j] - (i-j) = a[i] + a[j] - i + j = (a[i]-i) + (a[j]+j)
CASE i<j
    a[i] + a[j] - (j-i) = a[i] + a[j] - j + i = (a[i]+i) + (a[j]-j)


The key idea is to leverage the following:

Case 1: If you move from a cell `i` in row `r-1` to a cell `j` in row `r` where i > j:
        Score = (a[i]-i) + (a[j]+j)

Case 2: If you move from a cell `i` in row `r-1` to a cell `j` in row `r` where i < j:
        Score =  (a[i]+i) + (a[j]-j)

The above formulas suggest that the problem can be broken down into two parts:

Maximizing a[i] + i for all i when moving left to right (left max array).
Maximizing a[i] - i for all i when moving right to left (right max array).
"""

class Solution:

    def maxPoints(self, arr: List[List[int]]) -> int:
        nr, nc = len(arr), len(arr[0])

        prev = arr[0]
        for r in range(1, nr):
            lmax, rmax = [0]*nc, [0]*nc

            # lmax array -> Maximise arr[i]+i going L->R
            lmax[0] = prev[0]
            for i in range(1, nc):
                lmax[i] = max(lmax[i-1], prev[i]+i)

            # rmax array -> Maximise arr[i]-i going from R<-L
            rmax[-1] = prev[-1] - (nc-1)
            for i in reversed(range(0, nc-1)):
                rmax[i] = max(rmax[i+1], prev[i]-i)
            
            # update both option in current row
            for c in range(nc):
                # res = cur + best of left or right (consider `i` is prev_row idx, `c` is current row idx)
                # `i` is already maimized, now `c` or `j` needs to be maximized
                prev[c] = arr[r][c] + max(
                    rmax[c] + c, # (a[i]-i) + (a[j]+j)
                    lmax[c] - c  # (a[i]+i) + (a[j]-j)
                )
    
        return max(prev)


        