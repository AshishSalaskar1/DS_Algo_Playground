"""
Problem: 
- Given a grid, check if grid contains the given word
- You can move in 4 directions

SOLUTION: Backtracking
- function solve(i,j,word_idx):
    - You are at arr[i][j], and you matched word[:word_idx] chars already
    - Now, (i,j) should be valid, not visited and arr[i][j] == word[word_idx]
        - Since you have already found word_idx-1 chars, next needed would be word_idx index
    - Visit all 4 directions + BACKTRACK
"""
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


        