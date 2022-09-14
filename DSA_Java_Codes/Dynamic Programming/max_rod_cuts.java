package p1;

import java.util.*;
import java.lang.*;
import java.io.*;

class Main
 {
	
	static int[] dp = new int[4000];
	static int[] len = new int[3];
	
	static int rodCut(int n) {
		if(n>=0 && dp[n] != 0)
			return dp[n];
		
		if(n==0) {
			dp[n] = 0;
			return 0;
		}
		
		if(n<0) {
			return -1;
		}
		
		int res = Math.max(Math.max(rodCut(n-len[0]),rodCut(n-len[1])), rodCut(n-len[2]));
		res = (res == -1) ? -1 : 1 + res;
		dp[n] = res;
		return res;
		
		
	}

	
	
	
	
	

		

	public static void main (String[] args) throws Exception
	 {
	    int[] arr = new int[]{-23, 1000, 10, 20, 10, 17, 17}; 
	    
	    len[0] = 20;
	    len[1] = 20;
	    len[2] = 3;
	    
	    System.out.println(rodCut(23));
	    System.out.println(RR(23));
	    
	  
 	 }
}
