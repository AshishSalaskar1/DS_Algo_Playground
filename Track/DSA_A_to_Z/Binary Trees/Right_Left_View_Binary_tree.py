# Following is the structure of Tree Node:
class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def leftView(root: BinaryTreeNode) -> None:
    q = [root]
    res = [] 

    while len(q) != 0:
        lvl_len = len(q)
        for idx in range(lvl_len):
            curr = q.pop(0)  

            if idx == 0:
                print(curr.data, end=" ")

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)