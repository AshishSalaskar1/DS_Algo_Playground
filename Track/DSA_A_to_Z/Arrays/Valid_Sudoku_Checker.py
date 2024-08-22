"""
PROBLEM: https://leetcode.com/problems/valid-sudoku/?envType=study-plan-v2&envId=top-interview-150
- Only check if valid or not - NO NEED TO FILL

SOLUTION:
- For each (r,c) you need that the same number doesnt exist in 3 ways
    1. Vertical column
    2. Horizontal Row
    3. Sub-Square

-> Finding start and end of sub-square
- If the no of rows/cols = N, then len of square is sqrt(N) [9 -> 3]
- let k = len of sub-square

row_start = (i//k) * k
col_start = (j//k) * k

row_end = row_start + k
col_start = col_start + k

"""

from typing import List
import math

class Solution:
    def check_is_valid(self, r: int, c: int) -> bool:
        k = int(math.sqrt(self.nr)) # r=9, each smaller square = 3

        # check column
        for i in range(self.nr):
            if i!=r and self.board[i][c] == self.board[r][c]:
                return False

        # check row
        for j in range(self.nc):
            if j!=c and self.board[r][j] == self.board[r][c]:
                return False

        # check inner square of kxk
        rstart, cstart = r//k * k, c//k * k
        for i in range(rstart, rstart+k):
            for j in range(cstart, cstart+k):
                if (i,j) != (r,c) and self.board[i][j] == self.board[r][c]:
                    return False
        
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.board = board
        self.nr, self.nc = len(board), len(board[0])
        print(*board,sep="\n" )


        for i in range(self.nr):
            for j in range(self.nc):
                if self.board[i][j] != ".":
                    if self.check_is_valid(i, j) is False:
                        print(i,j)
                        return False

            
        return True