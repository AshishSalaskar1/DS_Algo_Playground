package java1;

import java.util.*;
class Sol2{
	
	
	static int minCoins(int[] coins,int n,int V) {
		if(V == 0) return 0;
		
		int res = Integer.MAX_VALUE;
		int coin = -1;
		
		for(int i=0;i<n;i++) {
			if(coins[i] <= V) {
				int sub_res = minCoins(coins, n, V-coins[i]);
				
				if(sub_res != Integer.MAX_VALUE && sub_res+1 < res)
					res = sub_res + 1;

			}
		}
		
		return res;
	}
	
	static int minCoinDP(int[] coins,int n,int V) {
		int[] dp = new int[V+1];
		Arrays.fill(dp, Integer.MAX_VALUE);
		
		dp[0] = 0;
		
		for(int i=0;i<=V;i++) {
			for(int j=0;j<n;j++) {
				if(coins[j] <= i) {
					int rRes = dp[i - coins[j]];
					if(rRes != Integer.MAX_VALUE && rRes+1 < dp[i])
						dp[i] = rRes +1;
				}
			}
		}
		
		return dp[V];
	}
	
	public static void main(String[] args){
		int[] coins = {9,6,5,1};
		System.out.println(minCoinDP(coins, coins.length, 11));
	}
		
}

