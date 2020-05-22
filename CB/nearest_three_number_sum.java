package p1;

import java.util.*;
import java.io.*;


class Main {
	
	//maybe +ve or -ve
	static int nearestTripletSum(int[] a,int sum,int n) {
		
		
		Arrays.sort(a);
		
		int minDiffSF = Integer.MAX_VALUE;
		int nearestSum = 0;
		
		for(int x =0 ; x<n; x++) {
		
			int curEle = a[x];
			int remSum = sum-curEle;
			
//			System.out.println("INDEXX: "+x+":"+curEle+"\n");
			
			int i = 0,j=n-1,diff,tempSum;
			while(i<j) {
				System.out.println(a[i]+" "+a[j] );
				if(i==x) {i++;continue;}
				else if(j==x) {j--;continue;}
				
				tempSum = a[i]+a[j];
				
				diff = Math.abs((tempSum+curEle) - sum);
				if(diff < minDiffSF) {
//					System.out.println("ENTERR " + curEle+" "+a[j]+" DIFF: "+diff);
					nearestSum = tempSum+curEle;
					minDiffSF = diff;
				}
				
				//two pointer based on remSum
				if(tempSum < remSum) i++;
				else	j--;
				
			}
			
		}
		
		return nearestSum;
	}
	
    public static void main(String args[] ) throws IOException{
    	
    	int[] arr = {-1, 2, 1, -4};
    	int n = arr.length;
    	int sum = 1;
    	
    	
    	System.out.println(nearestTripletSum(arr, sum, n));
    	
    
    }
}


