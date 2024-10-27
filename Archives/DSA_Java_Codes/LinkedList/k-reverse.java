/*
LL - K REVERSE
Given a head to Linked List L, write a function to reverse the list taking k elements at a time. Assume k is a factor of the size of List.

You need not have to create a new list. Just reverse the old one using head.

Input Format:
The first line contains 2 space separated integers N and K

The next line contains N space separated integral elements of the list.

Constraints:
0 <= N <= 10^6 0 <= K <= 10^6

Output Format
Display the linkedlist after reversing every k elements

Sample Input
9 3
9 4 1 7 8 3 2 6 5
Sample Output
1 4 9 3 8 7 5 6 2

*/


import java.util.*;
public class LinkedList {
	private class Node {
		int data;
		Node next;

		Node(int data, Node next) {
			this.data = data;
			this.next = next;
		}
	}

	private Node head;
	private Node tail;
	private int size;

	public LinkedList() {
		this.head = null;
		this.tail = null;
		this.size = 0;
	}

	public LinkedList(Node head, Node tail, int size) {
		this.head = head;
		this.tail = tail;
		this.size = size;
	}


	// O(1)
	public void addLast(int data) {
		Node node = new Node(data, null);

		if (this.size() == 0) {
			this.head = node;
			this.tail = node;
		} else {
			this.tail.next = node;
			this.tail = node;
		}

		this.size++;
	}

	// O(n)
	public void addAt(int idx, int data) throws Exception {
		if (idx < 0 || idx > this.size()) {
			throw new Exception("Invalid arguments");
		}

		if (idx == 0) {
			this.addFirst(data);
		} else if (idx == this.size()) {
			this.addLast(data);
		} else {
			Node nm1 = this.getNodeAt(idx - 1);
			Node n = nm1.next;

			Node node = new Node(data, n);
			nm1.next = node;

			this.size++;
		}
	}


	// O(n)
	public void display() {
		Node node = this.head;

		while (node != null) {
			System.out.print(node.data + " ");
			node = node.next;
		}

	}

	private Node reverseUtil(Node head,int k){
		Node curr = head;
		Node next = null;
		Node prev = null;

		int count =0;
		while(count < k && curr!=null){
			next = curr.next;
			curr.next = prev;
			prev = curr;

			curr = next;
			count++;
		}
		
		if(next != null){
			head.next = reverseUtil(next,2);
		}

		return prev;

	}
	
	public void reverse(int k){

    	this.head = reverseUtil(this.head,k);
    
	}
	
 

	public static void main(String[] args) throws Exception {
			
			Scanner scn = new Scanner(System.in);
			int N = scn.nextInt();
	        int k = scn.nextInt();
			
			LinkedList list = new LinkedList();

			for (int i = 0; i < N; i++) {
				list.addLast(scn.nextInt());
			}

		    list.reverse(k);
			list.display();
	}
}
