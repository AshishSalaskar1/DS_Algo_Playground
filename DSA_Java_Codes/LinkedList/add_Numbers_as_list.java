package basics;

//Add numbers represented by linked lists
import java.util.*;

class Node{
	int data;
	Node next;
	
	Node(int data) {
		this.data = data;
		this.next = null;
	}
	
	Node() {
//		this.data = null;
		this.next = null;
	}
}

class LL{
	
	Node head;
	
	void printList() {
         System.out.println("YEAH");
		Node temp = head;
		while(temp != null) {
			System.out.print(temp.data+"->");
			temp = temp.next;
			
		}
		System.out.println();
	}
	
	
	
	void addFirst(int val) {
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
			this.addFirst(val);
			return;
		}
		
		Node prevNode = this.getNodeAt(pos-1);
		
		node.next = prevNode.next;
		prevNode.next = node;
		
	}

}

public class Basics {
	static void printList(Node node) {

        System.out.println("YEAH_NEW");
		Node temp = node;
		int count = 0;
		while(temp != null) {
			
			if(count > 10) {
				System.out.println("F**ked up");
				System.exit(0);
			}
			System.out.print(temp.data+"->");
			temp = temp.next;
			count ++;
		}
		System.out.println();
	}
	
	static Node addList(Node h1,Node h2){
		Node res= null;
		Node prev = null;
        // Node temp = null;
		int carry = 0,sum;
		
		while(h1!=null || h2!=null) {
			int a = h1!=null ? h1.data : 0;
			int b = h2!=null ? h2.data : 0;
			
			sum = a+b+carry;
			carry = sum>=10 ? 1 : 0;
			sum = sum%10;
			
			Node temp = new Node(sum);
			//if first node of res
			if(res == null) res = temp;
			else prev.next = temp;
			
			prev = temp;
			
			if(h1!=null) h1 = h1.next;
			if(h2!=null) h2 = h2.next;
			
		}
		
		if(carry > 0) prev.next = new Node(carry);
		
		
		return res;
	}

	public static void main(String[] args) {
		
		//345
		LL a = new LL();
		a.addFirst(3);
		a.addFirst(4);
		a.addFirst(5);

		a.printList();
		
		//45
		LL b = new LL();
		b.addFirst(4);
		b.addFirst(5);;

		b.printList();
		
		Node res = addList(a.head, b.head);
		
        // printList(b.head);
		printList(res);
		

		
	}

}


