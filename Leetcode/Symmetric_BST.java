// Problem Link : https://leetcode.com/problems/symmetric-tree/
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
    static boolean sym(TreeNode a,TreeNode b){
        
        if(a == null && b == null)
            return true;
        else if(a == null || b == null)
            return false;
        
        return (a.val == b.val) && sym(a.right,b.left) && sym(b.right,a.left);
        
    }
    public boolean isSymmetric(TreeNode root) {
        if(root == null) 
            return true;
        return sym(root.left,root.right);
    }
}
