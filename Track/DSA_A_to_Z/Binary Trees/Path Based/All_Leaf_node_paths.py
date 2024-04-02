class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


final_ans = []

def all_leaf_paths(root, res):
    res = res.copy()
    global final_ans
    if root is None:
        return 

    if root.left is None and root.right is None:
        res.append(root.data)
        final_ans.append(res)
        return

    res.append(root.data)
    all_leaf_paths(root.left, res)
    all_leaf_paths(root.right, res)


def allRootToLeaf(root):
    global final_ans
    final_ans = []
    all_leaf_paths(root, [])
    print(final_ans)




root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

allRootToLeaf(root)