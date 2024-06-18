"""
PROBLEM: Maximum Level Sum of a Binary Tree
https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = [root]
        lvl = 1
        lvl_sums = []

        while len(q) != 0:
            lsum = 0
            for _ in range(len(q)):
                node = q.pop(0)
                lsum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            lvl_sums.append((lvl, lsum))
            lvl += 1
        
        # if lvls have equal maximum_sums return the smallest lvl
        lvl_sums = sorted(lvl_sums, key=lambda x:(x[1],x[0]))

        while len(lvl_sums)>1 and lvl_sums[-1][1] == lvl_sums[-2][1]:
            lvl_sums.pop()
        
        return lvl_sums[-1][0]
        
            
        