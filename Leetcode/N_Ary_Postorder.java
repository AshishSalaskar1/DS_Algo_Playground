// Problem Link : https://leetcode.com/problems/n-ary-tree-postorder-traversal/
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
    
    static void postOrder(Node node,List<Integer> res){
        if(node == null) return;
        
        for(Node child : node.children)
            postOrder(child,res);
        
        res.add(node.val);
    }
    
    public List<Integer> postorder(Node root) {
        List<Integer> res = new ArrayList<>();
        
        if(root == null)    return res;
        
        postOrder(root,res);
        
        return res;
    }
}


/**
	Iterative Solution
*/
class Solution {
    
 
    public List<Integer> postorder(Node root) {
        LinkedList<Integer> res = new LinkedList<>();
        LinkedList<Node> stack = new LinkedList<>();
        
        if(root == null)    return res;
        
        stack.add(root);
        
        while(!stack.isEmpty()){
            Node node = stack.removeLast();
            res.addFirst(node.val);
            
            for(Node child : node.children)
                stack.add(child);
            
        }
        
        
        return res;
        
        
    }
}
