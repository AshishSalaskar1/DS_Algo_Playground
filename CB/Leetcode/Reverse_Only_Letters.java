/**

Given a string S, return the "reversed" string 
where all characters that are not a letter stay in the same place, 
and all letters reverse their positions. 

Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
 

Note:

S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S doesn't contain \ or "

*/

// Two Pointer Approach
class Solution {
    public String reverseOnlyLetters(String S) {
        char[] s = S.toCharArray();
        
        int n = s.length;
        if(n==0) return "";
        
        int i = 0,j = n -1;
        
        while(i < j){
            while( !Character.isLetter(s[i]) ){
                i++;
                if(i == n) break;
            }
            
            while( !Character.isLetter(s[j]) ){
                j--;
                if( j == 0) break;
            }
            
            if( i >= j) break;
            
            char temp = s[i];
            s[i] = s[j];
            s[j] = temp;
            
            i++; j--;
        }
        
        return new String(s);
    }
}


