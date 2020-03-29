import java.util.*;
import java.lang.*;
import java.io.*;
class GFG
 {
     
     static boolean subSum(int[] arr,int N,int sum) {
		boolean [][] dp = new boolean[N+1][sum+1];
		
		for(int i=0;i<=N;i++) {
			for(int j=0;j<=sum;j++) {
				if(i==0)
					dp[i][j] = false;
				else if(j == 0)
					dp[i][j] = true;
				
				else if(arr[i-1] > j)
					dp[i][j] = dp[i-1][j];
				else
					dp[i][j] = dp[i-1][j] || dp[i-1][j-arr[i-1]];
			}
		}
		
		return dp[N][sum];
 	}
 	
 	
 	
	public static void main (String[] args) throws Exception
	 {
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    //System.out.println();
	    int T = Integer.parseInt(br.readLine());
	    
	    while(T-- > 0){
	        int n = Integer.parseInt(br.readLine());
	        String[] arr = br.readLine().trim().split(" ");
	        int[] a = new int[n];
	        for(int i=0;i<n;i++) a[i] = Integer.parseInt(arr[i]);
	        
	        int sum = 0;
	        for(int x : a) sum += x;
	        
	        String res = "";
	        
	        if(sum%2 != 0)
	            res = "NO";
	        else
	            res = subSum(a,n,sum/2) ? "YES" : "NO";
	            
	        System.out.println(res);
	        
 	    }
 	 }
}
