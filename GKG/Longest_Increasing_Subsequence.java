package p1;

import java.util.*;


class Solution {
	
	static int longestIncreasingSubsequence(int[] arr){
		int n = arr.length,temp;
		//Intger bcoz we need to use max function
		Integer[] dp = new Integer[n];
		
		dp[0] = 1;
		for (int i = 1; i < n; i++) {
			//LIS at i will be atleast 1
			dp[i] = 1; 
			for(int j=i-1;j>=0;j--) {
				if(arr[j] > arr[i]) continue;
				
				temp = dp[j] + 1;
				if(temp > dp[i]) dp[i] = temp;
				
			}
		}
		
		//find max in dp array
		int res = Collections.max(Arrays.asList(dp));
		
		return res;
	}
		

	
	public static void main(String[] args) {
		int[] arr  = {50, 3, 10, 7, 40, 80};
		System.out.println(longestIncreasingSubsequence(arr));
		
		
	
	}
	


}



