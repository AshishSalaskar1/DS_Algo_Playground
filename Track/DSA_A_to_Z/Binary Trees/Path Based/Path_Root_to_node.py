class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


final_ans = []

def path_to_given_node(root, target, res=[]):
    res = res.copy()
    global final_ans
    if root is None:
        return 
    
    if root.data == target:
        res.append(root.data)
        final_ans = res
        return

    res.append(root.data)
    path_to_given_node(root.left, target,  res)
    path_to_given_node(root.right, target, res)

def pathToGivenNode(root, target):
    global final_ans
    final_ans = []
    path_to_given_node(root, target, res=[])
    print(final_ans)



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

pathToGivenNode(root, 4)