"""
PROBLEM: https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/
SOLUTION: https://www.youtube.com/watch?v=JHIhlzdMFdY

LOGIC:
- IMP: SUM(row_sums) = SUM(col_sums) -> thats why this approach works
- At each step set value = min(rsum[r],csum[c]) => because if u pick larger one the ele > that sum [VIOLATES]
    1. If you set it with col, this col is done move to next col (Update rsums)
    2. If you set it with row, this row is done move to next row (Update csums)
- Why update csums, rsum? Once you set it contributes to both rsum and csum. 
    One of these is 0 (gets fulfilled) but other one can be used later (filled up later)
"""
class Solution:
    def restoreMatrix(self, row_sums: list[int], col_sums: list[int]) -> list[list[int]]:
        nr, nc = len(row_sums), len(col_sums)
        arr = [[0 for _ in range(nc)] for _ in range(nr)]

        r,c = 0,0
        while r<nr and c<nc:
            minval = min(row_sums[r], col_sums[c])
            arr[r][c] = minval

            row_sums[r] -= minval
            col_sums[c] -= minval

            if col_sums[c] == 0: # you picked this col -> no need to check for col -> move to next col
                c += 1
            else: # you picked this row -> move to next row
                r += 1
        
        return arr




        