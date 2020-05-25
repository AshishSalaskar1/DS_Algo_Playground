// Problem Link : https://leetcode.com/problems/path-sum
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
    
    static boolean sumPath(TreeNode root, int sum){
        if(root == null)
            return false;
        
        int curSum = sum - root.val;

        
        if(root.left == null && root.right == null)
        {         
            if(curSum == 0) 
                return true;
            else 
                return false;
        }
        
        else if(root.right == null)
            return sumPath(root.left,curSum);
        else if(root.left == null)
            return sumPath(root.right,curSum);
        
        return sumPath(root.left,curSum) || sumPath(root.right,curSum);
        
    }
    public boolean hasPathSum(TreeNode root, int sum) {
        return sumPath(root,sum);
    }
}
