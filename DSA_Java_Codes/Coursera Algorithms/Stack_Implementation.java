package p1;

import java.util.*;

//Stack using Linked List
class StackLL<T>
{
	class Node{
		T data;
		Node next;
		
		Node(T val){
			this.data = val;
		}
	}
	
	private Node head = null;
	

	void push(T val) {
		Node node = new Node(val);

		if(head == null) {
			head = node;
			return;
		}
		
		node.next = head;
		head = node;
	}
	

	T pop() {
		if(head == null)
			return null;
		
		Node removedNode = head;
		head = head.next;
		return removedNode.data;
	}
	
}

class StackArr<T>{
	int size;
	T[] stack;
	int top = -1;
	
	@SuppressWarnings("unchecked")
	StackArr(int n){
		this.size = n;
		//type casting needed bcoz : In java u cannot create array using Generics
		stack = (T[]) new Object[n];
	}
	
	void push(T val) {
		stack[++top] = val;
	}
	
	T pop() {
		if(top == -1)
			return null;
		
		return stack[top--];
	
	}
}

public class Main {

	public static void main(String args[]) {
		StackArr<Integer> stack = new StackArr<>(10);
		
		stack.push(1);
		stack.push(2);
		stack.push(3);
		
		System.out.println(stack.pop());
		System.out.println(stack.pop());
		System.out.println(stack.pop());
		System.out.println(stack.pop());
		System.out.println(stack.pop());
		
    }
}