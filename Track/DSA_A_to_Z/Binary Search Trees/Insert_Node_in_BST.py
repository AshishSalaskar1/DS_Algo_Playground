# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, val):
        if root is None:
            return 
        
        if val < root.val:
            lres = self.solve(root.left, val)
            if lres is None:
                root.left = TreeNode(val)
            return root
        else:
            rres = self.solve(root.right, val)
            if rres is None:
                root.right = TreeNode(val)
            return root
        



    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
            
        prev = None
        cur = root

        while cur:
            prev = cur
            if val < cur.val: # move left
                cur = cur.left
            else: # move right
                cur = cur.right

        # now cur has become None -> prev points to node where to insert
        # but u need to decide left or right
        if val < prev.val:
            prev.left=TreeNode(val)
        else:
            prev.right = TreeNode(val)

        return root