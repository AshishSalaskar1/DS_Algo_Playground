"""
VALIDATE BST

SOL 2:
- INORDER of BST == Sorted (LNR)

SOL 2: LEFT and RIGHT BOUND APPROACH
- Logically if you see each node in BST divides its subtrees such that it follows certain bounds
- Imagine initially the bounds are [-inf, +inf]
     (2) [-inf, inf]
   /     \ 
 (1)     (3)
- Now (2) here divides into 2 subtrees
    - Left subtree will have values within [-inf, 2]
    - Right subtree will have values within [2,inf]



"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solveBounds(self, node, lbound, rbound) -> bool:
        if node is None:
            return True

        # goes out of bounds - invalid BST
        if node.val >= rbound or node.val <= lbound:
            return False
        
        # update bounds for Left and right subtrees
        return self.solveBounds(node.left, lbound, node.val) and self.solveBounds(node.right, node.val, rbound)

    def isValidBSTBounds(self, root: Optional[TreeNode]) -> bool:
        return self.solveBounds(root, float("-inf"), float("inf"))
    
    def inorder(self, node):
        if node is None:
            return 
        
        self.inorder(node.left)
        self.res.append(node.val)
        self.inorder(node.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.res = []
        self.inorder(root)
        print(self.res)
        return self.res == sorted(set(self.res)) # WHY SET: [2,2,2] is an edge CASE



        
