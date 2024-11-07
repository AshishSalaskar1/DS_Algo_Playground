# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def indfs(self, node):
        if node is None:    return

        # CONSIDER THIS IS LEAF - BASE CASE
        self.dp[node] = {
            1: node.val,
            0: 0
        }

        childs = [node.left, node.right]
        for child in [x for x in childs if x is not None]:
            self.indfs(child) # Let recursion do its thing n fill up child dpt table
            self.dp[node][1] += self.dp[child][0]
            self.dp[node][0] += max(self.dp[child][0],self.dp[child][1])

    def rob(self, root: Optional[TreeNode]) -> int:
        self.dp = {}
        self.indfs(root)

        return max(
            self.dp[root][0],
            self.dp[root][1]
        )
        