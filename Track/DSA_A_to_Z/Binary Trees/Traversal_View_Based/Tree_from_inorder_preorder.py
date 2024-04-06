"""
INTUITION:
inorder = [40,20,50,10,60,30] -> Left-Node-Right
preorder = [10,20,40,50,30,60] -> Node-Left-Right

FIRST CALL
IN = [40,20,50,10,60,30]
PRE = [10,20,40,50,30,60] 
- First node or PRE=root
- Root: 10
- IN [40,20,50,10,60,30] => [LTreeNodes <-10-> RTreeNodes]
    - IN-LTreeNodes:[ 40, 20, 50]
    - IN-RTreeNodes:[ 60, 30]
- PRE [20,40,50,30,60] # root is removed
    - [(Root: 10), (LEFT_TREE:20,40,50), (RIGHT_TREE:30,60)]
    - wkt PRE you visit node -> visit all left tree nodes -> visit all right tree nodes
    - Here root is printed (10)
    - LeftSubTree has 3 nodes, RightSubTree has 2 nodes
    - PRE-LTreeNodes:[20,40,50]
    - PRE-RTreeNodes:[30,60]

Here you need find index of preorder[0]=ROOT in inorder
- For this instead of iterating you maintan a hashmap for O(1) index retrieval

"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



def build_tree(inorder, preorder):
    if len(preorder) == 1:
        return TreeNode(preorder[0])
    elif len(preorder) == 0:
        return None

    # GIVEN: node values are always unique
    inorder_hmap = {}
    for i, x in enumerate(inorder):
        inorder_hmap[x] = i 
    
    root = TreeNode(preorder.pop(0))

    # left subtree
    ls_inorder = inorder[:inorder_hmap.get(root.val)]
    ls_preorder = preorder[:len(ls_inorder)]
    
    root.left = build_tree(
        inorder= ls_inorder,
        preorder= ls_preorder
    )

    # right subtree
    rs_inorder = inorder[inorder_hmap.get(root.val)+1:]
    rs_preorder = preorder[len(ls_inorder):]
    root.right = build_tree(
        inorder=rs_inorder,
        preorder=rs_preorder
    )

    return root

def preorder_print(node):
    if node is None:
        return

    print(node.val, end="|")
    preorder_print(node.left)
    preorder_print(node.right)

inorder = [40,20,50,10,60,30]
preorder = [10,20,40,50,30,60]
root = build_tree(inorder, preorder)

# print(root.val)
preorder_print(root)
