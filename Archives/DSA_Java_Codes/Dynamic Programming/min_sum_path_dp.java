 static int minPath(int[][] a,int m,int n) {
		int[][] dp = new int[m+1][n+1];
		
		
		for(int i=0;i<m;i++) {
			for(int j=0;j<n;j++) {
				if(i==0 && j==0)
                    dp[i][j] = a[0][0];
				else if(i<0 || j <0)
					dp[i][j] = Integer.MAX_VALUE;
				else if(i==0 && j>0)
					dp[i][j] = a[i][j] + dp[i][j-1];
				else if(j==0 && i>0)
					dp[i][j] = a[i][j] + dp[i-1][j];
				else
					dp[i][j] = a[i][j] + Math.min(dp[i-1][j], dp[i][j-1]);
			}
		}
		
		return dp[m-1][n-1];
      
	}

 static int[][] dp;

     static int minPath(int[][] a,int i,int j) {
         
        if(dp[i][j] != -1) return dp[i][j];
         
		if(i==1 && j==1)
            return dp[i][j] = a[0][0];
         
        if(i<=0 || j<=0)
            return dp[i][j] = Integer.MAX_VALUE;
         
        return dp[i][j] = a[i-1][j-1] + Math.min(minPath(a,i-1,j),minPath(a,i,j-1));
	}