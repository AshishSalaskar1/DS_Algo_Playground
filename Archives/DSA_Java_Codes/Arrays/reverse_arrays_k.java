package java1;

import java.io.*;
import java.util.*;


public class Sol2 {
	
	
	static void reverseK(int[] a,int n,int k) {
		
		StringBuffer sb = new StringBuffer();
		int i;
		
		if(n<k) {
			for(int j=n-1;j>=0;j--)
				sb.append(a[j]+" ");
			
			System.out.println(sb);
			return;
		}
		
		
		for(i = k-1;i<n;i += k) {
			for(int j=i;j>(i-k);j--) {
				sb.append(a[j]+" ");
			}
		}
		
		int remainingEle = n%k;
		if(remainingEle > 0) {
			for(int j=n-1;j> (n-1-remainingEle);j--)
				sb.append(a[j]+" ");
		}
		System.out.println(sb);
	}
	
	static void reverseArrayK(int[] a,int n,int k) {
		
		for(int i=0; i<n; i+=k) {
			int left = i;
			
			//if n%k != 0 => 
			//Ex n=5,k=2 -- i=0,2,4 -> i=4 left=4,right=6>n
			int right = Math.min(i+k-1,n-1);
			
			int temp;
			while(left<right) {
				temp = a[left];
				a[left] = a[right];
				a[right] = temp;
				left++;
				right--;
			}
		}
		

		for(int x : a) {
			System.out.print(x+" ");
		}
	}
	
	public static void main(String[] args){
		
		int m = 2;
		int n = 8;
//		System.out.println(noOfPaths(m-1, n-1));
//		System.out.println(noOfPathsDp(m, n));
		
//		System.out.println(stairCaseDp(8));
//		System.out.println(stairCase(8));
		
		int[] arr = {1,2,3,4,5};
		
//		reverseK(arr, arr.length, 6);
		reverseArrayK(arr, arr.length, 6);
    	
	}

}

