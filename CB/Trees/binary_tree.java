package binary_tree;

import java.util.Scanner;

class BinaryTree{
	Scanner in = new Scanner(System.in);
	
	class Node{
		int data;
		Node right;
		Node left;
		
		public Node(int data, Node right, Node left) {
			this.data = data;
			this.right = right;
			this.left = left;
		}
	}
	
	Node root = null;
	BinaryTree(){
		this.root = generateTree(null, false);
	}
	
	Node generateTree(Node parent,boolean isLeftChild) {
		if(parent == null) {
			System.out.println("Enter data for root Node: ");
		}
		else {
			if(isLeftChild) {
				System.out.println("Enter data for left child of "+parent.data);
			}
			else {
				System.out.println("Enter data for right child of "+parent.data);
			}
		}
		
		int val = in.nextInt();
		Node node = new Node(val,null,null);
		
		boolean choice;
		System.out.println("Does "+node.data+ " have a left child");
		choice = in.nextBoolean();
		
		if(choice) {
			node.left = generateTree(node, true);
		}
		
		System.out.println("Does "+node.data+ " have a right child");
		choice = in.nextBoolean();
		
		if(choice) {
			node.right = generateTree(node, false);
		}
		
		return node;
	}
	
	void print() {
		print(this.root);
	}
	
	void print(Node node) {
		String str = "";
		
		if(node.left != null) {
			str = node.left.data+"=>"+str;
		}
		else {
			str = "END =>"+str;
		}
		
		str = str+node.data;
		
		if(node.right != null) {
			str = str+"<="+node.right.data;
		}
		else {
			str = str+" <=END";
		}
		
		System.out.println(str);
		
		//print left and right nodes
		if(node.left != null) {
			print(node.left);
		}
		if(node.right != null) {
			print(node.right);
		}
	}
}

public class Binary {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		BinaryTree b = new BinaryTree();
		System.out.println("END");
		b.print();

	}

}

