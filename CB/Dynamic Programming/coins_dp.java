package p1;

import java.util.*;
import java.lang.*;
import java.io.*;

class Main
 {
	
//	static int[] dp = new int[4000];
//	static int[] len = new int[3];


	//min coins
	static int DP(int[] a,int n,int sum){
        int[][] dp = new int[n+1][sum+1];
        
        for(int i=0;i<=sum;i++)
        	dp[0][i] = Integer.MAX_VALUE-1;
        
        for(int i=0;i<=n;i++)
        	dp[i][0] = 0;
        
        
        
        for(int i=1;i<=n;i++){
            for(int j=1;j<=sum;j++){
                
                if(a[i-1] <= j) 
                	dp[i][j] = Math.min(1 + dp[i][j-a[i-1]] , dp[i-1][j]);
                
                else 
                	dp[i][j] = dp[i-1][j];
            }
        }
        
        return dp[n][sum];
    }
	
	//no of ways to make change
	static int DP_ways(int[] a,int n,int sum){
        int[][] dp = new int[n+1][sum+1];
        
        for(int i=0;i<=sum;i++)
        	dp[0][i] = 0;
        
        for(int i=0;i<=n;i++)
        	dp[i][0] = 1;
        
        
        for(int i=1;i<=n;i++){
            for(int j=1;j<=sum;j++){
                
                if(a[i-1] <= j) 
                	dp[i][j] =dp[i][j-a[i-1]] + dp[i-1][j];
                
                else 
                	dp[i][j] = dp[i-1][j];
            }
        }
        
        return dp[n][sum];
    }
	

	public static void main (String[] args) throws Exception
	 {
	    int[] arr = new int[]{-23, 1000, 10, 20, 10, 17, 17}; 
	    
	    int[] a = {1,2,3};
	    System.out.println(DP(a, a.length, 5));

	    int[] b = {1,2,3};
	    System.out.println(DP_ways(b,b.length,5));
	    
	    
	    
	  
 	 }
}
