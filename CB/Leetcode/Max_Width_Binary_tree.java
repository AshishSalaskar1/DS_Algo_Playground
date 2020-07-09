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
    public int widthOfBinaryTree(TreeNode root) {
        if(root == null) return 0;
        
        int max= 0;
        
        LinkedList<TreeNode> q = new LinkedList<>();
        q.add(root);
        
        while( !q.isEmpty() ){
            //remove first and ending nulls
            while( !q.isEmpty() && q.getFirst() == null) q.removeFirst();
            while( !q.isEmpty() && q.getLast() == null) q.removeLast();
            
            int sz = q.size();
            max = Math.max(max,sz);
            
            for(int i=0;i<sz;i++){
                TreeNode node = q.poll();
                
                if(node == null){
                    q.add(null);
                    q.add(null);
                }
                else{
                    q.add(node.left);
                    q.add(node.right);
                }
            }
            
        }
        
        return max;
        
        
    }
}
