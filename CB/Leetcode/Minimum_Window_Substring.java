class Solution {
    public String minWindow(String S, String T) {
        char[] s = S.toCharArray();
        char[] t = T.toCharArray();
        
        int n = s.length;
        int left = 0,right=0,minLen = Integer.MAX_VALUE,minIndex = -1;
        int[] f = new int[128];
        for(char c : t) f[c]++;
        int count = t.length;
        
        while(right < n){
            char rC = s[right];
            if(f[rC] > 0) count--;
            f[rC]--;
            
            right++;
            while(count == 0){
                
                int len = right - left;
                
                if(len < minLen){
                    minLen = len;
                    minIndex = left;
                }
                
                char lC = s[left];
                
                f[lC]++;
                if(f[lC] > 0) count++;
                left++;
            }
        }
        
        return (minLen == Integer.MAX_VALUE) ? "" : S.substring(minIndex,minIndex+minLen);
        
        
    }
}



// Shorthand code 
class Solution {
    public String minWindow(String S, String T) {
        char[] s = S.toCharArray();
        char[] t = T.toCharArray();
        
        int n = s.length;
        int left = 0,right=0,minLen = Integer.MAX_VALUE,minIndex = -1;
        int[] f = new int[128];
        for(char c : t) f[c]++;
        int count = t.length;
        
        while(right < n){
            if( f[s[right++]]-- > 0) count--;
            
            while(count == 0){
                
                int len = right-left;
                if(len < minLen){
                    minLen = len;
                    minIndex = left;
                }
                
                if( ++f[s[left++]] > 0) count++;
            }
            
        }
        
        return (minLen == Integer.MAX_VALUE) ? "" : S.substring(minIndex,minIndex+minLen);
        
        
    }
}

































