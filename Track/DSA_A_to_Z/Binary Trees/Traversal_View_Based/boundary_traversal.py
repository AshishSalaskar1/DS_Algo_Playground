'''
    Time Complexity: O(N)
    Space Complexity: O(N)

    Where N is the number of nodes in the Binary Tree.
'''

# Binary tree node class for reference.
# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None


def is_leaf_node(node):
    return node.left is None and node.right is None

# This excludes leaf node
def left_boundary(root):
    # why? [null<-1->3], [4<-3->null], [5<-4->null]
        # 1
        #      3
        #   4
        # 5
        # In this case You might think LEFT: [1,3,4,5]
        # But instead its [1]. Why? Its asked left boundary and NOT LEFT VIEW
        # So even though you can see [3,4,5], since they are on right you ignore
    cur = root.left
    res = []

    # never include right side nodes -> even if it falls in left boundary
    while cur is not None and not is_leaf_node(cur):
        # if not is_leaf_node(cur): # WHY NOT IN WHILE?
        res.append(cur.data)       
        if cur.left: # first try going left
            cur = cur.left
        elif cur.right: # go right in case left not found
            cur = cur.right
    
    return res

def right_boundary(root):
     # dont include root (its already added in left-side)
    cur = root.right
    res = []

    while cur is not None and not is_leaf_node(cur):
        # if not is_leaf_node(cur): # WHY NOT IN WHILE?
        res.append(cur.data)
        if cur.right: # first try going right
            cur = cur.right
        elif cur.left: # go left in case left not found
            cur = cur.left

    return res[::-1]

leaf_nodes = []
def leaf_traverse_preorder(node):
    global leaf_nodes
    if node is None:
        return
    
    if is_leaf_node(node) and node.data not in leaf_nodes:
        leaf_nodes.append(node.data)
        return 

    leaf_traverse_preorder(node.left)
    leaf_traverse_preorder(node.right)



# Functions to traverse on each part.
def traverseBoundary(root):
    res = []


    left = left_boundary(root)
    right = right_boundary(root)
    leaf_traverse_preorder(root)


    return  [root.data, *left, *leaf_nodes, *right]