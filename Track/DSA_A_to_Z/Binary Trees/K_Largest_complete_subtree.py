"""
Problem: https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/

You are given the root of a binary tree and an integer k.
Return an integer denoting the size of the kth largest perfect binary subtree or -1 if it doesn't exist.
A perfect binary tree is a tree where all leaves are on the same level, and every parent has two children.


SOLUTION:
- Some considerations
=> Single node is always complete
=> If either subtrees of node are not perfect, then one including current node will also not be complete
=> If both subtrees are perfect, current subtree will also become perfect => count(left_subtree) == count(right_subtree)


"""
class Solution:
    def solve(self, root):
        if root is None:
            return 0

        # Single node is always complete
        if root.left is None and root.right is None:
            self.res.append(1)
            return 1
        
        lst = self.solve(root.left)
        rst = self.solve(root.right)

        # If either subtrees of node are not perfect, then one including current node will also not be complete
        if lst == -1 or rst == -1 or lst != rst:
            return -1
        
        # cur subtree size = 1 + left and right subtree sizes
        self.res.append(1+lst+rst)
        return 1 + lst + rst

    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.res = [] # remember the k-th ranking is including duplicates
        self.solve(root)
        res = sorted(self.res, reverse=True)
        return -1 if len(res)<k else res[k-1]