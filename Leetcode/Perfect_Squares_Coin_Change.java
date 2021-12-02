class Solution {
    
    static ArrayList<Integer> genPerfect(int n) {
		ArrayList<Integer> a = new ArrayList<>();
		
		int i = 1;
		while( i*i <= n) {
			a.add(i*i);
			i++;
		}
		
		return a;
	}
	
	static int coinChange(int sum) {
		ArrayList<Integer> coins = genPerfect(sum);
		int n = coins.size();
		
		int[][] dp = new int[n+1][sum+1];
		
		
		for(int i=0;i<=sum;i++)
			dp[0][i] = Integer.MAX_VALUE-1;
		
		for(int i=0;i<=n;i++)
			dp[i][0] = 0;
		
		for(int i=1;i<=n;i++) {
			for(int j=1;j<=sum;j++) {
				if(coins.get(i-1) <= j)
					dp[i][j] = Math.min(1+dp[i][j-coins.get(i-1)],dp[i-1][j]);
				else 
					dp[i][j] = dp[i-1][j];
			}
		}
		
		return dp[n][sum];
	}
    
    public int numSquares(int n) {
        return coinChange(n);
    }
}
