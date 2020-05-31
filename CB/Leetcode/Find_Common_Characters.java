/**

Given an array A of strings made only from lowercase letters, 
return a list of all characters that show up in all strings within the list (including duplicates).  
For example, if a character occurs 3 times in all strings but not 4 times, 
you need to include that character three times in the final answer.

You may return the answer in any order. 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]


*/

class Solution {
    public List<String> commonChars(String[] A) {
        List<String> res = new ArrayList<>();
        
        if(A.length == 0) return res;
        
        int[] freq = new int[26];
        Arrays.fill(freq,Integer.MAX_VALUE);

        for(int i=0;i<A.length;i++){
            
            int[] f = new int[26];
            
            for(char ch : A[i].toCharArray())   
                f[ch - 'a']++;
            
            for(int I=0;I<26;I++)
                freq[I] = Math.min(freq[I],f[I]);
            
        }
        
        
        for(int i=0;i<26;i++)
            if(freq[i] != 0){
                for(int j=0;j<freq[i];j++){
                    res.add((char)(i+'a')+ "" );
                }
            }
        
        return res;
        
        
    }
}
