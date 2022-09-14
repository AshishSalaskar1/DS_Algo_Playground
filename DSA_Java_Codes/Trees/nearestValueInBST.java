package p1;

import java.util.*;
import java.lang.*;
import java.io.*;

class BST{
	static class Node{
			int data;
			Node left,right;
			public Node(int data) {
				this.data = data;
				this.left = null;
				this.right = null;
			}
	}
		
	Node head = null;
		
	Node insertBST(Node node,int val) {
		if(node == null)
			return new Node(val);
			
		if(val >= node.data)
			node.right = insertBST(node.right, val);
		else
			node.left = insertBST(node.left, val);
			
		return node;
	}
		
	boolean findBST(Node node,int val) {
		if(node == null)
			return false;
			
		if(node.data == val)
			return true;
		else if(val < node.data)
			return findBST(node.left, val);
		else 
			return findBST(node.right, val);
			
	}
	
	int findNearestInBST(Node node,Node parent,int val) {
			
		if(node == null)
			return parent.data;
		
		if(node.data == val)
			return node.data;
		
		else if(val < node.data)
			return findNearestInBST(node.left,node,val);
		else 
			return findNearestInBST(node.right,node,val);
			
	}
	
	
}


class Main
 {
	public static void main (String[] args) throws Exception
	 {
		BST t = new BST();
		t.head = t.insertBST(t.head, 10);
		t.head = t.insertBST(t.head, 5);
		t.head = t.insertBST(t.head, 15);
		t.head = t.insertBST(t.head, 5);
		t.head = t.insertBST(t.head, 2);
		t.head = t.insertBST(t.head, 1);
		t.head = t.insertBST(t.head, 22);
		t.head = t.insertBST(t.head, 13);
		t.head = t.insertBST(t.head, 14);
		
		System.out.println(t.findBST(t.head, 12));
		System.out.println(t.findNearestInBST(t.head, t.head, 25));
		
	  
 	 }
}
