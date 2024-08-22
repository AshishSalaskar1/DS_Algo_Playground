"""
PROBLEM: https://leetcode.com/problems/sudoku-solver

SOLUTION:
- solve() method
    - Iterate all (r,c) pairs, and wherever u see a "."
    - Try filling 1-9 in (r,c)
        - is_valid_placement(r,c,1-9) is True:
            board[r][c] = 1-9
            sovle(board)
            board[r][c] = "." # BACKTRACK
    - If you cant fill anything in this "." -> RETURN FALSE
- Return True


- CHECK VALID MOVE
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
class Solution:
    def is_valid_placement(self, board: List[List[str]],  r: int, c: int, val: str) -> bool:
        k = int(math.sqrt(self.nr)) # r=9, each smaller square = 3

        # check column
        for i in range(self.nr):
            if board[i][c] == val:
                return False

        # check row
        for j in range(self.nc):
            if board[r][j] == val:
                return False

        # check inner square of kxk
        rstart, cstart = r//k * k, c//k * k
        for i in range(rstart, rstart+k):
            for j in range(cstart, cstart+k):
                if board[i][j] == val:
                    return False
        
        return True
    
    def solve(self, board: List[List[str]]) -> bool:

        for i in range(self.nr):
            for j in range(self.nr):
                if board[i][j] == ".":
                    for x in range(1,10):
                        if self.is_valid_placement(board, i, j, str(x)):
                            board[i][j] = str(x)
                            if self.solve(board):
                                return True
                            
                            board[i][j] = "." 
                    return False
                    
        
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.nr, self.nc = len(board), len(board[0])
        self.solve(board)