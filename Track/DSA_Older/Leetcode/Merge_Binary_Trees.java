//Problem Link : https://leetcode.com/problems/merge-two-binary-trees/

 
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
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        if(t1 == null) return t2;
        if(t2 == null) return t1;
        
        t1.val += t2.val;
        t1.right = mergeTrees(t1.right,t2.right);
        t1.left = mergeTrees(t1.left,t2.left);
        
        return t1;
    }
}


/**
Reduced Recursive Calls
*/
public TreeNode mergeTreesROP(TreeNode t1, TreeNode t2) {
        if(t1==null && t2==null) return null;
        if(t1==null) return t2;
        if(t2==null) return t1; 
      
        TreeNode t = new TreeNode(t1.val + t2.val);
        t.left = mergeTrees(t1!=null? t1.left: null, t2!=null?t2.left: null);
        t.right = mergeTrees(t1!=null? t1.right: null, t2!=null?t2.right: null);
        
        return t;
   }
