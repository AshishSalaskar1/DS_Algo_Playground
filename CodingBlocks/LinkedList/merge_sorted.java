package Basic;

import Basic.LinkedList.Node;

class LinkedList{
	class Node{
		int data;
		Node next;
		
		Node(int data, Node next) {
			this.data = data;
			this.next = next;
		}
	}

	Node head;
	Node tail;
	int size;
	
	LinkedList(){
		head = null;
		tail = null;
		size = 0;
	}
	
	void addFirst(int val) {
		Node temp = new Node(val,head);
		if(head == null) {
			head = temp;
			tail = temp;
		}
		else {
//			temp.next = head;
			head = temp;
			
		}
		size++;
	}
	
	void addLast(int val) {
		Node temp = new Node(val,null);
		if(head == null) {
			head = temp;
			tail = temp;
		}
		else {
				tail.next = temp;
				tail = temp;
		}
		size++;
			
	}
	
	Node getNodeAt(int ix) {
		
		Node it = head;
		
		for(int i=0;i<ix;i++) {
			it = it.next;
		}
		
		return it;
		
		
	}
	
	int getAt(int ix) {
		return this.getNodeAt(ix).data;
	}
	
	void addAt(int ix,int val) {
			
		
		if(ix == 1) {
			this.addFirst(val);
		}
		else if(ix  == this.size) {
			this.addLast(val);
		}
		else {	
			Node temp = new Node(val,null);
			Node it = this.getNodeAt(ix);
			
			temp.next = it.next;
			it.next = temp;
			size++;
		}
		
		
		
	}
	
	int removeFirst() {
		
		if (this.size == 0) {
			return -1;
		}
		int res = head.data;
		
		if(this.size == 1) {
			head =null;
			tail=null;

		}
		else {
			head = head.next;
		}
		
		size--;
		return res;
	}
	
	int removeLast(){
		if (this.size == 0) 
			return -1;
		
		int res = tail.data;
		
		if(this.size == 1) {
			head =null;
			tail=null;	
		}
		else {
			Node it = this.getNodeAt(this.size - 2);
			it.next = null;
			
			tail = it;
		}
		
		size--;
		return res;
	}
	
	
	void print() {
		Node temp = head;
		while(temp != null) {
			System.out.print(temp.data+"=>");
			temp = temp.next;
		}
		System.out.println();
		
	}
	
	void reversePtr() {
		
		
		
		Node temp = head;
		Node curr = temp;
		Node next= null;
		Node prev = null;
		
		while(curr != null) {
			next = curr.next;
			curr.next = prev;
			prev = curr;
			curr = next;
			
		}
		
		tail = head;
		head =  prev;
		
	}
	
	
	
	Node reverseKUtil(Node head,int k) {
		
		Node curr = head;
		Node prev = null;
		Node next = null;
		int count = 0;
		
		while(count<k && curr!= null) {
			next = curr.next;
			curr.next = prev;
			prev = curr;
			
			curr = next;
			count++;
		}
		
		if(next!=null) 
			head.next = reverseKUtil(next,k);
		
		
		return prev;

	}
	
	void reverseK(int k) {
		this.head = reverseKUtil(this.head,k);
	}
	

	
	 static Node merge(Node h1, Node h2) 
	    { 
	        if (h1 == null) 
	            return h2; 
	        if (h2 == null) 
	            return h1; 
	  

	        if (h1.data < h2.data) { 
	            h1.next = merge(h1.next, h2); 
	            return h1; 
	        } 
	        else { 
	            h2.next = merge(h1, h2.next); 
	            return h2; 
	        } 
	    } 
	

}

public class Main {


	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		LinkedList l1 = new LinkedList();
		LinkedList l2 = new LinkedList();


//		l1.addLast(1);
//		l1.addLast(3);
//		l1.addLast(5);
//		l1.addLast(7);
		
		l2.addLast(2);
		l2.addLast(4);
		l2.addLast(6);
		l2.addLast(8);
		l2.addLast(9);
		
	
		l1.print();
		l2.print();
//		l1.mergeSorted(l2);
		l1.head = l1.merge(l1.head,l2.head);
		l1.print();
	
	

		
	
	
		
		

		
	}

}

