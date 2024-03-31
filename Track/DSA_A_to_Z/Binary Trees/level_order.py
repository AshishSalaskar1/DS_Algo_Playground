'''
- LEVEL ORDER: BFS

    Following is the structure of Tree Node

    class TreeNode:

        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
'''
from typing import List

def levelOrder(root) -> List[int]:
    lvl_order = []
    q  = []
    q.append(root)

    while len(q) != 0:
        curr = q.pop(0)
        lvl_order.append(curr.data)

        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
    
    return lvl_order
