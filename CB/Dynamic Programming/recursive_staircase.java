package java1;

import java.util.*;


public class Sol2 {
	
	
	//paths from (0,0) to (m,n) of matrix
	static int noOfPaths(int x,int y) {
		if(x==0 && y==0)
			return 1;
		if(x<0 || y<0)
			return 0;
			
		return noOfPaths(x-1, y)+noOfPaths(x, y-1);
	}
	
	static int noOfPathsDp(int m,int n) {
		int[][] dp = new int[m][n];
		
		//if you are at (x,0) then u can reach only one way i.e always go up ie (x--,y)
		for(int i=0;i<m;i++)
			dp[i][0] = 1;
		
		//if you are at (0,x) then u can reach only one way i.e always go side ie (x,y--)
		for(int i=0;i<n;i++)
			dp[0][i] = 1;
		
		for(int i=1;i<m;i++) {
			for(int j=1;j<n;j++) {
				dp[i][j] = dp[i-1][j] + dp[i][j-1];
			}
		}
		
		
		return dp[m-1][n-1];
	}
	
	
	//You can climpb 1 or 2 stairs at a time
	static int stairCase(int n) {
		if(n==1 || n==0)
			return 1;
		
		if(n<0)
			return 0;
		
		return stairCase(n-1)+stairCase(n-2);
	}
	
	static int stairCaseDp(int n) {
		int[] dp = new int[n+1];
		
		dp[0] = 1;
		dp[1] = 1;
		
		for(int i=2;i<=n;i++)
			dp[i] = dp[i-1] + dp[i-2];
		
		return dp[n];
	}
	
	public static void main(String[] args){
		
		int m = 2;
		int n = 8;
//		System.out.println(noOfPaths(m-1, n-1));
//		System.out.println(noOfPathsDp(m, n));
		
		System.out.println(stairCaseDp(8));
		System.out.println(stairCase(8));
    	
	}

}

