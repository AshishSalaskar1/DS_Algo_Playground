/**

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

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
    
    static TreeNode createBST(int[] pre, int start,int end){
        if(start > end) return null;
        
        TreeNode node = new TreeNode(pre[start]);
        
        int i;
        /** find ele in pre which is  > than node.val
        8 5 1 7 10 12
        node.val = 8
        i = 4
        node.left = [5, 1 ,7] 
        node.right = [10, 12]
        */
        for(i= start;i<=end;i++){
            if(pre[i] > node.val) break;
        }
        
        
        node.left = createBST(pre,start+1,i-1);
        node.right = createBST(pre,i,end);
        
        return node;
    }
    
    public TreeNode bstFromPreorder(int[] pre) {
        int n = pre.length;
        if ( n == 0 ) return null;
        
        return createBST(pre,0,n-1);
    }
}
