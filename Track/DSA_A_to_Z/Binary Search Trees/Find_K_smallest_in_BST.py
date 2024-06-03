"""
PROBLEM: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
Find Kth smallest element in BST

SOLUTION: Inorder Traversal -> kth entry will be the K smallest
- O(N): find all inorder and then get inorder[k-1]
- O(height): stop inserting into inorder as soon as it has `k` items

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root) -> None:
        if root is None or len(self.res) == self.k:
            return

        self.inorder(root.left)
        if len(self.res) < self.k:
            self.res.append(root.val)
        self.inorder(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = []
        self.k = k
        self.inorder(root)

        return self.res[-1]
        