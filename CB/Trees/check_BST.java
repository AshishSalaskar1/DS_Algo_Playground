package p1;

import java.util.*;
import java.io.*;

class BST{
	static class Node{
		int value;
		Node left,right;
		
		Node(int val){
			value = val;
			left = right = null;
		}
	}
	
	Node root = null;
	
	Node insert(Node node,int val) {
		if(node == null)
			return new Node(val);
		
		if(val < node.value)
			node.left = insert(node.left, val);
		else
			node.right = insert(node.right, val);
		
		return node;
	}
	
	boolean isBST(Node node,int min,int max) {
		if(node == null)
			return true;
		
		int val = node.value;
		
		if(val < min || val > max )
			return false;
		
		else
			return isBST(node.left, min, val-1) && 
				   isBST(node.right, val, max);
	}
}

class Main
{	
	
	public static void main (String[] args) throws Exception
	 {

		BST t = new BST();
		t.root = t.insert(t.root, 10);
		t.root = t.insert(t.root, 23);
		t.root = t.insert(t.root, 45);
		t.root = t.insert(t.root, 5);
		t.root = t.insert(t.root, 9);
		t.root = t.insert(t.root, 4);
		t.root.left.right.value = 84;
		System.out.println(t.root.left.right.value);
		
		System.out.println(t.isBST(t.root, Integer.MIN_VALUE, Integer.MAX_VALUE));
		
		
		
 	 }
}
