// Problem Link :https://leetcode.com/problems/reverse-integer


class Solution {
    public int reverse(int x) {
        long res = 0;
        
        boolean isNeg = false;
        if(x < 0 ){
            isNeg = true;
            x = x*(-1);
        }
        
        while(x != 0){
            int rem = x % 10;
            
            res = (res*10) + rem;
            
            x = x/10;
        }
        
        if(isNeg)
            res *= -1;
        
        if(res >= Integer.MAX_VALUE || res <= Integer.MIN_VALUE)
            res = 0;
        
        return (int)res;
    }
}
