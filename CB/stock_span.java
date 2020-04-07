package p1;

import java.util.*;
import java.lang.*;
import java.io.*;

class Main
 {
	static void stockSpan(int[] price,int n) {
		int[] span = new int[n];
		span[0] = 1;
		
		//put indices in stack
		Stack<Integer> stack = new Stack<>();
		stack.push(0);
		
		for(int i=1;i<n;i++) {

			while(!stack.isEmpty() && price[stack.peek()] <= price[i])
				stack.pop();
				
			span[i] = stack.isEmpty() ? (i+1) : (i-stack.peek());
			stack.push(i);
			
		}
		
		for(int x : price) 
			System.out.print(x+" ");
		
		System.out.println();
		
		for(int x : span) 
			System.out.print(x+" ");
		
 	}
	

	

	public static void main (String[] args) throws Exception
	 {
		int[] arr = {100,80,60,70,60,75,85};
		
		stockSpan(arr, arr.length);
	  
 	 }
}
