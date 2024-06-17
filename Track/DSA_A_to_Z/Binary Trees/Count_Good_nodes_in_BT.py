"""
PROBLEM: Count Good Nodes in Binary Tree
https://leetcode.com/problems/count-good-nodes-in-binary-tree/?envType=study-plan-v2&envId=leetcode-75

SOLUTION:
- Maintain max_till_now_in_path and then just iterate 
"""
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def solve(self, node: TreeNode, max_in_path: int = float("-inf")) -> int:
        if node is None:
            return
        
        if node.val >= max_in_path:
            self.res += 1
        
        new_max_in_path = max(max_in_path, node.val)
        self.solve(node.left, new_max_in_path)
        self.solve(node.right, new_max_in_path)
        
        return
        


    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        self.solve(root)

        return self.res
        