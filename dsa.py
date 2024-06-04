class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.val, end="->")
    inorder(node.right)


class Solution:
    def morris(self, root):
        res = []
        cur = root
        
        while cur is not None:
            if cur.left is None:
                res.append(cur.val)
                cur = cur.right
                continue

            loopfound = False

            # find rightmost node in LEFT SUBTREE
            rightmost = cur.left
            while rightmost.right:
                rightmost = rightmost.right 
                if rightmost == cur:
                    loopfound = True
                    break
                    
            if loopfound:
                res.append(cur.val)
                print(res)
                cur = cur.right
            else:
                rightmost.right = cur
                cur = cur.left
        
        print(res)

            



root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

inorder(root)
print()

sol = Solution()
sol.morris(root)

"""
        5
       / \
      3   7
     / \ / \
    2  4 6  8

"""



