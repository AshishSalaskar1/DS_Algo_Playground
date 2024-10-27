package p1;

import java.util.*;


class Solution {
	
	static ArrayList<String> stringPermutation(String str){
		ArrayList<String> res = new ArrayList<>();
		
		if(str.length() == 0)
		{
			//" " and not ""
			res.add(" ");
			return res;
		}
		
		//ros: rest of string
		char ch = str.charAt(0);
		String ros = str.substring(1);
		
		ArrayList<String> rr = stringPermutation(ros);
		
		for(String x: rr) {
			for (int i = 0; i < x.length(); i++) {
				res.add(x.substring(0,i)+ch+x.substring(i));
			}
		}
		
		return res;
	}

	
	public static void main(String[] args) {
		
		System.out.println(stringPermutation("abcd"));
		
	
	}
	


}



