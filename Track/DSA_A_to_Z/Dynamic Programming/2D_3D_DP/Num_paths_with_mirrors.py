"""
Path with Mirrors: https://leetcode.com/problems/twisted-mirror-path-count/

-> When you hit a mirror you can move 2 directions
1) Enter RIGHT or LEFT: Exit DOWN
2) Enter DOWN or UP: Exit RIGHT
"""

from functools import cache
MOD = (10 ** 9 + 7)
class Solution:
    def uniquePaths(self, arr: List[List[int]]) -> int:
        nr,nc = len(arr), len(arr[0])
        
        @cache
        def solve(r,c,dir):
            if r<0 or c<0 or r>=nr or c>=nc:
                return 0
            if r==nr-1 and c==nc-1:
                return 1
            if arr[r][c] == 1: # If you came RIGHT, you will go DOWN
                return solve(r+1,c,"down") if dir=="right" else solve(r,c+1,"right")
            return solve(r + 1, c, "down") + solve(r, c + 1, "right")
        
        # solve.cache_clear() 
        return solve(0, 0, "right")%MOD