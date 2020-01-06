package generic_tree;

import java.util.ArrayList;
import java.util.Scanner;

class  GenericTree{
	class Node{
		int data;
		ArrayList<Node> children = new ArrayList<>();
		Node(int data){
			this.data = data;
		}
	}
	
	Node root = null;
	int size = 0;
	Scanner in = new Scanner(System.in);
	
	GenericTree() {
		this.root = insertNode(null, 0);
	}
	
	Node insertNode(Node pNode,int ithchild) {
		if(pNode == null) {
			System.out.println("Enter root node data: ");
		}
		else {
			System.out.println("Enter data for "+ithchild+" child of "+pNode.data);
		}
		Node node = new Node(in.nextInt());
		
		System.out.println("Enter no of children of node "+node.data);
		int childCount = in.nextInt();
		
		for(int i=0;i<childCount;i++) {
			Node childNode = insertNode(node, i);
			node.children.add(childNode);
		}
		
		size++;
		return node;
	
	}

	
	void printTree() {
		printNode(this.root);
	}
	
	void printNode(Node node) {
		System.out.print(node.data+" => ");
		for (int i = 0; i < node.children.size(); i++) {
			System.out.print(node.children.get(i).data+" , ");
		}
		System.out.println("END");
		for (int i = 0; i < node.children.size(); i++) {
			printNode(node.children.get(i));
		}
		
	}
	
}

public class G_tree {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		GenericTree t = new GenericTree();
		t.printTree();
	}

}

