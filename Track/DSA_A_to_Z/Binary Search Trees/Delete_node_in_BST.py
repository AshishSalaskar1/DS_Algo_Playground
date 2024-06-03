"""
PROBLEM: https://leetcode.com/problems/delete-node-in-a-bst/description/
- Given a BST, delete a given node if its present

INTUTION:
- To delete a node, you can replace it with 2 options (both are accepted)
    1. Largest element in left subtree (right most element in LST)
    2. Smallest element in right subtree (left most element in RST)
- We will follow (1)

- While iterating you have 3 options
    1. key < val -> node.left = delete(node.left)
    2. key > val -> node.right = delete(node.right)
    3. You find the node having key. Now this has 4 types
        1. Both left and right subtrees are absent -> delete this -> just return None
        2. Either left or right subtree is present -> return whatever is present
        3. BOTH PRESENT
            - find val of successor (smallest element in right subtree)
            - node.val = successor
            # Delete the successor node in right subtree (you have already)
            - node.right = delete(node.right, successor)

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, node: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if node is None:
            return node

        if key > node.val:
            node.right = self.deleteNode(node.right, key)
        elif key < node.val:
            node.left = self.deleteNode(node.left, key)
        else: # fonud node where val = needed val
            if node.left is None and node.right is None: # no subtrees -> just delete
                node =  None
            elif node.left is None:
                node =  node.right
            elif node.right is None:
                node =  node.left
            else: # both LEFT+RIGHT trees are present -> Find successor (lowest val in right subtree or highest in left subtree)
                successor = node.right
                while successor.left:
                    successor = successor.left
                
                node.val = successor.val
                node.right = self.deleteNode(node.right, successor.val)
        
        return node
    

