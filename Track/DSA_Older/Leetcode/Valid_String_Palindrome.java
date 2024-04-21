// https://leetcode.com/problems/valid-palindrome
class Solution {
    public boolean isPalindrome(String s) {
        char[] a = s.toLowerCase().toCharArray();
        
        if(a.length <= 1)  return true;
        
        int i = 0 , j = a.length-1;

        while( i <= j){
            if(!Character.isDigit(a[i]) && !Character.isLetter(a[i])){
                i++;
                continue;
            }
            
            if(!Character.isDigit(a[j]) && !Character.isLetter(a[j])){
                j--;
                continue;
            }
            
            if(a[i]!= a[j]) return false;
            else {
                i++;j--;
            }
        }
        
        return true;
    }
}
