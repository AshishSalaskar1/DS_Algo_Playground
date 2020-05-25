// Problem Link : https://leetcode.com/problems/partition-equal-subset-sum

class Solution {
    
    static boolean subsetSum(int[] a,int n,int sum){
        boolean[][] dp = new boolean[n+1][sum+1];
        
        
        for(int i=0;i<=sum;i++)   dp[0][i] = false;
        for(int i=0;i<=n;i++)   dp[i][0] = true;

        for(int i=1;i<=n;i++){
            for(int j=1;j<=sum;j++){
                if (a[i-1] > j)
                    dp[i][j] = dp[i-1][j];
                else
                    dp[i][j] = dp[i-1][j-a[i-1]] || dp[i-1][j];
            }

        }
        
                    
            return dp[n][sum];
    }
    
    public boolean canPartition(int[] nums) {
        
        int n = nums.length;
        if(n == 0 || n== 1) return false;
        
        int sum = 0;
        for(int x : nums)   sum += x;
        
        if(sum % 2 != 0) return false;
        else return subsetSum(nums,n,sum/2);
   
    }
}
