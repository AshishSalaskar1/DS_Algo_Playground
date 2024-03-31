"""
Explained: https://takeuforward.org/data-structure/preorder-inorder-postorder-traversals-in-one-traversal/

Core Logic:
1. In PRE-ORDER you visit the node and save it first time
2. In IN-ORDER you visit the node 2nd time and then save it 
    (Visit once -> Go left -> come back -> print on second visit -> GO RIGHT)
3. In POST-ORDER you visit the node 3rd time and then save it  
    (Visit once -> Go left -> come back -> VISIT second  -> GO RIGHT -> come back -> Print on third visit)

"""

# Following is the Binary Tree node structure:
class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def getTreeTraversal(root):
    inorder, preorder, postorder = [], [], [] 

    q = [(root,1)]
    vis = {}

    while len(q) != 0:
        curr_node, counter = q.pop()
        curr_val = curr_node.data
        

        if counter == 1: # this is part of pre-order (PRINT, LEFT, RIGHT)
            preorder.append(curr_val)
            q.append((curr_node, 2)) # add back to Q
            if curr_node.left: # add only left (PREORDER)
                q.append((curr_node.left, 1))
        elif counter == 2: # this is part of in-order (LEFT, PRINT, RIGHT)
            inorder.append(curr_val)
            q.append((curr_node, 3)) # add back to Q
            if curr_node.right: # add only right (INORDER)
                q.append((curr_node.right, 1))
        elif counter == 3:  # this is part of post-order (LEFT, RIGHT, PRINT)
            postorder.append(curr_val)

        
    return [inorder, preorder, postorder]