/** 
Problem Link : https://leetcode.com/problems/validate-binary-search-tree

BST cant contain same values

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
    
    
    static boolean checkBST(TreeNode node ,Integer min,Integer max){
        if(node == null)
            return true;
        
        
        int val = node.val;
        

        if((min!=null && val<=min) || (max!=null && val>=max))
            return false;
            
        return checkBST(node.left,min,val) && checkBST(node.right,val,max);
    }
    
    public boolean isValidBST(TreeNode root) {
        return checkBST(root,null,null);
        
    }
}
