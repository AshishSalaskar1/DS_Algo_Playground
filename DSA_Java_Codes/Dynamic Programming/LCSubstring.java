package p1;

import java.util.*;
import java.lang.*;
import java.io.*;


class Main
 {
	static int LCSubstring(String S,String T) {
		char[] s1 = S.toCharArray();
		char[] s2 = T.toCharArray();
		int m = s1.length;
		int n = s2.length;
		
		int[][] dp = new int[m+1][n+1];
		
		int res = Integer.MIN_VALUE;

		for(int i=0;i<=m;i++)
			dp[i][0] = 0;
		for(int i=0;i<=n;i++)
			dp[0][n] = 0;
		
		for(int i=1;i<=m;i++) {
			for(int j=1;j<=n;j++) {
				if(s1[i-1] == s2[j-1])
					dp[i][j] = 1 + dp[i-1][j-1];

				else 
					dp[i][j] = 0;
			}
		}
		
		for(int i=0;i<=m;i++) 
			for(int j=0;j<=n;j++) 
				res = Math.max(res, dp[i][j]);
			
		
		return res;
	}
	
	public static void main (String[] args) throws Exception
	 {
		System.out.println(LCSubstring("ashish", "ash"));
 	 }
}
