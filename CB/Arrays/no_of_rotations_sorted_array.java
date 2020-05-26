package p1;

import java.util.*;
import java.io.*;


class Main {
	
	static int leftRotationsOfSortedArr(int[] a,int n) {
		
		
		int lo=0,hi=n-1;
		int mid=0,prev,next,ele;
		
		while(lo <= hi) {
			
			mid = lo + (hi-lo)/2;
			ele = a[mid];

			prev = (mid + n -1) % n;
			next = (mid+1) % n;

			
			if(ele < a[prev] && ele < a[next])
				break;
			else if( ele >= a[lo])
				lo = mid+1;
			else
				hi = mid-1;
		}
		System.out.println(mid);
		return (n-mid) % n;
	}
	
	static int rightRotationsOfSortedArr(int[] a,int n) {
		
		
		int start=0,end=n-1;
		int mid=0,prev,next,ele;
		
		while(start <= end) {
			
			mid = start + (end-start)/2;
			ele = a[mid];

			prev = (mid + n -1) % n;
			next = (mid+1) % n;
			
			if(ele < a[prev] && ele < a[next])
				return mid;
			else if( ele >= a[start])
				start = mid+1;
			else
				end = mid-1;
		}
		
		return 0;
	
	}
	
    public static void main(String args[] ){
    	
    	int[] arr = {2,2,2,2,1,2};

    	
    	System.out.println(rightRotationsOfSortedArr(arr, arr.length));
    }
}


