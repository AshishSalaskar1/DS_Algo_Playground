"""
Problem:  https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
Same as: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/submissions/1598730999/


ALGORITHM
- At each step return Depth, LCA of that subtree rooted at current node
1. If node is None -> depth=0, lca=None
2. if left.depth > right.depth 
    - Then this node is definitely not LCA
    - depth = left.depth+1, LCA = left.LCA
3. If right.depth > left.depth 
    - Then this node is definitely not LCA
    - depth = right.depth+1, LCA = right.LCA
4. if left.depth == right.depth:
    - Means this nodes is at equal distant from both Deepest nodes -> hence this is a LCA of both node
    - depth = right|left.depth+1, LCA = node
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if root is None:
            return {
                "depth": 0,
                "lca": None
            }

        left = self.solve(root.left)
        right = self.solve(root.right)

        if left["depth"] > right["depth"]:
            return {"depth": 1+left["depth"], "lca": left["lca"]}
        elif right["depth"] > left["depth"]:
            return {"depth": 1+right["depth"], "lca": right["lca"]}
        else:
            return {"depth": 1+left["depth"], "lca": root }

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = self.solve(root)
        return res["lca"]
        