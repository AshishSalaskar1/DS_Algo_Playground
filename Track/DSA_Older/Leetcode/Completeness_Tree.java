/**

In a complete binary tree every level, except possibly the last, 
is completely filled, and all nodes in the last level are as far left as possible. 
It can have between 1 and 2h nodes inclusive at the last level h.


*/


/**
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
    public boolean isCompleteTree(TreeNode root) {
        // Aproach : do an level order traversal
        // If you find one null than after that there should not be any nodes
        if( root == null)
            return false;
        
        boolean seenNull = false;
        
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        
        while( !q.isEmpty() ){
            TreeNode cur = q.poll();
            
           if(cur == null)
               seenNull = true;
            
           else{
               if(seenNull)
                 return false;

               q.add(cur.left);
               q.add(cur.right);
           }
                
        }
        return true;
        
    }
}
