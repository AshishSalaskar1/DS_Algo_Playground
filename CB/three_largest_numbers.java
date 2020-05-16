package p1;

import java.util.*;
import java.io.*;


class Main {
	
	static void shiftUpdate(int[] arr,int index,int val) {
		for(int i=0;i<=index;i++) {
			if(i == index)
				arr[i] = val;
			else
				arr[i] = arr[i+1];
		}
	}
	
	static void threeGreatestNumbers(int[] a,int n) {
		int[] res = {Integer.MIN_VALUE,Integer.MIN_VALUE,Integer.MIN_VALUE};
		
		for(int x : a) {
			if(x > res[2])
				shiftUpdate(a,2,x);
			else if(x > res[1])
				shiftUpdate(a, 1, x);
			else if(x > res[0])
				shiftUpdate(a, 0, x);
		}
		
		System.out.println(res[0]+" "+res[1]+" "+res[2]);
	}
	
	static LinkedList<Integer> threeGreatestNumbersList(int[] a,int n) {
		LinkedList<Integer> res = new LinkedList<>();
		res.add(Integer.MIN_VALUE);
		res.add(Integer.MIN_VALUE);
		res.add(Integer.MIN_VALUE);
		
		/*
		 * [5, 10 , 15]
		 * x = 18 -> [10, 15 , 18]
		 * x = 16 -> [15, 16 , 18]
		 */
		
		for(int x : a) {
			if(x > res.get(2)) {
				res.removeFirst();
				res.addLast(x);
			}
			else if(x > res.get(1)) {
				res.removeFirst();
				res.add(1,x);
			}
			else if(x > res.get(0)){
					res.removeFirst();
					//TC to add at 0 is O(N)
					res.add(0,x);
				}
			
		}
		
		return res;
		
	}
	
    public static void main(String args[] ){
    	
    	int[] arr = {45,32,-98,-65,-2,12,65,88,4};
    	int n = arr.length;
    	
    	System.out.println(threeGreatestNumbersList(arr, n));

    }
}


