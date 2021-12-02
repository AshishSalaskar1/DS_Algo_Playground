/**

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. 
Return 9+15 = 24. 

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
    
    public int sumOfLeftLeaves(TreeNode node) {
        if(node == null)
            return 0;
        int res = 0;
        
        if(node.left != null)
            if(node.left.left == null && node.left.right == null)
                res += node.left.val;
            else 
                res += sumOfLeftLeaves(node.left);
        
        res += sumOfLeftLeaves(node.right);
        
        return res;
    }
}
