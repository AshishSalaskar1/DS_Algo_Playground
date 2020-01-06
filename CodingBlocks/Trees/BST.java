package bst;


class BST{
	class Node{
		int data;
		Node left,right;
	}
	
	Node root = null;
	
	BST(int[] arr){
		this.root = createBST(arr, 0,arr.length-1);
	}
	
	Node createBST(int[] arr,int lo,int hi) {
		
		int mid = (lo+hi)/2;
		
		if(lo>hi)
			return null;
		
		Node node = new Node();
		node.data = arr[mid];
		node.left =  null;
		node.right =  null;
		
		
		node.left = createBST(arr, lo, mid-1);
		node.right = createBST(arr, mid+1, hi);
		
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

	void addNode(int val) {
		addNode(this.root,val);
	}
	
	private void addNode(Node node,int val) {
		if(val>=node.data) {
			if(node.right == null) {
				Node newNode = new Node();
				newNode.data = val;
				node.right = newNode;
			}
			else {
				addNode(node.right,val);
			}
		}
		else {
			if(node.left == null) {
				Node newNode = new Node();
				newNode.data = val;
				node.left = newNode;
			}
			else {
				addNode(node.left,val);
			}
		}
	}


	public void removeNode(int key) {
		removeNode(this.root,this.root,key);
	}
	
	private void removeNode(Node parent,Node node,int key) {
		if(node.data != key) {
			if(key>=node.data) {
				removeNode(node,node.right,key);
			}
			else {
				removeNode(node,node.left,key);
			}
		}
		else {
			if(node.right == null && node.left == null) {
				if(key>=parent.data) {
					parent.right = null;
				}
				else {
					parent.left = null;
				}
			}
			else if(node.left != null) {
				node = node.left;
			}
			else {
				node = node.right;
			}
			
		}
	}
}

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		BST b = new BST(new int[] {1,2,3,4,5,6,7});
		b.print();
		System.out.println();
		b.addNode(451);
		b.print();
		System.out.println();
		b.removeNode(2);
		b.print();

	}

}

/*
 * 
 * GEEKS FOR GEEKS BST INSERT
 * void addNode(int val) {
		this.root = insertNode(this.root,val);
	}
	
	private Node insertNode(Node node,int val) {
		
		if (node == null) {
			Node newNode = new Node();
			newNode.data = val;
			newNode.left = null;
			newNode.right = null;
			
			return newNode;
		}
		
		if(val >= node.data) {
			node.right = insertNode(node.right,val);
		}
		else {
			node.left = insertNode(node.left,val);
		}
		
		return node;
	}
*/

