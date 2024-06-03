"""
PROBLEM: https://leetcode.com/problems/binary-search-tree-iterator/description/

SOLUTION 1: O(n)
- Create inorder array and keep when init() is called with root node - O(N) space and time
- Then hasNext() and next() can be done in O(1) time

Faster SOLUTION: O(height)
- In inorder wkt that its visit all lefts -> Print Node -> Print right
- Init(root) => push all lefts of root into stack
- next()
    - nextNode = stack.pop()
    - if nextNode has no right Subtree=> this itself is inorder
    - If it has has right subtree, push all of its lefts in the right subtree to stack
        - assume this as left was visited before pushing -> now you push node -> You need to visit nodes in right subtree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.push_all_left(root)

    
    def push_all_left(self, node: TreeNode):
        """
        Push all nodes iterating left of node into stack
        """
        cur = node
        while cur:
            self.stack.append(cur)
            cur = cur.left

    def next(self) -> int:
        next_node = self.stack.pop()
        if next_node.right is not None: # if right subtree is not empty
            self.push_all_left(next_node.right)
        return next_node.val
        

    def hasNext(self) -> bool:
        return len(self.stack) > 0

"""
BST Iterator which does REVERSE INORDER = [HIGHEST...LOWEST]
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

"""
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


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
