# Recursion & Backtracking Cheatsheet

Patterns in this repo (verbatim snippets)
- N-Queens placement/backtrack
- Word Search DFS backtracking
- Combination Sum (re-use allowed)
- Combination Sum II (unique, single-use each, sorted + skip dups)
- Palindrome Partitioning (front partition + backtrack)
- Sudoku Solver (fill '.', validate rows/cols/subgrid)

N-Queens (from Recursion_Backtracking/N_Queens.py)
```python
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
```

Word Search (from Recursion_Backtracking/Word_Search.py)
```python
class Solution:
    def solve(self, i:int, j:int, word_index: str) -> bool:
        if word_index == len(self.word): # you have already found n chars same
            return True
        
        if i<0 or j<0 or i>=self.nr or j>=self.nc or (i,j) in self.vis or self.arr[i][j] != self.word[word_index]:
            return False

        self.vis.add((i,j)) # mark this as visited

        top = self.solve(i-1, j, word_index+1)
        right = self.solve(i, j+1, word_index+1)
        left = self.solve(i, j-1, word_index+1)
        down = self.solve(i+1, j, word_index+1)

        self.vis.remove((i,j)) # backtrack -> since you have explored all paths

        return top or down or right or left
        

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.arr = board
        self.nr = len(board)
        self.nc = len(board[0])
        self.word = word

        self.vis = set()
        for i in range(self.nr):
            for j in range(self.nc):
                if self.arr[i][j] == word[0]:
                    if self.solve(i,j,0):
                        return True
        
        return False
```

Combination Sum (from Recursion_Backtracking/Combination_Sum.py)
```python
class Solution:
    def findCombination(self, ind: int, target: int):
        if ind == len(self.candidates):
            if target == 0:
                self.ans.append(self.ds[:])
            return

        # PICK -> if possible + BACKTRACK PICKED ONE FROM PICKED_ELEMENTS
        if self.candidates[ind] <= target: # you can pick the ele
            self.ds.append(self.candidates[ind])
            self.findCombination(ind, target - self.candidates[ind]) # you can pick same again
            self.ds.pop()
        # DONT PICK
        self.findCombination(ind + 1, target)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.ds = []
        self.candidates = candidates
        self.target = target
       
        self.findCombination(0, target)
        return self.ans
```

Combination Sum II (from Recursion_Backtracking/Combination_Sum_2.py)
```python
class Solution:
    def solve(self, i, target, res):
        if target == 0:
            self.ans.append(res.copy())
            return 
        
        for next_pick in range(i, len(self.arr)):
            if next_pick > i and self.arr[next_pick] == self.arr[next_pick-1]:
                continue
            if self.arr[next_pick] > target:
                break
            res.append(self.arr[next_pick])
            self.solve(next_pick+1, target-self.arr[next_pick], res)
            res.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.arr = sorted(candidates)
        self.ans = []
        self.solve(0,target, [])
        return self.ans
```

Palindrome Partitioning (from Recursion_Backtracking/Palindrome_Partitioning.py)
```python
def ispal(s):
    return s == s[::-1]

class Solution:
    def solve(self, i:int):
        if i == len(self.s): # you have partitioned everything
            self.res.append(self.path.copy())
        
        # try to make all possible palindromes starting from i (including i)
        for end in range(i, len(self.s)):
            new_str = self.s[i:end+1]
            if ispal(new_str):
                self.path.append(new_str)
                self.solve(end+1)
                self.path.pop()

    def partition(self, s: str) -> List[List[str]]:
        self.s = s
        self.path = []
        self.res = []

        self.solve(0)
        return self.res
```

Sudoku Solver (from Recursion_Backtracking/Soduku_Solver.py)
```python
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
```

---

## 🗺️ Quick map
- 🌿 Subsets/combinations/permutations
- ♟️ N-Queens / Sudoku / Partitioning
- 🚫 Constraints pruning (validity checks)

## ✅ Study checklist
- [ ] Base case returns and result capture correct?
- [ ] Choose → explore → unchoose (undo) steps present?
- [ ] Pruning/validity checks placed before deeper recursion?
- [ ] Avoid global state leaks between branches.
