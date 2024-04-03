"""
INTUTION:
- Max width: LEFT_MOST_NON_NULL_NODE - RIGHT_MOST_NON_NULL_NODE 
- In between these 2 there might be null nodes assuming its a PERFECT BINARY TREE

ALGO
- If root has idx=0, 
    1. LEFT: (2*0)+1 -> (2*IDX)+1
    2. RIGHT: (2*0)+2 -> (2*IDX)+2
    Note: [2*idx, 2*idx+1 if u start from 1]
- Get these for each LVL -> idx(first_node_lvl)-idx(last_node_lvl)+1

ISSUES
- If tree is skewed or huge depth, this index can become huge >>> INT_MAX (not issue in python)
Solution:
- At each lvl you get [x1.....xn] indexes. Make these rebased from (x1->xn) TO (0,n)
- For each x in [x1,...xn] DO x-IDX_OF_FIRST_NODE_IN_LVL
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = [(root, 0)]
        max_width = -1

        cur_lvl = 0
        while len(q) != 0:
            cur_lvl_n = len(q)
            start, end = 0, 0

            for i in range(cur_lvl_n):
                curr, curr_idx = q.pop(0)

                if i == 0:
                    start = curr_idx
                if i == cur_lvl_n - 1:
                    end = curr_idx

                if curr.left:
                    q.append((curr.left, 2*curr_idx + 1))
                if curr.right:
                    q.append((curr.right, 2*curr_idx + 2))
            
            # this leve; done
            max_width = max(max_width, end-start+1)
            cur_lvl += 1
        
        return max_width
        