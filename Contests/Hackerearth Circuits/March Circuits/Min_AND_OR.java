 package basic;

import java.io.*;
import java.text.*;
import java.util.*;

public class Main {

	static int minXOR(int[] a,int n) {
		int min = Integer.MAX_VALUE;
		
		Arrays.sort(a);
		
		for(int i=0;i<n-1;i++) {
			min = Math.min(min, (a[i]^a[i+1]));
		}
		
		return min;
		
		
	}

	public static void main(String[] args) throws Exception{

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		while(T-->0) {
			int n = Integer.parseInt(br.readLine());
			String[] arr = br.readLine().trim().split(" ");
			
			int[] a = new int[n];
			for(int i=0;i<n;i++)
				a[i] = Integer.parseInt(arr[i]);
			
			System.out.println(minXOR(a,n));
		}
		
		
	}	

}


