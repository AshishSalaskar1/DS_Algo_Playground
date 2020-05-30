/**
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
You may return any answer array that satisfies this condition.
*/

class Solution {
    public int[] sortArrayByParityII(int[] a) {
        int n = a.length;
        
        //hint: same no of even and odd
        // so if any odd no is at even index..then another even no is at odd index
        //swap those two
        
        int i = 0, j = 1;
        
        while(i<n && j<n){
            while(i<n && a[i]%2 == 0)
                i += 2;
                
            while(j<n && a[j]%2 == 1)
                j += 2;
            
            // System.out.println(i+":"+j);
            
            if(i<n && j<n){
                int temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
                
        }
        
        return a;
    }
}


