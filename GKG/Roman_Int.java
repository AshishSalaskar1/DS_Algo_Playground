package p1;

import java.util.*;


class Solution {
	//Roman to int
	public int romanToInt(String s) {
        char[] a = s.toCharArray();
		
		Map<Character,Integer> m = new HashMap<>();
		m.put('I', 1);
		m.put('V', 5);
		m.put('X', 10);
		m.put('L', 50);
		m.put('C', 100);
		m.put('D', 500);
		m.put('M', 1000);
		
		int res = 0;
		
		for(int i=0;i<a.length-1;i++) {
			if (  m.get(a[i]) >=  m.get(a[i+1])	 ) {
				res += m.get(a[i]);
			}
			else {
				res -= m.get(a[i]);
			}
		}
		
		res = res + m.get(a[a.length-1]);
		return res;
        
    }
	
  //int to roman
  public static String intToRoman(int num) {
	   String[] thousands = {"", "M", "MM", "MMM"};
	   String[] hundreds = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
	   String[] tens = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
	   String[] units = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
	   
	   return thousands[num / 1000] + 
	        hundreds[(num % 1000) / 100] + 
	        tens[(num % 100) / 10] + 
	        units[num % 10];
  }
  
  public static void main(String[] args) {
	  
  }

}



