package basics;

import java.util.*;



class LL{
	class Node{
		int data;
		Node next;
		
		Node(int data) {
			this.data = data;
			this.next = null;
		}
		
		Node() {
//			this.data = null;
			this.next = null;
		}
	}
	
	Node head;
	
	void printList() {
		Node temp = head;
		while(temp != null) {
			System.out.print(temp.data+"->");
			temp = temp.next;
			
		}
		System.out.println();
	}
	
	void addFist(int val) {
		Node node = new Node(val);
		
		if(head == null) {
			head = node;
			return;
		}
		
		node.next = head;
		head = node;
	}
	
	void addLast(int val) {
		Node node = new Node(val);
		
		if(head == null) {
			head = node;
			return;
		}
		
		Node temp = head;
		Node prev = null;
		
		while(temp != null) {
			prev = temp;
			temp = temp.next;
		}
		
		prev.next = node;
		
	}
	
	Node getNodeAt(int pos) {	
		Node temp = head;
		
		for(int i=1;i<pos;i++) {
			temp = temp.next;
		}
		
		return temp;
		
	}
	
	void insertAt(int pos,int val) {
		Node node = new Node(val);
		

		if(pos == 1) {
			this.addFist(val);
			return;
		}
		
		Node prevNode = this.getNodeAt(pos-1);
		
		node.next = prevNode.next;
		prevNode.next = node;
		
	}

	
	static Node mergeList(Node h1, Node h2) 
    { 
        if (h1 == null) 
            return h2; 
        if (h2 == null) 
            return h1; 
  
        // start with the linked list 
        // whose head data is the least 
        if (h1.data < h2.data) { 
            h1.next = mergeList(h1.next, h2); 
            return h1; 
        } 
        else { 
            h2.next = mergeList(h1, h2.next); 
            return h2; 
        } 
    } 
	
	
}

public class Basics {

	public static void main(String[] args) {
		
		LL a = new LL();
		a.addLast(2);
		a.addLast(3);
//		a.addLast(6);

		LL b = new LL();
		b.addLast(5);
		b.addLast(10);
//		b.addLast(78);
		
		a.printList();
		b.printList();
		
		LL c = new LL();
		c.head = LL.mergeList(a.head,b.head);
		c.printList();
		

		
	}

}

