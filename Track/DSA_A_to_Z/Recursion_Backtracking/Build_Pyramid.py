"""
https://leetcode.com/problems/pyramid-transition-matrix/?envType=daily-question&envId=2025-12-29


MAIN PART:
- Core backtracking
- You can use same allowed pattern many times
"""
from collections import defaultdict
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        ways = defaultdict(set)
        for a,b,c in allowed: 
            ways[a+b].add(c)
        
        def solve(row: str, col: int, nextrow: str) -> bool:
            if len(row) == 1:
                return True
            
            # this row is complete
            if col == (len(row)-1):
                return solve(nextrow, 0, "")

            curpair = row[col:col+2]

            for nbr in ways[curpair]:
                nextrow += nbr # choose
                if solve(row, col+1, nextrow): # explore
                    return True
                nextrow = nextrow[:-1] # backtrack -> remove last one
            
            # no pairs found
            return False
        
        return solve(bottom, 0, "")