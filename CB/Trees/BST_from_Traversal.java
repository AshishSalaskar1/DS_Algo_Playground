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

class BuildTree{
	Node root;
	int preIndex = 0;
	
	private int searchInorder(int[] arr,int start,int end,int val) {
		int ans = -1;
	
		int i;
		for( i=start;i<=end;i++) {
			if(arr[i] == val)
				return i;
		}
		
		return i;
	}
	
	Node buildTreeFromInPre(int[] inorder,int[] preorder,int inStart,int inEnd) {
		if(inStart > inEnd) return null;
		
		Node node = new Node(preorder[preIndex++]);
		
		//only one ele in inorder arr
		if(inStart == inEnd)  return node;
		
		int inorderSplitIndex = searchInorder(inorder, inStart, inEnd, node.data);
		
		
		//build subtree
		node.left = buildTreeFromInPre(inorder, preorder, inStart,inorderSplitIndex-1);
		node.right = buildTreeFromInPre(inorder, preorder, inorderSplitIndex+1, inEnd);
		
		return node;
	}
	
	void preorder(Node node) {
		if(node != null) {
			System.out.print(node.data+" ");
			preorder(node.left);
			preorder(node.right);
		}
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
    	a.preorder(a.root);
    	System.out.println();
    	a.postorder(a.root);
    	System.out.println();
//    	System.out.println(a.maxDepth(a.root));
    	
    	int[] inorder = {12 ,23 ,26 ,50, 64, 121 };
    	int[] preorder = {50 ,23 ,12 ,26 ,64 ,121 };
    	int[] postorder = {12, 26,23 ,121 ,64 ,50};
    	
    	BuildTree t = new BuildTree();
    	t.root = t.buildTreeFromInPre(inorder, preorder, 0, inorder.length-1);
    	t.preorder(t.root);
    	
//    	a.BFS();
    }

}



