"""
Problem: https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75
"""

class Solution:
    def equalPairs(self, arr: List[List[int]]) -> int:
        rows = {}
        nr, nc = len(arr), len(arr[0])
        res = 0

        # iterate all rows
        for i in range(nr):
            # why "-" in join: [[11,1],[1,11]]
            row = "-".join([str(x) for x in arr[i]])
            rows[row] = rows.get(row, 0) + 1
        
        # iterate all columns and store matches with rows
        for j in range(nc):
            col = []
            for i in range(nc):
                col.append(str(arr[i][j]))
            col = "-".join(col)

            res += rows.get(col, 0)
        
        print(rows)
        return res
        
    11, 1
    1, 11