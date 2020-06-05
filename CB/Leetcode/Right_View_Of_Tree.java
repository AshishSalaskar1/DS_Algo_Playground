/**
Given a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---


 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        
        LinkedList<TreeNode> q = new LinkedList<>();
        
        if(root == null) return res;
        
        q.add(root);
        
        while(!q.isEmpty()){
            //this gives cur size of queue = no of nodes in current level
            int levelSize = q.size();
            
            System.out.println(levelSize);
            //get last | right-most node of each level
            for(int i=0;i<levelSize;i++){
                TreeNode node = q.removeFirst();

                if(i == levelSize - 1)
                    res.add(node.val);
                
                if(node.left != null)
                    q.addLast(node.left);
                
                if(node.right != null)
                    q.addLast(node.right);
            }
        
        }
        
        return res;
        
        
    }
}





















