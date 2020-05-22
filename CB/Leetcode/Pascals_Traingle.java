//Problem Link : https://leetcode.com/problems/pascals-triangle/
class Solution {
    public List<List<Integer>> generate(int n) {
        List<List<Integer>> res = new ArrayList<>();
        
        if(n == 0) return res;
        
        List<Integer> firstRow= new ArrayList<>();
        firstRow.add(1);
        res.add(firstRow);
        
        for(int i=1;i<n;i++){
            List<Integer> prevRow= res.get(i-1);
            List<Integer> row= new ArrayList<>();
            row.add(1);
            
            for(int j=1;j<i;j++){
                row.add(prevRow.get(j-1)+prevRow.get(j));
            }   
            
            row.add(1);
            res.add(row);
            
        }
        
        return res;
        
    }
}

/*
Without Extra Space

class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<>();
        if(numRows<1){
         return result;   
        }
        for(int i=0;i<numRows;i++){
            result.add(new ArrayList<Integer>());
        }
        result.get(0).add(1);
        
        for(int i=1;i<numRows;i++){
            result.get(i).add(1);
            for(int j =1;j<=i-1;j++){
                result.get(i).add(result.get(i-1).get(j-1)+result.get(i-1).get(j));
            }
            result.get(i).add(1);
        }
        return result;
    }
}

*/
