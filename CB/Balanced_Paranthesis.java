/*package whatever //do not write package name here */
package p1;

import java.util.*;
import java.io.*;

class Solution {
    
    static boolean isBalancedParanthesis(String inp) {
    	
    	Stack<Character> s = new Stack<>();
    	
    	char[] str = inp.toCharArray();
    	for(int i=0;i<str.length;i++) {
    		char br = str[i];
    		System.out.println(br);
    		if(br == '{' || br == '(' || br == '[')
    			s.push(br);
    		else {
    			
    			if(s.isEmpty()) return false;
    			
    			char topEle = s.peek();
    			if(br == '}' && topEle == '{')
    				s.pop();
    			else if(br == ')' && topEle == '(')
    				s.pop();
    			else if(br == ']' && topEle == '[')
    				s.pop();
    			
    			else
    				return false;
    		
    			}
    	}
    	
    	if(s.isEmpty()) return true;
    	else return false;
    	
    }
    
	public static void main (String[] args) {
		
		System.out.println(isBalancedParanthesis("()}}"));
	}
}
