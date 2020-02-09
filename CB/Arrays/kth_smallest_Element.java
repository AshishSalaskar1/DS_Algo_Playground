/*package whatever //do not write package name here */
package p1;

import java.util.*;
import java.io.*;

class Solution {
	

	
	static int partition(int[] a,int l,int r) {
		int pivot = a[r];
		int pIndex = l;
		
		for(int i=l;i<r;i++) {
			if(a[i] <= pivot) {
				int temp = a[i];
				a[i] = a[pIndex];
				a[pIndex] = temp;
				
				pIndex++;
			}
		
		}
		
		int temp = a[r];
		a[r] = a[pIndex];
		a[pIndex] = temp;
	
		return pIndex;
		
	}
	
	static int kthsmallest(int[] arr,int l,int r,int k) {
		if(k>0 && k<= r-l+1) {
			
			int pivot = partition(arr, l, r);
			
			if(pivot-l == k-1)
				return arr[pivot];
			
			if(pivot-l > k-1)
				return kthsmallest(arr, l, pivot-1, k);
			else
				return kthsmallest(arr, pivot+1, r, l+k-pivot-1);
		}
		else
			return Integer.MAX_VALUE;
	}

    
	public static void main (String[] args) {
	
		int[] arr = {8,3,1,2,9};
		System.out.println(kthsmallest(arr, 0, arr.length-1, 3));
		
	}
}
