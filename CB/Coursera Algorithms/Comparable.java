package p1;

import java.util.*;

class A implements Comparable<A>{
	int a,b;
	A(int a,int b){
		this.a = a;
		this.b = b;
	}
	
	public String toString() {
		return "("+this.a+":"+this.b+")";
	}
	
	public int compareTo(A b) {
		return this.a - b.a;
	}
}


public class Main {

	public static void main(String args[]) {
	
		System.out.println("START");
		A[] arr = new A[3];
		arr[0] = new A(112,122);
		arr[1] = new A(112,31);
		arr[2] = new A(124,212);
		
		// Implement Comparable and use method compareTo() in class
		Arrays.sort(arr);
		
		// Pass comparator as argument;
		// sort by a and secondarily by b
		Arrays.sort(arr,(a,b) -> {
			if(a.a - b.a == 0)
				return a.b - b.b;
			else 
				return a.a - b.a;
				
		});
		
		for( A a: arr)
			System.out.println(a);
		
    }
}
