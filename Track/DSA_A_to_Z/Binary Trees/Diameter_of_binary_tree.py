# Following is the TreeNode class structure.
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# def find_depth(node):
#     if node is None:
#         return 0
#     return 1 + max(find_depth(node.left), find_depth(node.right))

# res = float("-inf")

# def find_diam(node):
#     global res
#     if node is None:
#         return 0
    
#     left_depth = find_depth(node.left)
#     right_depth = find_depth(node.right)

#     res = max(res, left_depth + right_depth)

#     find_diam(node.left)
#     find_diam(node.right)

#     return 

# def find_diam(node, diam):
#     if node is None:
#         return 0

#     lh = find_diam(node.left, diam)
#     rh = find_diam(node.right, diam)

#     diam = max(diam ,lh+ lh)
#     return 1+max(lh, rh)

class myAns:
    def __init__(self,diametre,height):
        self.d = diametre
        self.h = height


def solve(root):
    if root==None:
        ans = myAns(0,0)
        return ans

    left_diametre = solve(root.left)
    right_diametre= solve(root.right)


    op1 = left_diametre.d
    op2 = right_diametre.d
    op3 = left_diametre.h+right_diametre.h
 
    new_ans = myAns(0,0)
    new_ans.d = max(op3,max(op1,op2))
    new_ans.h = max(left_diametre.h,right_diametre.h)+1

    return new_ans

def diameterOfBinaryTree(root: TreeNode) -> int:
    # return solve(root).d
    return find_diam(root, 1)