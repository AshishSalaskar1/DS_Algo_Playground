package basics;

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
	
	
}

public class Basics {

	public static void main(String[] args) {
		
		LL a = new LL();
		a.addLast(1);
		a.addLast(2);
		a.addLast(3);
		a.addLast(4);
		a.printList();
		
//		LL.Node n = a.getNodeAt(4);
//		System.out.println(n.data);

		a.insertAt(1,45);
		a.printList();
//		
//		a.deleteKey(45);
//		a.printList();
//		
//		a.deleteAtPos(4);
//		a.printList();
		
		System.out.println(a.search(450));
		
		
	}

}

