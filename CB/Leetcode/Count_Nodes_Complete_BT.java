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

    
    static int leftDepth(TreeNode node){
        int res = 1;
        while( node.left != null){
            res++;
            node = node.left;
        }
        
        return res;
    }
    
    static int rightDepth(TreeNode node){
        int res = 1;
        while( node.right != null){
            res++;
            node = node.right;
        }
        
        return res;
    }
    
    public int countNodes(TreeNode root) {
       
        if(root == null)
            return 0;
        
        int leftD = leftDepth(root);
        int rightD = rightDepth(root);
        
        if(leftD == rightD)
            return (int)Math.pow(2,leftD)-1;
        else
            return 1 + countNodes(root.left) + countNodes(root.right);
        
       
    }
}












