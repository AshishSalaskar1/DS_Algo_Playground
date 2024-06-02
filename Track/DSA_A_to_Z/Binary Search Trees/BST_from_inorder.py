"""
PROBLEM: Construct BST from preoder

SOLUTON: 
preorder = [8,5,1,7,10,12]
- First element of PRE = ROOT
1. Root = (8) = [5,1,7,10,12]
    - split: first index where preorder[i] > root(8)
    - split index = 10 => [5,1,7 | 10, 12]
    - In some cases all can belong to left or right (init to len(preorder)) 
2. Left subtree : [5,1,7]
3. Right Subtree: [10, 12]


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, preorder: list[int]):
        if len(preorder) == 1: # only one node present
            return TreeNode(preorder[0])
        
        if len(preorder) == 0:
            return None

        node = TreeNode(preorder.pop(0)) # first node in PRE-ORDER= root

        first_greater = len(preorder) # why init to len (node=8, [1,2,3,4,5] => ALL WILL BELONG TO LEFT [1,2,3,4,5] and right will be [])
        for i in range(len(preorder)):
            if preorder[i] > node.val:
                first_greater = i
                break

        left_preorder = preorder[:first_greater]
        right_preorder = preorder[first_greater:]

        node.left = self.solve(left_preorder)
        node.right = self.solve(right_preorder)

        return node




    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.solve(preorder)
        