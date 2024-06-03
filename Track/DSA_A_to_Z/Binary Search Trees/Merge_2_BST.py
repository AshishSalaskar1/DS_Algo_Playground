
"""
merge 2 BST
"""
class Solution:
    def mergeTrees(self, root1, root2):
        if not root1:
            return root2
        if not root2:
            return root1
        
        root1.val += root2.val
        root1.left = self.mergeTrees(root2.left, root1.left)
        root1.right = self.mergeTrees(root2.right, root1.right)
        
        return root1