"""
PROBLEM: https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/?envType=problem-list-v2&envId=my4z5092

SOLUTION: Euler Tour
- Do dfs and height=lvl, before and after each call put (node,level) into tour array
- Once you have tour array, find start+end of each node
- Calculate prefix and suffix sums = max_till_index(max height from 0 to i) and max_from_index(max height from i to n)
          "1"
       " /   \"
      "2      3"
     "/"
    "4"
# euler tour array is [(1,0),(2,1),(4,2),(4,2),(2,1),(3,1),(3,1),(1,0)]
- If you observe between (NODE, lvl) ..... (NODE, lvl), you will have all nodes which are subtrees under given NODE

- Now query comes in [2]
    start, end = 1, 4
    [(1,0) | (2,1),(4,2),(4,2),(2,1) | (3,1),(3,1),(1,0)]
    - res = max_height([(1,0)]) OR max_height([(3,1),(3,1),(1,0)]])
    - res = max(  max_depth_till_here[start-1],  max_depth_till_here[end-1] )
    Note: 
    - Handle cases when start=0 and end=n 
    - Here 0 to n indicate index in Euler tours array - NOT NODE THEMSELVES

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class EulerTour:
    def __init__(self) -> None:
        pass

    def solve(self, node: TreeNode, level: int):
        self.tour.append( (node.val, level) )

        if node.left: self.solve(node.left, level+1)
        if node.right: self.solve(node.right, level+1)

        self.tour.append( (node.val, level) )

    def get_euler_tour(self, root: TreeNode):
        self.tour = []
        self.solve(root, 0)
        return self.tour


class Solution:
    def get_euler_tour(self, node: TreeNode, level: int):
        self.tour.append( (node.val, level) )

        if node.left: self.get_euler_tour(node.left, level+1)
        if node.right: self.get_euler_tour(node.right, level+1)

        self.tour.append( (node.val, level) )

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        self.tour = []
        self.get_euler_tour(root, 0)
        tour = self.tour    # [ (node, max_depth),... ]    ​

        max_depth_till_here = [0]*len(tour)
        max_depth_from_here = [0]*len(tour)

        # get start and end for each node (node value here) -> IDEALLY YOU SHOULD USE NODE_IDX since node values can repeat (DONT REPEAT IN THIS CASE)
        start_end_map = defaultdict(list)
        for i, tour_ele in enumerate(tour): # saving index of each node in the tour array
            start_end_map[tour_ele[0]].append(i)

        max_val = -1
        for i in range(len(tour)):
            max_val = max(max_val, tour[i][1])
            max_depth_till_here[i] = max_val

        max_val = -1
        for i in reversed(range(len(tour))):
            max_val = max(max_val, tour[i][1])
            max_depth_from_here[i] = max_val


        res = []
        for delete_root in queries:
            [start, end] = start_end_map[delete_root]
            depth = 0
            if start>0:
                depth = max(depth, max_depth_till_here[start-1])
            if end < len(tour)-1:
                depth = max(depth, max_depth_from_here[end+1])
            res.append(depth)
        
        return res



        