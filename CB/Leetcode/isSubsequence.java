class Solution {
    
    static char[] s;
    static char[] str;
    static int m,n;
    
    
    static boolean isSS(int i,int j){
        if(i==0)
            return true;
        if(j==0)
            return false;
        
        if(s[i-1] == str[j-1])
            return isSS(i-1,j-1);
        else
            return isSS(i,j-1);
    }
    
    public boolean isSubsequence(String S, String t) {
        
        s = S.toCharArray();
        str = t.toCharArray();
        
        m = s.length;
        n = str.length;
        
        return isSS(m,n);
        
    }
}
