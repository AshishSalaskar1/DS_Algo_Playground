package p1;

import java.util.*;
import java.lang.*;
import java.io.*;
class Main
 {
	

	 //{1,2,3} ans {1,2}-{3} = 0
     static int minSubsetSum(int[] a,int n) {
    	 
    	 int sum = 0;
    	 for(int x: a) sum+=x;
    	 
    	 boolean[][] dp = new boolean[n+1][sum+1];
    	 
    	 for(int i=0;i<=n;i++) {
    		 for(int j=0;j<=sum;j++) {
 				if(j==0)
 					dp[i][j] = true;
 				else if(i == 0)
 					dp[i][j] = false;
 				
 				else if(a[i-1] > j)
 					dp[i][j] = dp[i-1][j];
 				else
 					dp[i][j] = dp[i-1][j] || dp[i-1][j-a[i-1]];
 			}
    	 }
    	 
    	 int min = Integer.MAX_VALUE;
    	 

    	 
    	 for(int i=0;i<=sum/2+1;i++) {
    		 if(dp[n][i]) 
    			 min = Math.min(min, Math.abs(sum - (2*i)));
    	 }
    	 
    	 return min;
     }
      
 
     
     static boolean subSum(int[] a,int n,int sum) {
    	 boolean[][] dp = new boolean[n+1][sum+1];
    	 
    	 for(int i=0;i<=n;i++) {
    		 for(int j=0;j<=sum;j++) {
 				if(j==0)
 					dp[i][j] = true;
 				else if(i == 0)
 					dp[i][j] = false;
 				
 				else if(a[i-1] > j)
 					dp[i][j] = dp[i-1][j];
 				else
 					dp[i][j] = dp[i-1][j] || dp[i-1][j-a[i-1]];
 			}
    	 }
    	 
    	 return dp[n][sum];
     }
   
 	

 	
 	
	public static void main (String[] args) throws Exception
	 {
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    //System.out.println();
	    int[] a= {1,2,7};
	    int[] b = {36 ,7 ,46, 40};
	    
	    System.out.println(minSubsetSum(b, b.length));
	    System.out.println(minSubsetSum(a, a.length));
	    

	    
	
	    
	    
 	 }
}
