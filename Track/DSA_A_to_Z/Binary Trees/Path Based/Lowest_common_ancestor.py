"""
NEXT UPDATED QUESTION: https://www.naukri.com/code360/problems/distance-between-two-nodes-of-a-tree_800303
- Distance(a,b) = dist(root->a) + dist(root->b) - LCA(a,b)
- BETTER: modify faster_solve() to return curr_depth in node 
    - this wont work in case Node is both root and an ancestor


FASTER IMPROVEMENT:
- Do it in single iteration method (+ MIN DISTANCE BW 2 NODES IN TREE)
Intuition:
- return null if node not found else that number if found
- Each root -> call from both left and right
- In case both are not nulls => YOU GOT THE LCA
- Else: pick whichever is not NULL, (one node found is L or R subtree)
- return NULL if both are null (means node never found in subtrees)

SOLUTION:
- Find Root -> Node path using path_to_given_node() preorder method
- Now you have 2 paths, LCA = first common node in path from right
=> [1,2,3], [5,2,7,5,10] -> here LCA(3,10) = 2

"""

'''
Binary tree node class for reference

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

def faster_solve(root, x, y):
    # one of x,y is matched or null
    if  root is None or root.data == x or root.data == y:
        return root

    left_res = faster_solve(root.left, x,y)
    right_res = faster_solve(root.right, x, y)

    # both nodes found under L and R subtrees under same ROOT
    if left_res is not None and right_res is not None:
        # this will get propagated to TOP (ALL OTHER SUBTREES WILL BE NULL -> since both found in same subtree)
        return root

    # not found in both subtrees
    if left_res is None and right_res is None:
        return None
    else: # found in either one subtree
        if left_res:
            return left_res
        else:
            return right_res

class Solution:
    final_ans = []

    def path_to_given_node(self, root, target, res=[]):
        res = res.copy()
        if root is None:
            return 
        
        if root.data == target:
            res.append(root.data)
            self.final_ans = res
            return

        res.append(root.data)
        self.path_to_given_node(root.left, target,  res)
        self.path_to_given_node(root.right, target, res)

    def lowestCommonAncestor(self, root, p, q) :
        self.final_ans = []
        self.path_to_given_node(root, p, [])
        path1 = self.final_ans

        self.final_ans = []
        self.path_to_given_node(root, q, [])
        path2 = self.final_ans


        # [1,2,3,4] [2,8,9] LCS = 2
        if len(path1) > len(path2):
            larger_path = path1
            smaller_path = path2
        else:
            larger_path = path2
            smaller_path = path1

        smaller_path = set(smaller_path)
        for x in larger_path[::-1]:
            if x in smaller_path:
                return x
        

def lowestCommonAncestor(root, x: int, y: int) -> int:
    # sol = Solution()
    # return sol.lowestCommonAncestor(root, x, y)
    res = faster_solve(root, x ,y)
    return res.data