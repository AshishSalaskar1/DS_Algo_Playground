package p1;

import java.util.*;


class Solution {
	
	static boolean isSameCount(int[] a,int[] b) {
		for(int i=0;i<a.length;i++)
			if(a[i] != b[i])
				return false;
		
		return true;
	}
	
	
	//check if anangram of s1 is present in s2
	public static boolean anagramSearch(String s1,String s2) {
		int k = s1.length();
		int n = s2.length();
		
		int[] kCount = new int[256]; 
		int[] winCount = new int[256];
		
		
		//Populate search count values
		for(int i=0;i<s1.length();i++) kCount[s1.charAt(i)]++;
		
		//Populate for first window of size k
		for(int i=0;i<k;i++) winCount[s2.charAt(i)]++;
		
		
		if(isSameCount(kCount, winCount))	return true;
		
		
		//Slide a window of size k | first window already calculated
		for(int i=1;i<n-k + 1;i++) {
//			System.out.println(s2.substring(i,i+k));
			//update after window sliding
			winCount[s2.charAt(i-1)]--;
			winCount[s2.charAt(i-1+k)]++;
			
			if(isSameCount(kCount,winCount)) return true;
		}
		
		return false;
	}
	
	public static void main(String[] args) {
		String str = "geeksforgeeks";
		String s1 = "rosfd";
		
		System.out.println(anagramSearch(s1, str));
		
		
	}

}



