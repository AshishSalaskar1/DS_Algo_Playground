"""
LOGIC:

SERIALIZE: Tree -> STR
- Do level order traversal 
- For any node, if you find Left,right or both are null you add # for each missing
- By doing this we ensure that each node has 2 nodes for sure in STR_REP (It will be # if nulls)

DESERIALIZE: STR -> Tree
[10, 20, 30]
- 10 First ele will be root -> push in Q
    - root.left = TreeNode(30) -> str[0] -> push in Q
    - root.left = TreeNode(20) -> str[1] -> push in Q
    - if either str[0] or str[1] is # means its NULL. Dont do anything since TreeNode inits right,left as null
- WHILE LOOP RUNS TILL
    1) Q is not empty (no roots/node present to add)
    2) len(STR_REP) >= 2 [ex: [1] => "1"]

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = ""
        q = [root]

        if root is None:
            return ""

        # only one node -> you dont have to append ","
        if root.left is None and root.right is None:
            return str(root.val)

        while len(q) != 0:
            curr = q.pop(0)

            if curr is None: # needed since we also add null nodes -> dont add further in Q
                res += "#" + ","
                continue
            else: # non #/null value
                res += str(curr.val) + ","

            q.append(curr.left) # append null in case not present
            q.append(curr.right) # append null in case not present
        
        # print(res[:-1])
        # 1,2,3,#,#,4,5,#,#,#,#, (remove comma from last)
        return res[:-1]

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        str_rep = data.split(",")
        # case: [] -> [""] -> len("".split(",") = 1
        if len(data)==0 or len(str_rep) == 0:
            return None
        
        root = TreeNode(int(str_rep[0]))
        str_rep = str_rep[1:]
        q = [root]
        
        # Q is not empty and <2 nodes are remaining in str_rep (use case: input: [1], str_rep=1)
        while len(q) != 0 and len(str_rep)>=2:
            curr = q.pop(0)

            # left node
            left_node_val = str_rep[0]
            if left_node_val != "#":
                curr.left = TreeNode(left_node_val)
                q.append(curr.left)


            # right node
            right_node_val = str_rep[1]
            if right_node_val != "#":
                curr.right = TreeNode(right_node_val)
                q.append(curr.right)

            # remove 2 nodes [ROOT,L,R]
            str_rep = str_rep[2:]
        
        return root
                    

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))