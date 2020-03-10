package p1;
import java.util.*;

class Node{
	int data;
	Node right,left;
	
	public Node(int data) {
		this.data = data;
		this.right = null;
		this.left = null;
	}
	
	
}

class Tree{
	Node root = null;
	
	 void insertNode(int data) {
		this.root = insertUtil(this.root, data);
	}
	
	 private Node insertUtil(Node node,int data) {
		if(node == null) {
			Node leaf = new Node(data);
			return leaf;
		}
		
		if(data >= node.data)
			node.right = insertUtil(node.right, data);
		else
			node.left = insertUtil(node.left, data);
		
		return node;
	}
	
	void inorder(Node node) {
		if(node != null) {
			inorder(node.left);
			System.out.print(node.data+" ");
			inorder(node.right);
		}
	}
	
	void preorder(Node node) {
		if(node != null) {
			System.out.print(node.data+" ");
			preorder(node.left);
			preorder(node.right);
		}
	}
	
	void postorder(Node node) {
		if(node != null) {
			postorder(node.left);
			postorder(node.right);
			System.out.print(node.data+" ");
		}
	}
	
	int maxDepth(Node node) {
		if(node == null) return 0;
		return 1 + Math.max(maxDepth(node.right), maxDepth(node.left));
	}
	
	void BFS( ) {
		LinkedList<Node> q = new LinkedList<>();
		q.addLast(this.root);
		
		while(!q.isEmpty()) {
			Node node = q.removeFirst();
			System.out.print(node.data+" ");
			
			if(node.left != null) q.addLast(node.left);
			if(node.right != null) q.addLast(node.right);
		}
		
		System.out.println("BFS PRINTED");
	}
}


public class Main {
    public static void main(String args[]) { 
       
    	Scanner in = new Scanner(System.in);
    	Tree a = new Tree();
    	a.insertNode(50);
    	a.insertNode(23);
    	a.insertNode(12);
    	a.insertNode(64);
    	a.insertNode(121);
    	a.insertNode(26);
    	
    	
    	a.inorder(a.root);
    	System.out.println();
    	System.out.println(a.maxDepth(a.root));
    	
    	a.BFS();
    }

}



