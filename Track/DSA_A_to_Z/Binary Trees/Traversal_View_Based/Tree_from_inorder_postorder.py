"""
INTUITION:
inorder = [40,20,50,10,60,30] -> Left-Node-Right
postorder = [40,50,20,60,30,10] -> Left-Right-Node

FIRST CALL
IN = [40,20,50,10,60,30]
POST = [40,50,20,60,30,10] 
- First node or PRE=root
- Root: 10
- IN [40,20,50,10,60,30] => [LTreeNodes <-10-> RTreeNodes]
    - IN-LTreeNodes:[ 40, 20, 50]
    - IN-RTreeNodes:[ 60, 30]
- POST [40,50,20,60,30,10] # root is removed=10
    - wkt POST  visit all left tree nodes -> visit all right tree nodes -> print Node
    - [(LEFT_TREE:40,50,20), (RIGHT_TREE:30,10) (Root: 10)]
    - Here root is printed (10)
    - LeftSubTree has 3 nodes, RightSubTree has 2 nodes
    - POST-LTreeNodes:[40,50,20]
    - POST-RTreeNodes:[30,10]

Here you need find index of POST[-1]=ROOT in inorder
- For this instead of iterating you maintan a hashmap for O(1) index retrieval

"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



def build_tree(inorder, postorder):
    inorder = inorder.copy()
    postorder = postorder.copy()
    if len(postorder) == 1:
        return TreeNode(postorder[0])
    elif len(postorder) == 0:
        return None

    # GIVEN: node values are always unique
    inorder_hmap = {}
    for i, x in enumerate(inorder):
        inorder_hmap[x] = i 
    
    root = TreeNode(postorder.pop())

    # left subtree
    ls_inorder = inorder[:inorder_hmap.get(root.val)]
    ls_postorder = postorder[:len(ls_inorder)]
    root.left = build_tree(
        inorder= ls_inorder,
        postorder= ls_postorder
    )

    # right subtree
    rs_inorder = inorder[inorder_hmap.get(root.val)+1:]
    rs_postorder = postorder[len(ls_postorder):]
    root.right = build_tree(
        inorder=rs_inorder,
        postorder=rs_postorder
    )

    return root

def postorder_print(node):
    if node is None:
        return

    postorder_print(node.left)
    postorder_print(node.right)
    print(node.val, end="|")

inorder = [40,20,50,10,60,30]
postorder = [40,50,20,60,30,10]


inorder=[3,2,1]
postorder=[3,2,1]

inorder= [9,3,15,20,7]
postorder=[9,15,7,20,3]


root = build_tree(inorder, postorder)

# print(root.val)
postorder_print(root)
