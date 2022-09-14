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
	
	void deleteKey(int key) {
		Node temp = head;
		Node prev = null;
		if(head == null) return;
		
		if(head.data == key) {
			head = head.next;
			return;
		}
		
		
		while(temp != null) {
			if(temp.data == key) break;
			
			prev = temp;
			temp = temp.next;
		}
		
		if(temp != null) {
			prev.next = temp.next;
		}
		
		
	}
	
	void deleteAtPos(int pos) {
		if(pos == 1) {
			head = head.next;
			return;
		}
		
		Node temp = head;
		Node prev = null;
		
		for (int i = 1; i < pos; i++) {
			prev = temp;
			temp = temp.next;
		}
		
		prev.next = temp.next;
		
	}
	
	int search(int key) {
		if (head == null) return -1;
		
		int pos = 1;
		
		Node temp = head;
		while(temp != null) {
			if(temp.data == key) return pos;
			
			temp = temp.next;
			pos++;
		}
		
		return -1;
	}
	
	void reverse() {
		if(head == null) return;
		
		Node cur = head;
		Node prev = null;
		Node next;
		
		while(cur != null) {
			next = cur.next;
			cur.next = prev;
			prev = cur;
			cur = next;
		}
		
		head = prev;
		
	}
	
	void reverseRecursive(Node cur,Node prev) {
		if(cur == null) return;
		
		//last element of linked list
		if(cur.next == null) {
			cur.next = prev;
			head = cur;
			return;
		}
		
		Node next = cur.next;
		cur.next = prev;
		
		reverseRecursive(next, cur);
		
	}
	
	void printMiddle() {
		if(head == null) return;
		
		Node slow = head;
		Node fast = head;
		
		while(fast != null && fast.next != null) {
			slow = slow.next;
			fast = fast.next.next;
		}
		
		System.out.println(slow.data);
	}
	
	void rotateList(int k) {
		Node cur = head;
		
		for(int i=1;i<k;i++) {
			if(cur == null) return;
			cur = cur.next;
		}
		
		Node kthNode = cur;
		
		//get last node
		while(cur.next!=null) cur = cur.next;
		
		cur.next = head;
		head = kthNode.next;
		
		kthNode.next = null;

	}
	
	Node reverseK(Node head,int k) {
		Node cur = head;
		Node prev = null;
		Node next = null;
		
		int i = 0;
		while(i<k && cur != null) {
			next = cur.next;
			cur.next = prev;
			prev = cur;
			cur = next;
			i++;
		}
		
		if(next!=null)
			head.next = reverseK(next,k);
		
		return prev;
		
	}
	
	
}

public class Basics {

	public static void main(String[] args) {
		
		LL a = new LL();
		a.addLast(8);
		a.addLast(5);
//		a.addLast(3);
//		a.addLast(4);
//		a.addLast(5);
//		a.addLast(6);
//		a.addLast(7);
//		a.addLast(8);
		a.printList();
		
//		LL.Node n = a.getNodeAt(4);
//		System.out.println(n.data);

//		a.insertAt(1,45);
//		a.printList();
//		
//		a.deleteKey(45);
//		a.printList();
//		
//		a.deleteAtPos(4);
//		a.printList();
		
//		System.out.println(a.search(450));
		
//		a.reverse();
//		a.printList();
//		
//		a.reverseRecursive(a.head,null);
//		a.printList();
		
//		a.printMiddle();
//		
//		a.rotateList(4);
//		a.printList();
		
		a.head = a.reverseK(a.head, 1);
		a.printList();
		
	}

}

