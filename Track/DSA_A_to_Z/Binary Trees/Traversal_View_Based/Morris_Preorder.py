"""
MORRIS INORDER TRAVERSAL
- Do inorder traversal in O(N) time and using O(1) space
- Challenge: You use recursion or stack to store nodes and automatically revist them while returning (BUT CANT DO THAT)
- Solution: Use threads to maintain where to come back


SOLUTION:
- PREORDER: PRINT -> LEFT -> RIGHT
- CUR = ROOT
    - if cur.left is None (Nothing in left to print) -> PRINT ->  GO RIGHT
    - If you have a left subtree
        1. Find right most node in that left subtree (start from cur.left and only go right)
        2. If you find a node which has right = cur (Its already threaded)
            - Just ignore and move RIGHT
            - Since this is alread threaded, u must have printed it while the thread was made
        3. right_mode_node.RIGHT = curr
            - In this case you PRINT the curr node (PRINT -> LEFT -> RIGHT)
            - For every node you visit 
                - either left is NULL -> PRINT -> MOVE RIGHT
                - you find some node and thread it: right_most_node.right = cur
        4. MOVE RIGHT
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 


def preorder(node):
    if node is None:
        return

    print(node.val, end=" ")
    preorder(node.left)
    preorder(node.right)


def morris_preorder(root):
    res = []

    cur = root
    while cur is not None:
        # left subtree is empty -> no need to visit
        if cur.left is None:
            res.append(cur.val)
            cur = cur.right
            continue
        
        # left subtree present -> find rightmost node
        right_most_node = cur.left
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
        
        # check if right-most node is already threaded -> all left nodes are visited
        if right_most_node == -1: # add thread to current node -> move left
            right_most_node.right = cur.right
            left_subtree = cur.left
            cur = left_subtree
            cur.left = None
    
    return res


root = TreeNode(1)
root.right = TreeNode(3)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.right = TreeNode(6)

preorder(root) # 4 2 5 6 1 3
print()
morris_preorder(root) # 4 2 5 6 1 3