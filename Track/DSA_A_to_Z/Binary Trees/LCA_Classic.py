"""
ASSUMPTIONS
1. The tree always has these nodes
2. You dont need the path or anything else

SOME CONSIDERATIONS:
1. Whenever you see that cur_node is either p,q you just return that node.
At the end this node gets returned (Ideally it might be the case that cur_node is `p` but `q` is in child subtree)

BETTER SOLUTION: BINARY LIFTING
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:

    def solve(self, root: TreeNode, p, q):
        if root is None or root.data in set([p.data,q.data]):
            return root
        
        left, right = self.solve(root.left,p,q), self.solve(root.right,p,q)
        
        if left is None:
            return right
        elif right is None:
            return left
        else: # Both left and right are not null, we found our result
            return root

    def lowestCommonAncestor(self, root, p, q):
        # print(type(p))
        self.res = None
        return self.solve(root, p,q)
        # return root
        # return self.res if self.res else root
