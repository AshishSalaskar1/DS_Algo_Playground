"""
- VERTICAL ORDER and LVL_ORDER
- TRACK:
    {
        vert: {
            hor: [.....]
        }
    }

vert -> vertical level
hor -> horizontal level

- Top view: 
    1. Iterate through vert_lvls in sorted order
    2. First element in the top most / lowest hor_lvl will come in top view

- Bottom view: 
    1. Iterate through vert_lvls in sorted order
    2. Last element in the bottom most / highest hor_lvl will come in top view
"""

from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**7)

# Following is the TreeNode class structure:
class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def bottomView(root: BinaryTreeNode) -> List[int]:
    # vert -> lvl -> [] 
    track = {}
    q = [(root, 0, 0)] # (node, vertical_level, level)

    while len(q) != 0:
        curr, vert, hor = q.pop(0)

        track[vert] = track.get(vert, {})
        track[vert][hor] = track[vert].get(hor, [])
        track[vert][hor].append(curr.data)

        if curr.left: # you are moving LEFT+DOWN
            q.append((curr.left, vert-1, hor+1))
        if curr.right: # you are moving RIGHT+DOWN
            q.append((curr.right, vert+1, hor+1))

    res = []

    for vert_lvl in sorted(track.keys()): # vertical level sorted: -2, -1, 0 , 1, 2
        # get last lower most / top horizontal order
        last_lvl = sorted(track[vert_lvl].keys())[-1]
        res.append(track[vert_lvl][last_lvl][-1])

    return res