# DP ON TREES

Types
1. In-Out DP
2. Ancestor Property DP
3. Knapsack DP


## Examples

### (IN-DP) House Robber style (You cant pick adjacent nodes)
- Here adjacent refers to parent-child
- Common pattern for in-dp
  
```py
def indfs(self, node, par):
    # CONSIDER THESE ARE LEAF NODE - BASE CASES
    # if this was the leaf node, you can either pick/not pick
    self.dp[node][1] = self.val[node] # node is picked
    self.dp[node][0] = 0 # node is not picked

    for child in self.adj[node]:
        if child != par:
            self.indfs(child, node) # this will calculate all the lower child values 

            # picked this node, you cant pick child node 
            self.dp[node][1] += self.dp[child][0] 
            # didnt pick this node, you can either pick child or not 
            self.dp[node][0] += max(self.dp[child][0], self.dp[child][1]) 


# max_res from node=1, by either picking or not picking
ans = max(tree.dp[1][0], tree.dp[1][1])

```

💡 Same thing is done in **House-Robber-III** (But with TreeNode concept)
- Since we see that you assign dp[node][0/1] only once in each call => you can use dict for same

```py
class Solution:
    def indfs(self, node):
        if node is None:    return
        self.dp[node] = {
            1: node.val,
            0: 0
        }

        childs = [node.left, node.right]
        for child in [x for x in childs if x is not None]:
            self.indfs(child)
            self.dp[node][1] += self.dp[child][0]
            self.dp[node][0] += max(self.dp[child][0],self.dp[child][1])

    def rob(self, root: Optional[TreeNode]) -> int:
        self.dp = {}
        self.indfs(root)

        return max(
            self.dp[root][0],
            self.dp[root][1]
        )
```