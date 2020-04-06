package p1;

import java.util.*;
import java.lang.*;
import java.io.*;

class Main
 {
	
	static int rodCuttingProblem(int[] profit,int n,int i) {
		if(n == 0) return 0;
		
		if(i==0) return 0;
		
		if(i > n)
			return rodCuttingProblem(profit, n, i-1);
	
		else 
			return Math.max(profit[i-1]+rodCuttingProblem(profit, n-i, i),
							rodCuttingProblem(profit, n, i-1));
	}
	
	static int rodDp(int[] profit,int n) {
		int[][] dp = new int[n+1][n+1];
		
//		X--> size of rod (n)
//		Y -> length of cuts
		
		for(int i=0;i<=n;i++) {
			for(int j=0;j<=n;j++) {
				if(j==0)
					dp[i][j] = 0;
				else if(i==0)
					dp[i][j] = 0;
				else if(i > j)
					dp[i][j] = dp[i-1][j];
				else 
					dp[i][j] =  Math.max(profit[i-1]+dp[i][j-i], 
										 dp[i-1][j]);
			}
		}
		
		
		
		return dp[n][n];
		
	}

		

	public static void main (String[] args) throws Exception
	 {
	    int[] arr = new int[]{-23, 1000, 10, 20, 10, 17, 17}; 
	    
	    System.out.println(rodCuttingProblem(arr,arr.length,arr.length));
	    
	    System.out.println(rodDp(arr, arr.length));
	    
	  
 	 }
}
