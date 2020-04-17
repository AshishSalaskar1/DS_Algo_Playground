package p1;

import java.util.*;
import java.io.*;

class Main
{	
	static String intToRoman(int n) {
		String res = "";
		
		String[] roman = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
		int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
		
		
		int i = 0;
		while(n > 0) {
			if(n >= values[i])
			{
				res = res + roman[i];
				n = n - values[i];
			}
			else
				i++;
			
		}

		
		return res;
	}
	
	public static void main (String[] args) throws Exception
	 {
//		System.out.println(LCS("heap","peapk"));
		System.out.println(intToRoman(449));
		
 	 }
}
