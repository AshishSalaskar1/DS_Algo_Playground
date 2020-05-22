package p1;

import java.util.*;
import java.io.*;


class Main {
	
	static boolean threeSum(int[] a,int sum,int n) {
		
		for(int i = 0 ; i < n-2 ; i++) {
			
			HashMap<Integer,Integer> map = new HashMap<>();
			int curSum = sum - a[i];
			for(int j=i+1; j<n; j++) {
				if(map.containsKey(curSum - a[j])) {
					System.out.println(a[i]+" "+a[j]+" "+(curSum-a[j]));
					return true;
				}
				map.put(a[j],j);
			}
			
		}
		
		System.out.println("Not Found");
		return false;
	}
	
    public static void main(String args[] ){
    	
    	int[] arr = {6,2,1,5,4,3,89};
    	int n = arr.length;
    	
    
    	threeSum(arr,900,n);
    }
}


