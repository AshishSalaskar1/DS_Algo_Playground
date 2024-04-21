/**

Given a sorted array arr, two integers k and x, find the k closest elements to x in the array. 
The result should also be sorted in ascending order.
If there is a tie, the smaller elements are always preferred.

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

*/

class Solution {
    static class Pair{
        int index,val;
        public Pair(int x,int y){
            this.index = x;
            this.val = y;
        }
    }
    
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        List<Pair> l = new ArrayList<>();
        for(int i=0;i<arr.length;i++)
            l.add(new Pair(i,Math.abs(x-arr[i])));
        
        Collections.sort(l,new Comparator<Pair>(){
            @Override
            public int compare(Pair a,Pair b){
                int res =  Integer.valueOf(a.val).compareTo(b.val);
                //if first condition is same
                if(res == 0)
                   return Integer.valueOf(arr[a.index]).compareTo(arr[b.index]);
                else return res;
            }
        });
        
        List<Integer> res = new ArrayList<>();
        for(int i=0;i<k;i++)
            res.add(arr[l.get(i).index]);
        
        Collections.sort(res);
        return res;
        
    }
}
