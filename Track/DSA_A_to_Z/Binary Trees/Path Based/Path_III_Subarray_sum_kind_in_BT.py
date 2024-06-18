"""
PROBLEM: PATH III - Subarray Path Sum
https://leetcode.com/problems/path-sum-iii

SOLUTION:
- https://leetcode.com/problems/path-sum-iii/solutions/141424/python-step-by-step-walk-through-easy-to-understand-two-solutions-comparison

INTUITION
=> This is similar like finding subarray sum in array
    - You maintain all sums seen previously, then see if csum==target or csum-target in hmap_of_seen_sums
=> SAME CASE HERE - PREFIX sum kind of approach
- At any node,
    1. csum += node.val
    2. if csum == target (one ans found, res++)
    3. needed_sum = csum-target (check how many times csum  has been seen)
- IMPORTANT: We need to maintain CSUMS pathwise -> SO BACKTRACK adding in hmap
    - Consider each root -> leaf path to be a array and your finding subarray sum in that

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def solve(self, node: TreeNode, csum: int) -> None:
        if node is None:
            return

        x = node.val
        csum += x
        if csum == self.target:
            self.res += 1

        needed = csum-self.target
        self.res += self.hmap.get(needed, 0)
        self.hmap[csum] = self.hmap.get(csum,0) + 1
        
        self.solve(node.left, csum)
        self.solve(node.right, csum)

        # backtrack -> since this csum should only be used for the subtree/children nodes
        self.hmap[csum] -= 1
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0
        self.target = targetSum
        self.hmap = {}

        self.solve(root, 0)
        return self.res
        