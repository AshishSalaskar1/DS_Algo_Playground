package p1;

import java.util.*;


class Solution {
	
	static int fact(int n) {
		if(n==0 || n==1 ) return 1;
		else return n*fact(n-1);
	}
	
	static int lexographicRank(String str) {
		int rank = 1;
		int n = str.length();
		int fMul = fact(n);
		
		int[] count = new int[256];
		
		for(int i=0;i<n;i++)	count[str.charAt(i)]++;
		
		//prefix array -> no of characters less rank than i = count[i-1]
		for(int i=1;i<256;i++)	count[i] += count[i-1];
		
		for(int i=0;i<n;i++) {
			fMul = fMul / (n-i);
			
			rank += count[str.charAt(i)-1] * fMul;
			
			//update count ie as str[i] is fixed , remove str[i]
			for(int k=str.charAt(i);k<256;k++)
				count[k]--;
				
		}
		

		return rank;
	}
	
	public static void main(String[] args) {
		String str = "geeksforgeeks";
		String s1 = "rosfd";
		
		System.out.println(lexographicRank("acb"));
		
		
	}
	
	/*lexographic rank: 
	 *str = abc
	 *Sorted permutations of str: 
	 *abc - 1
	 *acb - 2
	 *bac - 3
	 *bca - 4
	 
	 rank(acb) = 2
	 * */

}



