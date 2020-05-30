//** Link : https://leetcode.com/problems/backspace-string-compare/

/**
 Stack Solution


 */
class Solution {
    
    static String getString(String S){
        
        String s1 = ""; 
        Stack<Character> s = new Stack<>();
        
        for(char x : S.toCharArray())
            if(x == '#')    
                if(!s.isEmpty()) s.pop();   
                else continue;
            
            else   s.push(x);
    
        //store in string
        while(!s.isEmpty())  s1 = s.pop() + s1;  
        
        return s1;
    }
    
    public boolean backspaceCompare(String S, String T) {
                
        return getString(S).equals(getString(T));
  
    }
}


/**
Two pointer Approach
*/


