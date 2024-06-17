"""
PROBLEM: Longest ZigZag Path in a Binary Tree
https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree

SOLUTION:
- Maintain 3 vars: node, cur_len, prev_dir
1) if prev_dir == "left" (which previously you took left to reach here)
    - Move LEFT -> cur_len=1 (reset from here),  prev_dir="left"
    - Move RIGHT -> cur_len++ (valid zigzag path), prev_dir="right"
2) if prev_dir == "right" (you reached this point by taking right)
    - Move LEFT -> cur_len++ (valid zigzag path),  prev_dir="left"
    - Move RIGHT -> cur_len=1 (reset from here), prev_dir="right"
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def solve(self, node: TreeNode, cur_len: int, prev_dir: str) -> None:
        if node is None:
            return

        self.res = max(self.res, cur_len)
        
        if prev_dir == "right":
            self.solve(node.left, cur_len+1, "left")
            self.solve(node.right, 1, "right")
        else:
            self.solve(node.right, cur_len+1, "right")
            self.solve(node.left, 1, "left")
        
        return

        
        
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.solve(root.right, 1, "right")
        self.solve(root.left, 1, "left")

        return self.res