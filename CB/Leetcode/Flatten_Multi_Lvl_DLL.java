/*
// Definition for a Node.
class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;
};
*/

class Solution {
    
    public Node flatten(Node head) {
        
        Stack<Node> stack = new Stack<>();
        
        Node cur = head;
        Node tail = head;
        
        while( cur != null){
            if(cur.child != null){
                Node child = cur.child;
                if(cur.next != null){
                    stack.push(cur.next);
                    cur.next.prev = null;
                }
                cur.next = child;
                child.prev = cur;
                cur.child = null;
            }
            
            tail = cur;
            cur = cur.next;
        }
        
        while( !stack.isEmpty() ){
            Node node = stack.pop();
            tail.next = node;
            node.prev = tail;
            
            while(node != null){
                tail = node;
                node = node.next;
            }
            
        }
        
        return head;
        
        
    }
}
