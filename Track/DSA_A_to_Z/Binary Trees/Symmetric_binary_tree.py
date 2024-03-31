# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
INTUITION:
    - for each node its subtrees must be symmetrical
    - VAL(curr.left) == VAL(curr.right)

"""

class Solution:
    def solve(self, n1: TreeNode, n2: TreeNode):
        if n1 is None and n2 is None:
            return True
        if n1 is None or n2 is None:
            return False

        return n1.val == n2.val and self.solve(n1.left, n2.right) and self.solve(n1.right, n2.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self.solve(root.left, root.right)
        


        
        