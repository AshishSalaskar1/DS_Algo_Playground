"""
PBLM: Flatten the tree like a linked list in PREORDER: RIGHT SKEWED TREE

INTUITION:
- Modification of MORRIS
- For each node root:
    0. If root.left is None -> continue
    1. Find right most node in Left Subtree, right_most.RIGHT = root.RIGHT
       (right most node in LT will be last node in preorder of LT,
       so ROOT (left=null, right=LST) -> LST -> ROOT.right
    2. There is no concept of revisting the same thread here
    3. ROOT.left=NULL, ROOT.right=(Left Subtree)

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur is not None:
            # print("curr: ",cur.val, cur.left, cur.right, sep="|")
            # left subtree is empty -> no need to visit
            if cur.left is None:
                cur = cur.right
                continue
            
            # left subtree present -> find rightmost node
            right_most_node = cur.left
            # print("RM Init: ",right_most_node.val)
            while True:
                if right_most_node.right is not None:
                    # if right most node is already threaded to curr
                    if right_most_node.right == cur:
                        right_most_node = -1
                        break
                    
                    # move to right node
                    right_most_node = right_most_node.right
                else:
                    break
            
            # print("RM Node: ", right_most_node.val)
            # check if right-most node is already threaded -> all left nodes are visited
            if right_most_node != -1: # add thread to current node -> move left
                right_most_node.right = cur.right
                
                # set cur->LEFT_SUBTREE, null<-cur
                # move cur = cur.right (cur.right is newly set LEFT SUBTREE NOW)
                left_subtree = cur.left
                cur.left = None # ROOT.left=NULL
                cur.right = left_subtree # ROOT.right=(Left Subtree)

                cur = cur.right # run on left subtree == cur.right
                
                # print(f"set {right_most_node.val} -> {right_most_node.right.val}")
        
        return root
            