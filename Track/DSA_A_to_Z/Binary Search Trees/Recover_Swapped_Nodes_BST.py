"""
PROBLEM: https://leetcode.com/problems/recover-binary-search-tree/
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

INTUTION:
- Only 2 nodes are swapped. There may be 2 cases in this
[1,2,3,4,5]

Voilation: When inserting into INORDER the cur ele < last element in inorder

Case 1) ADJACENT NODES SWAPPED - 1 VIOLATION 
=> [1,(3),(2),4,5] => You get 1 VIOLATION
- Here you just swap (3)<->(2)

Case 2) NON-ADJACENT NODES SWAPPED - 2 VIOLATION
=> [1,(4),3,2,(5)] => You get 2 VIOLATIIONS
- Here you swap (4)<->(5)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, node):
        if node is None:
            return

        self.solve(node.left)

        if self.prev and node.val < self.prev.val:
            if self.first is None: # first voilation
                self.first = self.prev
                self.middle = node
            else: # second voilation
                self.last = node

        self.prev = node
        self.solve(node.right)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first, self.last, self.middle = None, None, None
        self.prev = None
        self.solve(root)

        if self.last is None: # only voilation - together swap
            self.first.val, self.middle.val = self.middle.val, self.first.val
        else: # 2 violations => not together
            self.first.val, self.last.val = self.last.val,self.first.val

        return root
        