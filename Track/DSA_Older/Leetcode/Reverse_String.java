// Link : https://leetcode.com/problems/reverse-string
class Solution {
    public void reverseString(char[] s) {
        if(s.length <= 1) return;
        
        int i = 0;
        int j = s.length-1;
        
        while ( i< j){
            char temp = s[i];
            s[i] = s[j];
            s[j] = temp;
            
            i++;j--;
        }
    }
}
