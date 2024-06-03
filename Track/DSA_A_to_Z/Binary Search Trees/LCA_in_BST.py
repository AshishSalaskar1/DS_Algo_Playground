"""
Normal BT LCA: You have to iterate both subtrees
In BST: There will be only point where split happens [GIVEN BOTH NODES EXIST]
- Split: one node lies in Right Subtree and another in left subtree 

- For each node you have 3 decisions to make where p,q lies based on value
1. p,q lie in left tree -> search only in left
2. p,q lie in right tree -> search only in right
3. p lies left, q lies right (vice versa) -> SPLIT LINE FOUND
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def LCA(self, node, p, q):
        if node is None:
            return None

        if node.val > p.val and node.val > q.val:
            return self.LCA(node.left, p, q)
        elif node.val < p.val and node.val < q.val:
            return self.LCA(node.right, p, q)
        else: # SPLIT POINT 
            return node
    


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.LCA(root, p, q)



        