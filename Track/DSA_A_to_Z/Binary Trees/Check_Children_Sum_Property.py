"""
O(N^2) Solution
- maintain global res = True
- Visit each node and update res=False, in case sum is not meant
- If met, call the same function for right and left subtrees

Faster Solution
- 
"""

'''
    Following is the class structure of the Node class:

    class Node:
        def __init__(self, data=0, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
'''

res = True

def solve(root):
    global res 
    if root is None:
        return

    # if leaf node -> doesnt count the property
    if root.left is None and root.right is None:
        return 

    rval, lval = 0, 0
    if root.left:
        lval = root.left.data
    if root.right:
        rval = root.right.data

    if rval + lval != root.data:
        # print("issue at: ", root.data, rval, lval)
        res = False
        return 
    
    # this root is proper
    solve(root.left)
    solve(root.right)
    return

def isParentSumSlower(root):
    global res 
    res = True
    solve(root)
    return res

# OPTIMAL APPROACH

def isParentSum(root):
    if root is None:
        return True

    # if leaf node -> doesnt count the property
    if root.left is None and root.right is None:
        return True

    rval, lval = 0, 0
    if root.left:
        lval = root.left.data
    if root.right:
        rval = root.right.data

    if rval + lval != root.data:
        return False
    
    # this root is proper
    return isParentSum(root.left) and isParentSum(root.right)
    


        

        
