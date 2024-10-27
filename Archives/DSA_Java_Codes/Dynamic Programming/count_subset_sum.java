package p1;

import java.util.*;
import java.lang.*;
import java.io.*;
class Main
 {
	
	static int recursiveCountSub(int[] a,int n,int sum) {
		if(sum == 0)
			return 1;
		
		if(n == 0)
			return 0;
		
		if(a[n-1] > sum)
			return recursiveCountSub(a, n-1, sum);
		
		return recursiveCountSub(a, n-1, sum-a[n-1])
				+ recursiveCountSub(a, n-1, sum);
	}
     
     static int CountsubSum(int[] arr,int N,int sum) {
		int [][] dp = new int[N+1][sum+1];
		
		// i : N
		// j : Sum
		
		for(int i=0;i<=N;i++) {
			for(int j=0;j<=sum;j++) {
				//n becomes 0
				if(j==0)
					dp[i][j] = 1;
				
				//sum becomes 0
				else if(i == 0)
					dp[i][j] = 0;
				
				else if(arr[i-1] > j)
					dp[i][j] = dp[i-1][j];
				
				else
					dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]];
			}
		}
		
		return dp[N][sum];
 	}
 	

 	
 	
	public static void main (String[] args) throws Exception
	 {
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    //System.out.println();
	    int[] a= {2,3,5,6,8,9,10};
	    
	    System.out.println(CountsubSum(a, a.length, 10));
	    System.out.println(recursiveCountSub(a,a.length,10));
	    
	    
 	 }
}
