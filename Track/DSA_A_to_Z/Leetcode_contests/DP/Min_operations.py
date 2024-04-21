"""
Link: https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/description/

Greedy wont work -> DP NEEDS TO BE DONE
 
INTUITIONS
- You can only fill numbers 0-9
- Each ele must be equal to ele below it also -> means whole col has same number
- Since each row has same number, the next col cant have the same number as filled in the current col
- No of replacement needed in cur_row by filling X(0-9) = num_of_rows - (num_times element X occured in row:cur_row )

SOLUTION
- DP inputs -> prev_filled_val, cur_col
- Try filling 0-9 except prev_filled in cur_col and then pick it + pass it to next row
"""

class Solution:
    
    def solve(self, col, prev, freq, nr, nc):
        idx = (col, prev)

        if idx in self.dp:
            return self.dp[idx]

        if col >= nc:
            return 0

        min_repl = float("inf")
        for x in range(10):
            if x!=prev:
                min_repl = min(
                    min_repl,
                    (nr-freq[col][x]) + self.solve(col+1, x, freq, nr, nc) 
                )
        
        self.dp[idx] = min_repl
        return min_repl


    def minimumOperations(self, arr: List[List[int]]) -> int:
        self.dp = {}
        nr, nc = len(arr), len(arr[0])
        freq = [[0 for _ in range(10)] for _ in range(nc)] # freq[col_num][0-9]

        for row in range(nr):
            for col in range(nc):
                freq[col][arr[row][col]] += 1 

        res = self.solve(0, -1, freq, nr, nc)
        return res





        