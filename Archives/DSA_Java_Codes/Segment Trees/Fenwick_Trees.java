package p1;

import java.util.*;
import java.io.*;

class Main {
  
	static int[] BIT;
	
	static int getSum(int index) {
		int sum = 0;
		
		//len(BIT) = a + len(arr)
		index = index+1;
		
		while(index > 0) {
			sum += BIT[index];
			index = index - (index & -index);
		}
		
		return sum;
	}
	
	static void updateValue(int index,int diff) {
		index += 1;
		
		int n = BIT.length;
		
		while(index < n) {
			BIT[index] += diff;
			
			index = index + (index & -index);
		}
	}
	
	static void buildBIT(int[] a,int n) {
		//BIT initialized to 0 and size - len(arr)+1
		BIT = new int[n+1];
		
		
		//insert values from arr to BIT
		for(int i=0;i<n;i++) {
			updateValue(i, a[i]);
		}
	}
	
    public static void main(String args[] ) {

    	int[] a = new int[] {1,2,3,4,5,6};
    	
    	buildBIT(a, a.length);
    	
    	//0 indexing 2 => 0,1,2
    	System.out.println(getSum(3));
    	
    	//add 10 to index 3
    	updateValue(3, 10);
    	System.out.println(getSum(2));
    	
       
    }
}

/*
6
2 5 2 -3 4 -1
*/


