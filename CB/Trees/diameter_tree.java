/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    
    static class Int{
        int value = 0;
        
        Int(int val){
            this.value = value;
        }
    }
    
    static int diameter(TreeNode node,Int res){
        if(node == null) return 0;
        
        int l = diameter(node.left,res);
        int r = diameter(node.right,res);
        
        int temp = Math.max(l,r) +1 ;
	//only for non negative edges
        //int ans = Math.max(temp,l+r+1);
        res.value = Math.max(l+r+1,res.value);
        
        return temp;
    }
    
    public int diameterOfBinaryTree(TreeNode root) {
        Int res = new Int(Integer.MIN_VALUE);
        diameter(root,res);
        return (res.value == 0) ? 0 : res.value -1 ;
    }
}
