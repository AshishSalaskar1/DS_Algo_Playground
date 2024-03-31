# Following is the TreeNode class structure.
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def maxDepth(root: TreeNode) -> int:
    if root is None:
        return 0

    # if root.right is None and root.left is None: # no other children then this is the only node present
    #     return 1

    # # either left or right can also be null 
    # left_height, right_height = float('-inf'), float('-inf')
    # if root.left: 
    #     left_height = maxDepth(root.left) 
    # if root.right:
    #     right_height = maxDepth(root.right) 

    return 1+max(maxDepth(root.left), maxDepth(root.right))