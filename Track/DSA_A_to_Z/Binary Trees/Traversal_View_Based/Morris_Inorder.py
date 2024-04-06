"""
MORRIS INORDER TRAVERSAL
- Do inorder traversal in O(N) time and using O(1) space
- Challenge: You use recursion or stack to store nodes and automatically revist them while returning (BUT CANT DO THAT)
- Solution: Use threads to maintain where to come back


SOLUTION:
- INORDER: LEFT -> PRINT -> RIGHT
- CUR = ROOT
    - if cur.left is None (Nothing in left to print) -> PRINT ->  GO RIGHT
    - If you have a left subtree
        1. Find right most node in that left subtree (start from cur.left and only go right)
        2. If you find a node which has right = cur (Its already threaded)
            - This happens when u have threaded node x->cur, u go visit all left subtree and then
              you reach right_most_node.right -> and reach root/cur again
            - This means u previously visited this left subtree (from the same node)
            - You can consider this left subtree as visited -> PRINT -> MOVE RIGHT
        3. right_mode_node.RIGHT = curr
        4. MOVE LEFT (Visit left subtree now since you have thread to return back to curr node later)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 


def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.val, end=" ")
    inorder(node.right)


def morris_inorder(root):
    res = []

    cur = root
    while cur is not None:
        print("curr: ", cur.val)
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
        if right_most_node == -1:
            res.append(cur.val)
            cur = cur.right
        else: # add thread to current node -> move left
            right_most_node.right = cur
            cur = cur.left

    
    print(res)
    return res


root = TreeNode(1)
root.right = TreeNode(3)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.right = TreeNode(6)

inorder(root) # 4 2 5 6 1 3
print()
morris_inorder(root) # 4 2 5 6 1 3