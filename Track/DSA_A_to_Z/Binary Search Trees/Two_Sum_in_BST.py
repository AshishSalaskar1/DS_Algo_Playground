"""
PROBLEM: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
- pair sum in BST

SOLUTION 1 - Simple
- Do inorder, this will give you sorted array
- Twosum on this sorted array
TC = O(n) + (n)
SC = O(N)

SOUTION 2 - O(h) space
- BST Iterator: https://leetcode.com/problems/binary-search-tree-iterator/
- This gives you the nodes in INORDER (lowest -> highest) on calling next()
- Modify this to give you reverse also - POSTORDER => (highest -> lowest) on calling next()
    => HOW?
    ==> Low to high
        1. INIT: push node and all its lefts
        2. next(): cur = stack.top(), if that has right tree -> then add all lefts of that
        - Consider this as inorder (L Node R)
    ==> High to Low:
        1. INIT: push node and all its rights
        2. next(): cur = stack.top(), if that has left tree -> then add all rights of that
        - Consider this as reverse Inorder (R Node L)

- Then use these 2 ierators as feeders for lo and hi pointers

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    """
    next() -> returns 
    """

    def __init__(self, root: Optional[TreeNode], reverse: bool = False):
        self.stack = []
        self.reverse = reverse
        self.push_all_left(root)

    
    def push_all_left(self, node: TreeNode):
        """
        Push all nodes iterating left of node into stack
        """
        cur = node
        while cur:
            self.stack.append(cur)
            if self.reverse is True:
                cur = cur.right
            else:
                cur = cur.left

    def next(self) -> int:
        next_node = self.stack.pop()
        if next_node.right is not None: # if right subtree is not empty
            if self.reverse:
                self.push_all_left(next_node.left)
            else:
                self.push_all_left(next_node.right)
        return next_node.val
        

    def hasNext(self) -> bool:
        return len(self.stack) > 0


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        incr = BSTIterator(root, reverse=False)
        decr = BSTIterator(root, reverse=True)

        lo,hi = incr.next(), decr.next()

        while incr.hasNext() and decr.hasNext():
            print(lo, hi)
            if k == lo+hi:
                return True
            elif k < lo+hi:
                hi = decr.next()
            else:
                lo = incr.next()

        return False
            
        
    # -3 -1 0 2 4 [-4]