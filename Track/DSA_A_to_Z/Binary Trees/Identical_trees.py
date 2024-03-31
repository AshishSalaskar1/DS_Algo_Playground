# Following is the structure of BinaryTree Node
class BinaryTreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        
def identicalTrees(root1: BinaryTreeNode, root2:BinaryTreeNode ) -> bool:
    # both nodes are None
    if root1 is None and root2 is None:
        return True
    
    # either of the nodes is None
    if root1 is None or root2 is None:
        return False

    # check value equal -> check subtrees
    return root1.data == root2.data and identicalTrees(root1.left,root2.left) and identicalTrees(root1.right, root2.right)