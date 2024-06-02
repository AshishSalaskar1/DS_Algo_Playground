"""
BRUTE FORCE
1. Iterate through each node, calculate left and right depths -> False if diff > 1
2. Current tree is balanced, now check if both subtrees are balanced also
TC: O(N*N) -> Your calling depth on each N and depth itself takes O(N)

FASTER -> modify height function
function returns -1 -> IF subtree is IMBALANCED
function returns != -1 -> height/depth of the subtree
1. For each node, 
    1. find left height -> if its -1 return -1
    2. find right height -> if its -1 return -1
2. If abs(diff) > 1: return -1
3. return height = 1 + max(left, right)  # THIS MEANS subtree is balanced and the height is returned

"""

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def depth(root):
    if root is None:
        return 0

    return 1 + max(depth(root.left), depth(root.right))

# BRUTE FORCE: O(n*n) approach since depth is calculated each time
def is_balanced(root) -> bool:
    if root is None:
        return True

    left_height = depth(root.left)
    right_height = depth(root.right)

    # IMBALANCED: No need to check lower sub-trees
    if abs(left_height-right_height) > 1:
        return False
    
    # now check if lower subtrees are balanced
    return is_balanced(root.left) and is_balanced(root.right)


def is_balanced_depth(root):
    if root is None:
        return 0
    
    left_height = is_balanced_depth(root.left)
    if left_height == -1:
        return -1
    
    right_height = is_balanced_depth(root.right)
    if right_height == -1:
        return -1

    if abs(left_height-right_height) > 1:
        return -1
    
    return 1 + max(left_height, right_height)
    

def isBalancedBT(root: BinaryTreeNode) -> bool:
    if is_balanced_depth(root) == -1:
        return False
    else:
        return True
    