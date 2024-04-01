# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        track = {}
        q = [(root, 0, 0)] # (node, vertical_level, level)

        while len(q) != 0:
            curr, vert, hor = q.pop(0)

            track[vert] = track.get(vert, {})
            track[vert][hor] = track[vert].get(hor, [])
            track[vert][hor].append(curr.val)

            if curr.left: # you are moving LEFT+DOWN
                q.append((curr.left, vert-1, hor+1))
            if curr.right: # you are moving RIGHT+DOWN
                q.append((curr.right, vert+1, hor+1))

        res = []

        for vert_lvl in sorted(track.keys()): # vertical level sorted: -2, -1, 0 , 1, 2
            vert_lvl_res = []
            for hor_lvl in sorted(track[vert_lvl].keys(), reverse=False):
                vert_lvl_res.extend(sorted(track[vert_lvl][hor_lvl])) # RESULT: sorted in case of same vert, hor order
            res.append(vert_lvl_res)

        return res
        