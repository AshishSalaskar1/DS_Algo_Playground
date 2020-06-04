/**

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.

*/

class Solution {
    public int candy(int[] a) {
        int n = a.length;
        
        int[] left = new int[n];
        int[] right = new int[n];
        
        //each get atleast 1 candy
        Arrays.fill(left,1);
        Arrays.fill(right,1);
        
        //left neigbors (L -> R)
        for(int i=1;i<n;i++)
            if(a[i] > a[i-1])    
                left[i] = left[i] + left[i-1];
        
        //right neighbors (L <- R)
        for(int i=n-2;i >= 0;i--)
            if(a[i] > a[i+1])    
                right[i] = right[i] + right[i+1];
        
        for(int i=0;i<n;i++)
            System.out.print(left[i]+" ");
        
        System.out.println();
        
        for(int i=0;i<n;i++)
            System.out.print(right[i]+" ");
        
        
        int res = 0;
        //for both left and right take max
        for(int i=0;i<n;i++)
            res += Math.max(left[i],right[i]);
        
        return res;
        
        
    }
}


