package p1;

import java.util.*;
import java.io.*;


class Main {
	
	static void nextGreaterPermutation(int[] a,int n) {
		
		//find first ele in non decreasing order : P
		int p=-1;
		for(int i=n-1;i>0;i--) {
			if(a[i-1] < a[i]) {
				p=i-1;
				break;
			}
		}
		
		if(p == -1) {
			Arrays.sort(a);
			return;
		}
		
		System.out.println(a[p]);
		
		//find first greater element to right of p
		int minI = p;
		for(int i = n-1 ; i > p ; i--) {
			if(a[i] > a[p]) {
				minI = i;
				break;
			}
		}
		
		//swap p and q
		int temp = a[p];
		a[p] = a[minI];
		a[minI] = temp;
		
		//reverse p..n
		Arrays.sort(a,p+1,n);
	
	}
	
	
    public static void main(String args[] ){
    	
    	int[] arr = {6,2,1,5,4,3,0};
    	int n = arr.length;
    	
    	nextGreaterPermutation(arr, n);
    	
    	for(int x : arr)
    		System.out.print(x+" ");
    	
    	
    }
}


