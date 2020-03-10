package p1;

import java.util.*;




public class Main {
	static int count = 0;
	
	static boolean isSubsetSum(int[] arr,int m,int sum) {
		if(sum == 0) return true;
		
		if(m==0 && sum!=0) return false;
		
		//cur ele > needed sum
		if(arr[m-1] > sum) return false;
		
		return isSubsetSum(arr, m-1, sum) ||
				isSubsetSum(arr, m-1, sum-arr[m-1]);
	}

	static boolean subsetSumDp(int[] arr,int m,int sum) {
		boolean[][] dp = new boolean[m+1][sum+1];
		
		//return 1 for sum = 0
		for(int i=0;i< m+1;i++) dp[i][0] = true;
		
		//return false if no coin i.e 0
		for(int i=0;i< sum+1;i++) dp[0][i] = false;
		
		for(int i=1;i< m+1;i++) {
			for(int curSum=1;curSum< sum+1;curSum++) {
				if(arr[i-1] > curSum)
					dp[i][curSum] = false;
				else
					dp[i][curSum] = dp[i-1][curSum] || dp[i-1][curSum-arr[i-1]];
				
			}
		}
		
		
		return dp[m][sum];
	}
	
    public static void main(String args[]) {
    	Scanner in = new Scanner(System.in);
    
    	char[] a = "abbg".toCharArray(); 
    	char[] b = "agbg".toCharArray();
    	
    	int[] arr = {1,2,3,4};
    	
    	System.out.println(isSubsetSum(arr, arr.length, 4));
    	System.out.println(subsetSumDp(arr,arr.length, 9));
  
    	
    	
    	

    	

    }
}

