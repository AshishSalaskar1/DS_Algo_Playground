class Solution {
    public boolean checkValidString(String s) {
        char[] str = s.toCharArray();        
        int n = str.length;
        
        if(n == 0) return true;
        if(n==1 && str[0] == '*') return true;
        
        int balance = 0;
        
        //L->R & replace * as (
        for(int i=0;i<n;i++){
            if(str[i] == ')') balance--;
            else balance++;
            
            //))
            if(balance<0) return false;
        }
        
        if(balance == 0) return true;
       
                
        //l<-R & replace * as )
        balance = 0;
        for(int i = n-1;i>=0;i--){
            if(str[i] == '(') balance--;
            else balance++;
            
            //()()((
            if(balance<0) return false;
        }
        
        return true;
 
   }
}
