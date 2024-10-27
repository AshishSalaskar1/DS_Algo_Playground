package java1;
import java.util.*;


class Sol2{
	

	static int tsp(int mask,int pos,int[][] cost,int max_vis,int n) {
		if(mask == max_vis)
				return cost[pos][0];
		
		int res = Integer.MAX_VALUE;
		
		for(int city=0;city<n;city++) {
			int rMask = (1<<city);
			
			if((rMask&mask) == 0) {
				int ans = cost[pos][city] + tsp((mask | rMask), city, cost, max_vis, n);
			
				res = Integer.min(ans, res);
			}
		}
		
		return res;
	}
	
	static int tsp(int mask,int pos,int[][] cost,int[][] dp,int max_vis,int n) {
		if(mask == max_vis)
				return cost[pos][0];
		
		if(dp[mask][pos] != -1)
			return dp[mask][pos];
		
		int res = Integer.MAX_VALUE;
		
		for(int city=0;city<n;city++) {
			int rMask = (1<<city);
			
			if((rMask&mask) == 0) {
				int ans = cost[pos][city] + tsp((mask | rMask), city, cost, max_vis, n);
			
				res = Integer.min(ans, res);
			}
		}
		
		dp[mask][pos] = res;
		return res;
	}

	
	public static void main(String[] args){
		int n = 4;
		int cost[][] = {
				{0,20,42,28},
				{20,0,30,34},
				{42,30,0,10},
				{25,34,10,0}
		};
		
		//all bits set to 1 : 2^n -1
		int VIS_ALL = (1<<n)-1;
		
		//initial mask: 00001 -> first city visited as source
		System.out.println(tsp(1, 0, cost, VIS_ALL, n));
		
		int[][] dp = new int[10000][10000];
		
		for(int i=0;i<(1<<n);i++) 
			for(int j=0;j<n;j++) 
				dp[i][j] = -1;
			
		System.out.println(tsp(1, 0, cost, dp, VIS_ALL, n));
		
		
	}
		
}

