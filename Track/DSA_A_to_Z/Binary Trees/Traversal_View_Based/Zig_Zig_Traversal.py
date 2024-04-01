# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
            
        q = [root]
        zig_zag = []

        while len(q) != 0:
            n_cur_lvl = len(q)
            # all nodes present in Q belogn to same lvl (THEY WERE ADDED AT SAME LVL)
            cur_lvl = []
            for _ in range(n_cur_lvl):
                curr = q.pop(0)
                cur_lvl.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        
            zig_zag.append(cur_lvl)
        
        for idx, arr in enumerate(zig_zag):
            if idx % 2 != 0: # odd index reverse
                zig_zag[idx] = reversed(arr)
        
        return zig_zag


        
        