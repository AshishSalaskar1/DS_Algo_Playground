// Problem Link :  https://leetcode.com/problems/3sum
class Solution {
    public List<List<Integer>> threeSum(int[] a) {
        List<List<Integer>> res = new ArrayList<>();
        Set<List<Integer>> resSet = new HashSet<>();
        
        Arrays.sort(a);
        
        int n = a.length;
        
        for(int I=0; I<n-2 ; I++){
            int ele = a[I];
            
            int i = I+1;
            int j = n-1;
            
            while(i < j){
                int curSum = ele + a[i] + a[j];
                
                if(curSum == 0) {
                    // System.out.print("FOUND");
                    List<Integer> temp = new ArrayList<>();
                    temp.add(ele);temp.add(a[i]);temp.add(a[j]);
                    
                    resSet.add(temp);
                }
                
                if(curSum < 0) i++;
                else j--;
            }
            
        }
        
        for(List<Integer> x : resSet)
            res.add(x);
        
        return res;
    }
}
