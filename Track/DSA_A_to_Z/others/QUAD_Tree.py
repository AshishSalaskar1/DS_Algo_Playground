"""
LEETCODE LINK: https://leetcode.com/problems/construct-quad-tree/description/

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

"""

# generate code snipper for QUAD tree


class Solution:
    def check_leaf(self, grid):
        val = grid[0][0]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != val:
                    return False
        
        return True

    def construct(self, grid: List[List[int]]) -> 'Node':
        

        if grid is None:
            return None
        
        if self.check_leaf(grid):
            return Node(grid[0][0] == 1, True, None, None, None, None)

        n = len(grid)
        return Node(
            '*',
            False,
            self.construct([row[:n//2] for row in grid[:n//2]]),
            self.construct([row[n//2:] for row in grid[:n//2]]),
            self.construct([row[:n//2] for row in grid[n//2:]]),
            self.construct([row[n//2:] for row in grid[n//2:]])
        )