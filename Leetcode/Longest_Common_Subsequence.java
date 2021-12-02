// Problem Link : https://leetcode.com/problems/longest-common-subsequence

class Solution {
    
    static int LCS(char[] a,char[] b,int m,int n){
        int[][] dp = new int[m+1][n+1];
        
        for(int i=0;i<=m;i++){
          for(int j=0;j<=n;j++){
              
              if(i==0 || j==0)
                  dp[i][j] = 0;
              
              else if(a[i-1] == b[j-1])
                  dp[i][j] = 1 + dp[i-1][j-1];
              else
                  dp[i][j] = Math.max(dp[i-1][j],dp[i][j-1]);
              
          }  
        }
        
        return dp[m][n];
    }
    
    public int longestCommonSubsequence(String text1, String text2) {
        return LCS(text1.toCharArray(),text2.toCharArray(),text1.length(),text2.length());
    }
}

