class Solution:
    def can_place(self, row: int, col:int,  board: list[list[str]]) -> list[int]:
        # CAN you place a queen at arr[ROW][COL]
        # check top
        for i in range(0, row):
            if board[i][col] == "Q":
                return False

        # check top-right diagonals
        i,j = row,col
        while i>=0 and j>=0 and i<self.nr and j<self.nc:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        # check top-left diagonals
        i,j = row,col
        while i>=0 and j>=0 and i<self.nr and j<self.nc:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        return True

    def solve(self, row: int, board: list[list[str]]):
        if row == self.nr:
            res_board = ["".join(x) for x in board]
            self.res.append(res_board)
        for col in range(0, self.nc):
            if self.can_place(row, col, board):
                board[row][col] = "Q" # you placed a QUEEN HERE
                self.solve(row+1, board)
                board[row][col] = "." # BACKTRACK -> remove queen to see other ways

    def solveNQueens(self, n: int) -> list[list[str]]:
        self.nr, self.nc = n, n
        board = [["." for _ in range(n)] for _ in range(n)]
        self.res = []

        self.solve(0, board)
        return self.res