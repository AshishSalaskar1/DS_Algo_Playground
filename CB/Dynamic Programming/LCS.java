package p1;

import java.util.*;




public class Main {

	static int LCS(char[] A,char[] B,int m, int n) {
		if(m==0 || n==0 ) return 0;
		
		//last char are same
		if(A[m-1] == B[n-1]) 
			return 1+LCS(A,B,m-1,n-1);
		
		//different last characters
		else
			return Math.max(LCS(A, B, m-1, n), LCS(A, B, m, n-1));
		
	}
	
	static int LCS_dp(char[] A,char[] B,int m, int n) {
		/*
		abbg & agbg
		*   "" 	 a 	 g 	 b 	  g
		""| 0  |0  |0	|0	| 0   
		 a|	0  |   |	|	|	  
		 b|	0  |   |	|	|LCS(ab,agbg)	  
		 b|	0  |   |	|	|	  
		 g|	0  |   |	|	|LCS(abbg,agbg)
		  
		*/
		
		//first extra row n coll for "" empty string
		int[][] dp = new int[m+1][n+1];
		
		//both are empty
		dp[0][0] = 0;
		
		for(int i=0;i<=m;i++) {
			for(int j=0;j<=m;j++) {
				//any one string is ""
				if(i==0 || j==0)
					dp[i][j] = 0;
				
				else if(A[i-1] == B[i-1])
					dp[i][j] = 1 + dp[i-1][j-1];
				
				else
					dp[i][j] = Math.max(dp[i-1][j],dp[i][j-1]);
			}
		}
		
		return dp[m][n];
		
	}
	

    public static void main(String args[]) {
    	Scanner in = new Scanner(System.in);
    
    	char[] a = "abbg".toCharArray();
    	char[] b = "agbg".toCharArray();
    	
    	System.out.println(LCS(a, b, a.length, b.length));
    	System.out.println(LCS_dp(a, b, a.length, b.length));

    	

    }
}

