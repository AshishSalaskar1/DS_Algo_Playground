// Problem Link : https://leetcode.com/problems/n-ary-tree-preorder-traversal/
/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    
    static void preOrder(Node node,List<Integer> res){
        if(node == null) return;

        res.add(node.val);
        
        for(Node child : node.children)
            preOrder(child,res);
        
    }
    
    public List<Integer> preorder(Node root) {
        List<Integer> res = new ArrayList<>();
        
        if(root == null)    return res;
        
        preOrder(root,res);
        
        return res;
    }
}


/**
	Iterative Solution
*/
class Solution {
    
 
    public List<Integer> preorder(Node root) {
        LinkedList<Integer> res = new LinkedList<>();
        LinkedList<Node> stack = new LinkedList<>();
        
        if(root == null)    return res;
        
        stack.add(root);
        
        while(!stack.isEmpty()){
            Node node = stack.removeLast();
            res.add(node.val);
            
            Colllections.reverse(node.children);
            for(Node child : node.children)
                stack.add(child);
            
        }
        
 
        return res;
         
    }
}
