/**

Given an array A of non-negative integers, 
return an array consisting of all the even elements of A, 
followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 

*/

class Solution {
    public int[] sortArrayByParity(int[] a) {
        int n = a.length;
        if(n==0) return null;
        
       
        int i=0,j=n-1;
        while(i<j){
            while(a[i]%2 == 0){
                i++;
                if(i >= n) break;
            }
            
            while(a[j]%2 != 0){
                j--;
                if(j < 0) break;
            }
            
            
            if(i>=j) break;
            
            int temp = a[i];
            a[i] = a[j];
            a[j] = temp;
            
            i++; j--;
        }
        
        return a;
    }
}

// Slower but easy to understand : move only one right and left in each iteration
class Solution {
    public int[] sortArrayByParity(int[] a) {
        int n = a.length;
        if(n==0) return null;
        
       
        int i=0,j=n-1;
        while(i<j){
        
            if( (a[i]%2 != 0) && (a[j]%2 == 0)){
                int temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
            
            if(a[i] % 2 == 0) i++;
            if(a[j] %2 != 0) j--;
        
        }
        
        return a;
    }
}
