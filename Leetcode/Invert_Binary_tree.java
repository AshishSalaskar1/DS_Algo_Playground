// Problem Link : https://leetcode.com/problems/invert-binary-tree/
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
    static TreeNode temp;
    
    static void invert(TreeNode root){
         if(root == null)
            return ;
        
        // Swap right and left sub trees
        temp = root.left;
        root.left = root.right;
        root.right = temp;
        
        invert(root.left);
        invert(root.right);
        
    }
    public TreeNode invertTree(TreeNode root) {
       
        invert(root);
        return root;
    
    }
}
