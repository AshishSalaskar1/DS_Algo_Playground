package java1;

import java.util.*;


public class Sol2 {
	
	static int startIndex;
	static int maxLength;
	
	
	static String LongestPalindromicSubstring(String str) {
		int n = str.length();
		
		if(n<2) return str;
		
		for(int i=0; i<n-1; i++) {
			//if mp is odd then end = start = middle
			isPalindrome(str, i,i);
			
			//if Midpoint i is even
			isPalindrome(str, i,i+1);
		}
		
		String ans = str.substring(startIndex,startIndex+maxLength);
		System.out.println(maxLength);
		return ans;
	}
	
	
	static private void isPalindrome(String s,int start,int end) {
		while(start>=0 && end<s.length() &&
				s.charAt(start) == s.charAt(end) ) {
			start--;
			end++;
		}
		
		//+1 bcause start-- while loop exits
		int curLen = end-start-1;
		if(curLen > maxLength ) {
			maxLength = curLen;
			startIndex = start+1;
		}
	}
	
	
	
	public static void main(String[] args){
		
		int[] arr= {1,2,3,4,5,6,7};
		
		System.out.println(LongestPalindromicSubstring("asadhuasdhsashijqowenqdb"));
		

		
		
    	
	}

}

