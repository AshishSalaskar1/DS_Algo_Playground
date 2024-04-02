"""
Here sum can be negative also

APPROACH:
1. At each node, 
    a) consider max_path_sum passes through this node 
        max_sum = max_left + max_right + node.val => UPDATE THIS IN GLOLBAL
    b) Doesnr pass through current node: answer is only Left or Right Subtree
        - The only case where this applies LS or RS is -ve
        - But while returning max for parent subrtrees, we return 0 in case of -ve
        - And those individual subtree sums must have been accounted in global variable before reaching here

2. Return the max_sum for parents to utilize
    - In this case if u cant pick both LEFT and RIGHT -> Parents needs to be accounted
    - You pick either one

    In case this is -ve -> return 0 [same as saying dont pick this path]


IMP:
- What your RETURN: is max considering that node is not CORNER/TURNING POINT
- What you UPDATE: max considering that node is CORNER/TURNING point
- max is "INF"

"""

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    max_sum = float("-inf")

    def solve(self, node) -> int:
        if node is None:
            return 0

        # get subtree max_path_sums
        # in case any subtree is -ve, you wont consider it (so make it 0)
        max_sum_left = max(0, self.solve(node.left))
        max_sum_right = max(0,self.solve(node.right))

        # update considering CORNER point
        cur_max = node.data + max_sum_left + max_sum_right
        self.max_sum = max(self.max_sum, cur_max)

        # send back considering this is not CORNER point
        # you can either pick LEFT or RIGHT (NOT BOTH) for calculating upper subtree sums
        cur_max_sum = max(max_sum_left, max_sum_right) + node.data
        return cur_max_sum


    def maxPathSum(self, root) -> int:
        self.solve(root)
        return self.max_sum

def maxPathSum(root: BinaryTreeNode) -> int:
    sol = Solution()
    return sol.maxPathSum(root)