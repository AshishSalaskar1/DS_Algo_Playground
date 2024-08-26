
from typing import List
import math

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



sol = Solution()


board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
output = [
    ["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"]
]

sol.solveSudoku(board)
print(*board, sep="\n")

